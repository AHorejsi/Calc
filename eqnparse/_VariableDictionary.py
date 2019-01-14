from os import mkdir, chdir, getcwd, path
from calc.MathFunction import PI, E
from itertools import chain
from re import fullmatch, split
from calc import Complex, Quaternion, Vector, Matrix
from eqnparse.SingletonException import SingletonException


class _VariableDictionary:
    __instance = None
    __filePath = "C:/Users/Public/Public Documents"

    def __init__(self):
        if _VariableDictionary.__instance is None:
            _VariableDictionary.__instance = self

            self.__universalVars = {"pi" : PI, "e" : E}
            self._vars = {}
            self._permVars = {}
            self.__readPermVars()
        else:
            raise SingletonException("This is a singleton class")

    @staticmethod
    def instance():
        if _VariableDictionary.__instance is None:
            return _VariableDictionary()
        else:
            return _VariableDictionary.__instance

    def __readPermVars(self):
        file = _VariableDictionary.__findFile("r")
        lines = file.readlines(path.getsize(_VariableDictionary.__filePath + "Calc/CalcVars.txt"))

        for line in lines:
            parts = line.split(",")
            name = parts[0]
            value = _VariableDictionary.__parseValue(parts[1])

            self._permVars[name] = value

        file.close()

    @staticmethod
    def __parseValue(strValue):
        if fullmatch("(-?\d+.?\d+)(e\d+)?[+|-](\d+.?\d+)(e\d+)?i", strValue) is not None:
            # Type is Complex
            nums = split("[+|-]", strValue[0 : len(strValue) - 1])

            return Complex(float(nums[0]), float(nums[1]))

        elif fullmatch("(-?\d+.?\d+)(e\d+)?[+|-](\d+.?\d+)(e\d+)?i[+|-](\d+.?\d+)(e\d+)?j[+|-](\d+.?\d+)(e\d+)?k",
                       strValue) is not None:
            # Type is Quaternion
            nums = split("[+|-]", strValue)

            return Quaternion(float(nums[0]), float(nums[1][0 : len(nums[1]) - 1]),
                              float(nums[2][0 : len(nums[2]) - 1]), float(nums[3][0 : len(nums[3]) - 1]))
        elif fullmatch("<((-?\d+.?\d+)(e\d+)?,)*((-?\d+.?\d+)(e\d+)?)?>", strValue) is not None:
            # Type is Vector
            nums = split(",", strValue[1 : len(strValue) - 1])
            listOfNums = []

            for numStr in nums:
                listOfNums.append(float(numStr))

            return Vector(listOfNums)

        else:
            # Type is Matrix
            rows = list(filter(lambda string: string != "", split("\[\[|\]\]|\],\[", strValue)))
            table = []

            for row in rows:
                newRow = []
                listOfNums = split(",", row)

                for numStr in listOfNums:
                    newRow.append(float(numStr))

                table.append(newRow)

            return Matrix(table)

    def savePermVars(self):
        file = _VariableDictionary.__findFile("w")
        file.truncate(0)

        for varName, varValue in self._permVars.items():
            varData = str(varName) + "," + str(varValue) + "\n"
            file.write(varData)

        file.close()

    @staticmethod
    def __findFile(modeInput):
        path = _VariableDictionary.__filePath + "Calc"
        chdir(path)

        if getcwd() != path:
            mkdir(path)
            chdir(path)

        return open("CalcVars.txt", mode=modeInput)

    def getVar(self, varName):
        return self._vars.get(varName)

    def getPermVar(self, varName):
        return self._permVars.get(varName)

    def getUniversalVar(self, varName):
        return self.__universalVars.get(varName)

    def __getitem__(self, varName):
        # Search "Var" dictionary
        var = self.getVar(varName)
        if var is not None:
            return var

        # Search "PermVar" dictionary
        permVar = self.getPermVar(varName)
        if permVar is not None:
            return permVar

        # Search "Universal Var" dictionary
        universalVar = self.getUniversalVar(varName)
        if universalVar is not None:
            return universalVar

        return None

    def setVar(self, varName, varValue):
        if varName in self._permVars:
            raise KeyError("Variable named \"" + varName + "\" already exists in permanent variables")
        if varName in self.__universalVars:
            raise KeyError("Invalid variable name \"" + varName + "\"")

        self._vars[varName] = varValue

    def setPermVar(self, varName, varValue):
        if varName in self._vars:
            raise KeyError("Variable names \"" + varName + "\" already exists in temporary variables")
        if varName in self.__universalVars:
            raise KeyError("Invalid variable name \"" + varName + "\"")

        self._permVars[varName] = varValue

    def hasVar(self, varName):
        return varName in self._vars

    def hasPermVar(self, varName):
        return varName in self._permVars

    def hasUniversalVar(self, varName):
        return varName in self.__universalVars

    def __contains__(self, varName):
        return self.hasVar(varName) or self.hasPermVar(varName) or self.hasUniversalVar(varName)

    def removeVar(self, varName):
        try:
            del self._vars[varName]
        except KeyError:
            # Do nothing
            pass

    def removePermVar(self, varName):
        try:
            del self._permVars[varName]
        except KeyError:
            # Do nothing
            pass

    def iterVars(self):
        return iter(self._vars)

    def iterPermVars(self):
        return iter(self._permVars)

    def iterUniversalVars(self):
        return iter(self.__universalVars)

    def __iter__(self):
        return chain(self.iterUniversalVars(), self.iterPermVars(), self.iterVars())

    def clearVars(self):
        self._vars.clear()

    def clearPermVars(self):
        self._permVars.clear()

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        rep = ""

        for varName, varValue in self:
            rep += varName + " = " + varValue + "\n"

        return rep

    def __repr__(self):
        return str(self)
