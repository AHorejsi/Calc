import os
from calc.MathFunction import PI, E
from itertools import chain


class _VariableDictionary:
    __instance = None
    __filePath = "C:/Users/Public/Public Documents"

    def __init__(self):
        if _VariableDictionary.__instance is None:
            _VariableDictionary.__instance = self

            self._universalVars = {"pi" : PI, "e" : E}
            self._vars = {}
            self._permVars = {}
            self.__readPermVars()
        else:
            raise Exception("This is a singleton class")

    @staticmethod
    def instance():
        if _VariableDictionary.__instance is None:
            return _VariableDictionary()
        else:
            return _VariableDictionary.__instance

    def __readPermVars(self):
        file = _VariableDictionary.__findFile("r")
        lines = file.readlines(os.path.getsize(_VariableDictionary.__filePath + "Calc/CalcVars.txt"))

        for line in lines:
            parts = line.split(",")

            self._permVars[parts[0]] = parts[1]

        file.close()

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
        os.chdir(path)

        if os.getcwd() == path:
            return open("CalcVars.txt", mode=modeInput)
        else:
            os.mkdir(_VariableDictionary.__filePath)
            # TODO File creation

    def getVar(self, varName):
        return self._vars.get(varName)

    def getPermVar(self, varName):
        return self._permVars.get(varName)

    def getUniversalVar(self, varName):
        return self._universalVars.get(varName)

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
        if varName in self._universalVars:
            raise Exception("Invalid variable name \"" + varName + "\"")

        self._vars[varName] = varValue

    def setPermVar(self, varName, varValue):
        if varName in self._vars:
            raise KeyError("Variable names \"" + varName + "\" already exists in temporary variables")
        if varName in self._universalVars:
            raise Exception("Invalid variable name \"" + varName + "\"")

        self._permVars[varName] = varValue

    def hasVar(self, varName):
        return varName in self._vars

    def hasPermVar(self, varName):
        return varName in self._permVars

    def hasUniversalVar(self, varName):
        return varName in self._universalVars

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
        return iter(self._universalVars)

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
            rep += varName + " = " + varValue

        return rep

    def __repr__(self):
        return str(self)
