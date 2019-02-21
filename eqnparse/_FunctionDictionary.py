from __future__ import annotations
from typing import Optional, Iterable, Tuple
from math import factorial, ceil, floor, gcd
from random import randrange, random
from calc import expMath, logMath, signumMath, sqrtMath, sinMath, cosMath, tanMath, sinhMath, coshMath, \
                 tanhMath, asinMath, acosMath, atanMath, asinhMath, acoshMath, atanhMath, Quaternion, Vector


class _FunctionDictionary:
    __instance = None

    def __init__(self):
        if _FunctionDictionary.__instance is None:
            _FunctionDictionary.__instance = self

            self.__universalFuncs = {"com" : lambda value1, value2: complex(value1, value2),
                                     "quat" : lambda value1, value2, value3, value4: Quaternion(value1, value2, value3, value4),
                                     "abs" : abs,
                                     "ceil" : ceil,
                                     "floor" : floor,
                                     "round" : round,
                                     "real" : lambda value: value if (type(value) is int) or (type(value) is float) else value.real,
                                     "imag0" : lambda value: 0 if (type(value) is int) or (type(value) is float) else value.imag if type(value) is complex else value.imag1,
                                     "imag1" : lambda value: 0 if type(value) is not Quaternion else value.imag1,
                                     "imag2" : lambda value: 0 if type(value) is not Quaternion else value.imag2,
                                     "dim" : lambda vector: len(vector),
                                     "rows" : lambda matrix: matrix.rowLength,
                                     "cols" : lambda matrix: matrix.columnLength,
                                     "xor" : lambda bool1, bool2: ((not bool1) and bool2) or (bool1 and (not bool2)),
                                     "max" : lambda real1, real2: real1 if real1 > real2 else real2,
                                     "min" : lambda real1, real2: real1 if real1 < real2 else real2,
                                     "mod" : lambda real1, real2: real1 % real2,
                                     "exp" : expMath,
                                     "ln" : lambda entity: logMath(entity),
                                     "log10" : lambda entity: logMath(entity) / logMath(10),
                                     "log2" : lambda entity: logMath(entity) / logMath(2),
                                     "log" : lambda entity, base: logMath(entity) / logMath(base),
                                     "sgn" : signumMath,
                                     "sqrt" : sqrtMath,
                                     "cbrt" : lambda entity: entity ** 0.33333333333333,
                                     "gcd" : gcd,
                                     "rand_int" : randrange,
                                     "rand" : random,
                                     "arg" : lambda complexVal: atanMath(complexVal.imag / complexVal.real),
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
                                     "permutation" : lambda value1, value2: factorial(value1) / factorial(value1 - value2),
                                     "dot" : lambda vec1, vec2: vec1.dot(vec2),
                                     "cross" : lambda vec1, vec2: vec1.cross(vec2),
                                     "magn" : lambda vec: vec.magnitude,
                                     "angle" : lambda vec1, vec2: vec1.angleBetween(vec2),
                                     "dist" : lambda vec1, vec2: vec1.distanceFrom(vec2),
                                     "det" : lambda matrix: matrix.determinant,
                                     "inv" : lambda matrix: matrix.inverse(),
                                     "transpose" : lambda matrix: matrix.transpose(),
                                     "norm" : lambda entity: entity.normalize(),
                                     "conj" : lambda entity: entity.conjugate()}
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

    def hasUniversalFunc(self, funcName: str) -> bool:
        return funcName in self.__universalFuncs

    def iterUniversalFuncs(self) -> Iterable[Tuple[str, function]]:
        return iter(self.__universalFuncs.items())

    def __eq__(self, other: _FunctionDictionary) -> bool:
        return self is other

    def __ne__(self, other: _FunctionDictionary) -> bool:
        return self is not other
