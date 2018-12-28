import os


class _VariableDictionary:
    __instance = None
    __filePath = "C:/Users/Public/Public Documents/Calc"

    def __init__(self):
        if _VariableDictionary.__instance is None:
            _VariableDictionary.__instance = self

            self._vars = {}
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
        self._permVars = {}

        file = _VariableDictionary.__findFile("r")
        lines = file.readlines(os.path.getsize(_VariableDictionary.__filePath + "/CalcVars.txt"))

        for line in lines:
            parts = line.split(":")

            self._permVars[parts[0]] = parts[1]

        file.close()

    def savePermVars(self):
        file = _VariableDictionary.__findFile("w")
        file.truncate(0)

        for varName, varValue in self._permVars.items():
            varData = str(varName) + ":" + str(varValue) + "\n"
            file.write(varData)

        file.close()

    @staticmethod
    def __findFile(modeInput):
        os.chdir(_VariableDictionary.__filePath)

        if os.getcwd() == _VariableDictionary.__filePath:
            return open("CalcVars.txt", mode=modeInput)
        else:
            os.mkdir(_VariableDictionary.__filePath)
            # TODO File creation

    def getVar(self, varName):
        return self._vars.get(varName)

    def getPermVar(self, varName):
        return self._permVars.get(varName)

    def hasVar(self, varName):
        return varName in self._vars

    def hasPermVar(self, varName):
        return varName in self._permVars

    def removeVar(self, varName):
        try:
            del self._vars[varName]
        except KeyError:
            pass

    def removePermVar(self, varName):
        try:
            del self._permVars[varName]
        except KeyError:
            pass

    def iterVars(self):
        return self._vars.__iter__()

    def iterPermVars(self):
        return self._permVars.__iter__()

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

        for varName, varValue in self.iterPermVars():
            rep += varName + " = " + varValue

        for varName, varValue in self.iterVars():
            rep += varName + " = " + varValue

        return rep

    def __repr__(self):
        return str(self)
