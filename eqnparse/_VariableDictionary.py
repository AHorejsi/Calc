from os import mkdir, chdir, getcwd, path
from calc.MathFunction import PI, E
from itertools import chain
from eqnparse.SingletonException import SingletonException
from eqnparse.EquationParsing import _parseVariableValue


class _VariableDictionary:
    __instance = None
    __filePath = "C:/Users/Public/Public Documents"

    def __init__(self):
        if _VariableDictionary.__instance is None:
            _VariableDictionary.__instance = self

            self.__universalVars = {"pi" : PI, "e" : E}
            self.__tempVars = {}
            self.__permVars = {}
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
            value = _parseVariableValue(parts[1])

            if value is not None:
                self.__permVars[name] = value

        file.close()

    def savePermVars(self):
        file = _VariableDictionary.__findFile("w")
        file.truncate(0)

        for varName, varValue in self.__permVars.items():
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

        return open(path + "CalcVars.txt", mode=modeInput)

    def getTempVar(self, varName):
        return self.__tempVars.get(varName)

    def getPermVar(self, varName):
        return self.__permVars.get(varName)

    def getUniversalVar(self, varName):
        return self.__universalVars.get(varName)

    def __getitem__(self, varName):
        # Search "Var" dictionary
        var = self.getTempVar(varName)
        if var is not None:
            return var

        # Search "PermVar" dictionary
        permVar = self.getPermVar(varName)
        if permVar is not None:
            return permVar

        # Search "UniversalVar" dictionary
        universalVar = self.getUniversalVar(varName)
        if universalVar is not None:
            return universalVar

        return None

    def setTempVar(self, varName, varValue):
        if varName in self.__permVars:
            raise KeyError("Variable named \"" + varName + "\" already exists in permanent variables")
        if varName in self.__universalVars:
            raise KeyError("Invalid variable name \"" + varName + "\"")

        self.__tempVars[varName] = varValue

    def setPermVar(self, varName, varValue):
        if varName in self.__tempVars:
            raise KeyError("Variable names \"" + varName + "\" already exists in temporary variables")
        if varName in self.__universalVars:
            raise KeyError("Invalid variable name \"" + varName + "\"")

        self.__permVars[varName] = varValue

    def hasTempVar(self, varName):
        return varName in self.__tempVars

    def hasPermVar(self, varName):
        return varName in self.__permVars

    def hasUniversalVar(self, varName):
        return varName in self.__universalVars

    def __contains__(self, varName):
        return self.hasTempVar(varName) or self.hasPermVar(varName) or self.hasUniversalVar(varName)

    def removeVar(self, varName):
        try:
            del self.__tempVars[varName]
        except KeyError:
            # Do nothing
            pass

    def removePermVar(self, varName):
        try:
            del self.__permVars[varName]
        except KeyError:
            # Do nothing
            pass

    def iterTempVars(self):
        return iter(self.__tempVars)

    def iterPermVars(self):
        return iter(self.__permVars)

    def iterUniversalVars(self):
        return iter(self.__universalVars)

    def __iter__(self):
        return chain(self.iterUniversalVars(), self.iterPermVars(), self.iterTempVars())

    def clearTempVars(self):
        self.__tempVars.clear()

    def clearPermVars(self):
        self.__permVars.clear()

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
