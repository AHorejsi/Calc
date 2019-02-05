from __future__ import annotations
from typing import TextIO, Union, Iterable, Tuple, Optional
from calc.MathConstant import PI, EULER, IMAG_0, IMAG_1, IMAG_2, POSITIVE_INFINITY, NEGATIVE_INFINITY
from calc import MathEntity, Complex, Quaternion
from eqnparse.ValueParsing import parseVariableValue
from os import mkdir, chdir, getcwd, path
from itertools import chain
from re import split


class _VariableDictionary:
    __instance = None

    def __init__(self):
        if _VariableDictionary.__instance is None:
            _VariableDictionary.__instance = self

            self.__universalVars = {"pi" : PI,
                                    "e" : EULER,
                                    "i" : IMAG_0,
                                    "j" : IMAG_1,
                                    "k" : IMAG_2,
                                    "pos_infinity" : POSITIVE_INFINITY,
                                    "neg_infinity" : NEGATIVE_INFINITY}
            self.__tempVars = {}
            self.__permVars = {}
            self.__mainDirectory = getcwd()
            self.__dataDirectory = "C:\\Users\\alexh\\Documents"
            self.__readPermVars()
        else:
            raise Exception("This is a singleton class")

    @staticmethod
    def instance() -> _VariableDictionary:
        if _VariableDictionary.__instance is None:
            return _VariableDictionary()
        else:
            return _VariableDictionary.__instance

    def __readPermVars(self) -> None:
        file = self.__findFile("r")
        lines = file.readlines(path.getsize(self.__dataDirectory + "\\Calc\\Perms\\CalcVars.txt"))

        for line in lines:
            parts = split("\s*:\s*", line)
            name = parts[0]
            value = parseVariableValue(parts[1])

            if value is not None:
                self.__permVars[name] = value

        file.close()
        chdir(self.__mainDirectory)

    def savePermVars(self) -> None:
        file = self.__findFile("w")
        file.truncate(0)

        for varName, varValue in self.__permVars.items():
            varData = str(varName) + ":" + str(varValue) + "\n"
            file.write(varData)

        file.close()
        chdir(self.__mainDirectory)

    def __findFile(self, modeInput: str) -> TextIO:
        path = self.__dataDirectory + "\\Calc\\Perms"
        chdir(path)

        if getcwd() != path:
            mkdir(path)
            chdir(path)

        return open(path + "\\CalcVars.txt", mode=modeInput)

    def getTempVar(self, varName: str) -> Optional[Union[int, float, bool, MathEntity]]:
        return self.__tempVars.get(varName)

    def getPermVar(self, varName: str) -> Optional[Union[int, float, bool, MathEntity]]:
        return self.__permVars.get(varName)

    def getUniversalVar(self, varName: str) -> Optional[Union[int, float, Complex, Quaternion]]:
        return self.__universalVars.get(varName)

    def __getitem__(self, varName: str) -> Optional[Union[float, bool, MathEntity]]:
        # Search "TempVar" dictionary
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

    def setTempVar(self, varName: str, varValue: Union[int, float, bool, MathEntity]) -> None:
        if varName in self.__permVars:
            raise KeyError("Variable named \"" + varName + "\" already exists in permanent variables")
        if varName in self.__universalVars:
            raise KeyError("Invalid variable name \"" + varName + "\"")

        self.__tempVars[varName] = varValue

    def setPermVar(self, varName: str, varValue: Union[int, float, bool, MathEntity]) -> None:
        if varName in self.__tempVars:
            raise KeyError("Variable names \"" + varName + "\" already exists in temporary variables")
        if varName in self.__universalVars:
            raise KeyError("Invalid variable name \"" + varName + "\"")

        self.__permVars[varName] = varValue

    def hasTempVar(self, varName: str) -> bool:
        return varName in self.__tempVars

    def hasPermVar(self, varName: str) -> bool:
        return varName in self.__permVars

    def hasUniversalVar(self, varName: str) -> bool:
        return varName in self.__universalVars

    def __contains__(self, varName: str) -> bool:
        return self.hasTempVar(varName) or self.hasPermVar(varName) or self.hasUniversalVar(varName)

    def removeTempVar(self, varName: str) -> None:
        try:
            del self.__tempVars[varName]
        except KeyError:
            # Do nothing
            pass

    def removePermVar(self, varName: str) -> None:
        try:
            del self.__permVars[varName]
        except KeyError:
            # Do nothing
            pass

    def iterTempVars(self) -> Iterable[Union[Tuple[str, int], Tuple[str, float], Tuple[str, bool], Tuple[str, MathEntity]]]:
        return iter(self.__tempVars.items())

    def iterPermVars(self) -> Iterable[Union[Tuple[str, int], Tuple[str, float], Tuple[str, bool], Tuple[str, MathEntity]]]:
        return iter(self.__permVars.items())

    def iterUniversalVars(self) -> Iterable[Union[Tuple[str, float], Tuple[str, Complex], Tuple[str, Quaternion]]]:
        return iter(self.__universalVars.items())

    def __iter__(self) -> Iterable[Union[Tuple[str, int], Tuple[str, float], Tuple[str, bool], Tuple[str, MathEntity]]]:
        return chain(self.iterUniversalVars(), self.iterPermVars(), self.iterTempVars())

    def clearTempVars(self) -> None:
        self.__tempVars.clear()

    def clearPermVars(self) -> None:
        self.__permVars.clear()

    def __eq__(self, other: _VariableDictionary) -> bool:
        return self is other

    def __ne__(self, other: _VariableDictionary) -> bool:
        return not (self == other)

    def __str__(self) -> str:
        rep = ""

        for (varName, varValue) in self:
            rep += str(varName) + " = " + str(varValue) + "\n"

        return rep

    def __repr__(self) -> str:
        return str(self)
