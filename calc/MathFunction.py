import math
from calc.ComplexFunction import *
from calc.QuaternionFunction import *
from calc.MatrixFunction import *


E = math.e
PI = math.pi
IMAG_0 = Complex(0, 1)
IMAG_1 = Quaternion(0, 0, 1, 0)
IMAG_2 = Quaternion(0, 0, 0, 1)
POSITIVE_INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf
NOT_A_NUMBER = math.nan


def signum(mathEntity):
    pass


def sqrt(mathEntity):
    pass


def exp(mathEntity):
    pass


def log(mathEntity, base=E):
    pass


def log10(mathEntity):
    pass


def sin(mathEntity):
    pass


def cos(mathEntity):
    pass


def tan(mathEntity):
    pass


def sinh(mathEntity):
    pass


def cosh(mathEntity):
    pass


def tanh(mathEntity):
    pass


def asin(mathEntity):
    pass


def acos(mathEntity):
    pass


def atan(mathEntity):
    pass


def asinh(mathEntity):
    pass


def acosh(mathEntity):
    pass


def atanh(mathEntity):
    pass


def sec(mathEntity):
    return 1 / cos(mathEntity)


def csc(mathEntity):
    return 1 / sin(mathEntity)


def cot(mathEntity):
    return 1 / tan(mathEntity)


def sech(mathEntity):
    return 1 / cosh(mathEntity)


def csch(mathEntity):
    return 1 / sinh(mathEntity)


def coth(mathEntity):
    return 1 / tanh(mathEntity)


def asec(mathEntity):
    return 1 / acos(mathEntity)


def acsc(mathEntity):
    return 1 / asin(mathEntity)


def acot(mathEntity):
    return 1 / atan(mathEntity)


def asech(mathEntity):
    return 1 / acosh(mathEntity)


def acsch(mathEntity):
    return 1 / asinh(mathEntity)


def acoth(mathEntity):
    return 1 / atanh(mathEntity)


def ceil(mathEntity):
    return math.ceil(mathEntity)


def floor(mathEntity):
    return math.floor(mathEntity)
