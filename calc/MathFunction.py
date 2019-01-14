import math
import cmath
from calc.Complex import Complex


E = math.e
PI = math.pi


def pow(leftOperand, rightOperand):
    return leftOperand ** rightOperand


def exp(operand):
    return E ** operand


def sqrt(operand):
    return operand ** 0.5


def log(operand, base=E):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.log(operand, base)
    elif typeOfOperand is Complex:
        return _logComplex(operand, base)


def log10(operand):
    return log(operand, 10)


def _logComplex(complex, base):
    com = Complex.toBuiltInComplex(complex)
    result = cmath.log(com, base)

    return Complex.fromBuiltInComplex(result)


def sin(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.sin(operand)
    elif typeOfOperand is Complex:
        return _sinComplex(operand)


def _sinComplex(complex):
    return Complex(math.sin(complex.real) * math.cosh(complex.imag0), math.cos(complex.real) * math.sinh(complex.imag0))


def cos(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.cos(operand)
    elif typeOfOperand is Complex:
        return _cosComplex(operand)


def _cosComplex(complex):
    return Complex(math.cos(complex.real) * math.cosh(complex.imag0), -math.sin(complex.real) * math.sinh(complex.imag0))


def tan(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.tan(operand)
    elif typeOfOperand is Complex:
        return _tanComplex(operand)


def _tanComplex(complex):
    return Complex(math.tan(complex.real),
                   math.tanh(complex.imag0)) / Complex(1, -math.tan(complex.real) * math.tanh(complex.imag0))


def asin(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.asin(operand)
    elif typeOfOperand is Complex:
        return _asinComplex(operand)


def _asinComplex(complex):
    imag = Complex(0, 1)

    return -imag * _logComplex(imag * complex + _sqrtComplex(1 - (complex ** 2)), E)


def acos(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.acos(operand)
    elif typeOfOperand is Complex:
        return _acosComplex(operand)


def _acosComplex(complex):
    imag = Complex(0, 1)

    return -imag * _logComplex(complex + _sqrtComplex((complex ** 2) - 1), E)


def atan(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.atan(operand)
    elif typeOfOperand is Complex:
        return _atanComplex(operand)


def _atanComplex(complex):
    imag = Complex(0, 1)

    return (1 / Complex(0, 2)) * _logComplex((1 + imag * complex) / (1 - imag * complex), E)


def sinh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.sinh(operand)
    elif typeOfOperand is Complex:
        return _sinhComplex(operand)


def _sinhComplex(complex):
    return Complex(math.sinh(complex.real) * math.cos(complex.imag0), math.cosh(complex.real) * math.sin(complex.imag0))


def cosh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.cosh(operand)
    elif typeOfOperand is Complex:
        return _coshComplex(operand)


def _coshComplex(complex):
    return Complex(math.cosh(complex.real) * math.cos(complex.imag0), math.sinh(complex.real) * math.sin(complex.imag0))


def tanh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.tanh(operand)
    elif typeOfOperand is Complex:
        return _tanhComplex(operand)


def _tanhComplex(complex):
    return Complex(math.tanh(complex.real), math.tan(complex.imag0)) / Complex(1, math.tanh(complex.real) * math.tan(complex.imag0))


def asinh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.asinh(operand)
    elif typeOfOperand is Complex:
        return _asinhComplex(operand)


def _asinhComplex(complex):
    return _logComplex(complex + sqrt(1 + (complex ** 2)), E)


def acosh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.acosh(operand)
    elif typeOfOperand is Complex:
        return _acoshComplex(operand)


def _acoshComplex(complex):
    return _logComplex(complex + sqrt(complex + 1) * sqrt(complex - 1), E)


def atanh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.atanh(operand)
    elif typeOfOperand is Complex:
        return _atanhComplex(operand)


def _atanhComplex(complex):
    return (log(1 + complex) - log(1 - complex)) / 2


def sec(operand):
    return 1 / cos(operand)


def csc(operand):
    return 1 / sin(operand)


def cot(operand):
    return 1 / tan(operand)


def asec(operand):
    return 1 / acos(operand)


def acsc(operand):
    return 1 / asin(operand)


def acot(operand):
    return 1 / atan(operand)


def sech(operand):
    return 1 / cosh(operand)


def csch(operand):
    return 1 / sinh(operand)


def coth(operand):
    return 1 / tanh(operand)


def asech(operand):
    return 1 / acosh(operand)


def acsch(operand):
    return 1 / asinh(operand)


def acoth(operand):
    return 1 / atanh(operand)


def ceil(operand):
    return math.ceil(operand)


def floor(operand):
    return math.floor(operand)
