from math import ceil, floor
from itertools import chain
from os import mkdir, chdir, getcwd, path
from eqnparse.EquationParsing import _parseVariableValue
from calc.MathFunction import ceil, floor, exp, log, signum, sqrt, sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, \
                              asinh, acosh, atanh, sec, csc, cot, sech, csch, coth, asec, acsc, acot, asech, acsch, \
                              acoth


class _FunctionDictionary:
    __instance = None
    __filePath = "C:/Users/Public/Public Documents"

    def __init__(self):
        if _FunctionDictionary.__instance is None:
            _FunctionDictionary.__instance = self

            self.__universalFuncs = {"abs" : abs,
                                     "ceil" : ceil,
                                     "floor" : floor,
                                     "round" : round,
                                     "xor" : lambda bool1, bool2: ((not bool1) and bool2) or (bool1 and (not bool2)),
                                     "max" : lambda real1, real2: real1 if real1 > real2 else real2,
                                     "min" : lambda real1, real2: real1 if real1 < real2 else real2,
                                     "mod" : lambda real1, real2: real1 % real2,
                                     "exp" : exp,
                                     "ln" : lambda entity: log(entity),
                                     "log" : lambda entity, base: log(entity, base),
                                     "sgn" : signum,
                                     "sqrt" : sqrt,
                                     "cbrt" : lambda entity: entity ** 0.33333333333333,
                                     "sin" : sin,
                                     "cos" : cos,
                                     "tan" : tan,
                                     "sinh" : sinh,
                                     "cosh" : cosh,
                                     "tanh" : tanh,
                                     "arcsin" : asin,
                                     "arccos" : acos,
                                     "arctan" : atan,
                                     "arcsinh" : asinh,
                                     "arccosh" : acosh,
                                     "arctanh" : atanh,
                                     "sec" : sec,
                                     "csc" : csc,
                                     "cot" : cot,
                                     "sech" : sech,
                                     "csch" : csch,
                                     "coth" : coth,
                                     "arcsec" : asec,
                                     "arccsc" : acsc,
                                     "arccot" : acot,
                                     "arcsech" : asech,
                                     "arccsch" : acsch,
                                     "arccoth" : acoth,
                                     "bit_and" : lambda int1, int2: int1 & int2,
                                     "bit_or" : lambda int1, int2: int1 | int2,
                                     "bit_not" : lambda integer: ~integer,
                                     "bit_xor" : lambda int1, int2: int1 ^ int2,
                                     "dot" : lambda vec1, vec2: vec1.dot(vec2),
                                     "cross" : lambda vec1, vec2: vec1.cross(vec2),
                                     "mag" : lambda vec: vec.magnitude,
                                     "angle" : lambda vec1, vec2: vec1.angleBetween(vec2),
                                     "dist" : lambda vec1, vec2: vec1.distanceFrom(vec2),
                                     "det" : lambda matrix: matrix.determinant,
                                     "inv" : lambda matrix: matrix.inverse(),
                                     "transpose" : lambda matrix: matrix.transpose(),
                                     "norm" : lambda entity: entity.normalize(),
                                     "conj" : lambda entity: entity.conjugate()}
            self.__tempFuncs = {}
            self.__permFuncs = {}
            self.__readPermFuncs()
        else:
            raise Exception("This is a singleton class")

    @staticmethod
    def instance():
        if _FunctionDictionary.__instance is None:
            return _FunctionDictionary()
        else:
            return _FunctionDictionary.__instance

    def __readPermFuncs(self):
        file = _FunctionDictionary.__findFile("r")
        lines = file.readlines(path.getsize(_FunctionDictionary.__filePath + "Calc/CalcVars.txt"))

        for line in lines:
            parts = line.split(":")
            name = parts[0]
            value = _parseVariableValue(parts[1])

            if value is not None:
                self.__permFuncs[name] = value

        file.close()

    def savePermFuncs(self):
        file = _FunctionDictionary.__findFile("w")
        file.truncate(0)

        for varName, varValue in self.__permFuncs.items():
            varData = str(varName) + ":" + str(varValue) + "\n"
            file.write(varData)

        file.close()

    @staticmethod
    def __findFile(modeInput):
        path = _FunctionDictionary.__filePath + "Calc"
        chdir(path)

        if getcwd() != path:
            mkdir(path)
            chdir(path)

        return open(path + "CalcVars.txt", mode=modeInput)

    def getUniversalFunc(self, funcName):
        return self.__universalFuncs.get(funcName)

    def getTempFunc(self, funcName):
        return self.__tempFuncs.get(funcName)

    def getPermFunc(self, funcName):
        return self.__permFuncs.get(funcName)

    def __getitem__(self, funcName):
        # Search "TempFunc" dictionary
        tempFunc = self.getTempFunc(funcName)
        if tempFunc is not None:
            return tempFunc

        # Search "PermFunc" dictionary
        permFunc = self.getPermFunc(funcName)
        if permFunc is not None:
            return permFunc

        # Search "UniversalFunc" dictionary
        universalFunc = self.getUniversalFunc(funcName)
        if universalFunc is not None:
            return universalFunc

        return None

    def hasTempFunc(self, funcName):
        return funcName in self.__tempFuncs

    def hasPermFunc(self, funcName):
        return funcName in self.__permFuncs

    def hasUniversalFunc(self, funcName):
        return funcName in self.__universalFuncs

    def __contains__(self, funcName):
        return self.hasTempFunc(funcName) or self.hasPermFunc(funcName) or self.getUniversalFunc(funcName)

    def removeTempFunc(self, funcName):
        try:
            del self.__tempFuncs[funcName]
        except KeyError:
            # Do nothing
            pass

    def removePermFunc(self, funcName):
        try:
            del self.__permFuncs[funcName]
        except KeyError:
            # Do nothing
            pass

    def iterTempFuncs(self):
        return iter(self.__tempFuncs)

    def iterPermFuncs(self):
        return iter(self.__permFuncs)

    def iterUniversalFuncs(self):
        return iter(self.__universalFuncs)

    def __iter__(self):
        return chain(self.__tempFuncs, self.__permFuncs, self.__universalFuncs)

    def clearTempFuncs(self):
        self.__tempFuncs.clear()

    def clearPermFuncs(self):
        self.__permFuncs.clear()

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self is not other

