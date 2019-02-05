from __future__ import annotations
from typing import Optional, Iterable, Tuple
from math import factorial, ceil, floor
from random import randrange, random
from itertools import chain
from calc.MathFunction import expMath, logMath, signumMath, sqrtMath, sinMath, cosMath, tanMath, sinhMath, coshMath, \
                              tanhMath, asinMath, acosMath, atanMath, asinhMath, acoshMath, atanhMath


class _FunctionDictionary:
    __instance = None

    def __init__(self):
        if _FunctionDictionary.__instance is None:
            _FunctionDictionary.__instance = self

            self.__universalFuncs = {"abs" : abs,
                                     "ceil" : ceil,
                                     "floor" : floor,
                                     "round" : round,
                                     "re" : lambda value: value if (type(value) is int) or (type(value) is float) else value.real,
                                     "im0" : lambda value: value.imag0,
                                     "im1" : lambda quaternion: quaternion.imag1,
                                     "im2" : lambda quaternion: quaternion.imag2,
                                     "dim" : lambda vector: len(vector),
                                     "rows" : lambda matrix: matrix.rowLength,
                                     "cols" : lambda matrix: matrix.columnLength,
                                     "xor" : lambda bool1, bool2: ((not bool1) and bool2) or (bool1 and (not bool2)),
                                     "max" : lambda real1, real2: real1 if real1 > real2 else real2,
                                     "min" : lambda real1, real2: real1 if real1 < real2 else real2,
                                     "mod" : lambda real1, real2: real1 % real2,
                                     "exp" : expMath,
                                     "ln" : lambda entity: logMath(entity),
                                     "log" : lambda entity, base: logMath(entity) / logMath(base),
                                     "sgn" : signumMath,
                                     "sqrt" : sqrtMath,
                                     "cbrt" : lambda entity: entity ** 0.33333333333333,
                                     "rand_int" : randrange,
                                     "rand" : random,
                                     "sin" : sinMath,
                                     "cos" : cosMath,
                                     "tan" : tanMath,
                                     "sinh" : sinhMath,
                                     "cosh" : coshMath,
                                     "tanh" : tanhMath,
                                     "arcsin" : asinMath,
                                     "arccos" : acosMath,
                                     "arctan" : atanMath,
                                     "arcsinh" : asinhMath,
                                     "arccosh" : acoshMath,
                                     "arctanh" : atanhMath,
                                     "sec" : lambda entity: 1 / cosMath(entity),
                                     "csc" : lambda entity: 1 / sinMath(entity),
                                     "cot" : lambda entity: 1 / tanMath(entity),
                                     "sech" : lambda entity: 1 / coshMath(entity),
                                     "csch" : lambda entity: 1 / sinhMath(entity),
                                     "coth" : lambda entity: 1 / tanhMath(entity),
                                     "arcsec" : lambda entity: 1 / acosMath(entity),
                                     "arccsc" : lambda entity: 1 / asinMath(entity),
                                     "arccot" : lambda entity: 1 / atanMath(entity),
                                     "arcsech" : lambda entity: 1 / acoshMath(entity),
                                     "arccsch" : lambda entity: 1 / asinhMath(entity),
                                     "arccoth" : lambda entity: 1 / atanhMath(entity),
                                     "bit_and" : lambda int1, int2: int1 & int2,
                                     "bit_or" : lambda int1, int2: int1 | int2,
                                     "bit_not" : lambda integer: ~integer,
                                     "bit_xor" : lambda int1, int2: int1 ^ int2,
                                     "factorial" : factorial,
                                     "choose" : lambda value1, value2: factorial(value1) / (factorial(value2) * factorial(value1 - value2)),
                                     "choose_repeat" : lambda value1, value2: self.__universalFuncs["choose"](value1 + value2 - 1, value2),
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
        else:
            raise Exception("This is a singleton class")

    @staticmethod
    def instance() -> _FunctionDictionary:
        if _FunctionDictionary.__instance is None:
            return _FunctionDictionary()
        else:
            return _FunctionDictionary.__instance

    def getUniversalFunc(self, funcName: str) -> Optional[function]:
        return self.__universalFuncs.get(funcName)

    def getPermFunc(self, funcName: str) -> Optional[function]:
        return self.__permFuncs.get(funcName)

    def getTempFunc(self, funcName: str) -> Optional[function]:
        return self.__tempFuncs.get(funcName)

    def __getitem__(self, funcName: str) -> Optional[function]:
        # Search "UniversalFunc" dictionary
        universalFunc = self.getUniversalFunc(funcName)
        if universalFunc is not None:
            return universalFunc

        # Search "TempFunc" dictionary
        tempFunc = self.getTempFunc(funcName)
        if tempFunc is not None:
            return tempFunc

        # Search "PermFunc" dictionary
        permFunc = self.getPermFunc(funcName)
        if permFunc is not None:
            return permFunc

        return None

    def hasUniversalFunc(self, funcName: str) -> bool:
        return funcName in self.__universalFuncs

    def hasPermFunc(self, funcName: str) -> bool:
        return funcName in self.__permFuncs

    def hasTempFunc(self, funcName: str) -> bool:
        return funcName in self.__tempFuncs

    def __contains__(self, funcName: str) -> bool:
        return self.hasUniversalFunc(funcName) or self.hasPermFunc(funcName) or self.hasTempFunc(funcName)

    def iterUniversalFuncs(self) -> Iterable[Tuple[str, function]]:
        return iter(self.__universalFuncs.items())

    def iterPermFuncs(self) -> Iterable[Tuple[str, function]]:
        return iter(self.__permFuncs.items())

    def iterTempFuncs(self) -> Iterable[Tuple[str, function]]:
        return iter(self.__tempFuncs.items())

    def __iter__(self) -> Iterable[Tuple[str, function]]:
        return chain(self.__universalFuncs)

    def __eq__(self, other: _FunctionDictionary) -> bool:
        return self is other

    def __ne__(self, other: _FunctionDictionary) -> bool:
        return self is not other
