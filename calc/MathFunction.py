import math
from calc.Complex import Complex


def pow(leftOperand, rightOperand):
    return leftOperand ** rightOperand


def sqrt(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.sqrt(operand)
    elif typeOfOperand is Complex:
        return _sqrtComplex(operand)


def _sqrtComplex(complex):
    sign = None

    if complex.imag0 < 0:
        sign = -1
    elif complex.imag0 > 0:
        sign = 1
    else:
        sign = 0

    return 0.5 * math.sqrt(2) * Complex(math.sqrt(abs(complex) + complex.real),
                                        sign * math.sqrt(abs(complex) - complex.real))


def log(operand, base=math.e):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.log(operand, base)
    elif typeOfOperand is Complex:
        return _logComplex(operand, base)


def _logComplex(complex, base):
    return Complex(math.log(abs(complex), base), math.atan(complex.imag0 / complex.real))


def log2(operand):
    return log(operand, 2)


def log10(operand):
    return log(operand, 10)


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
    return Complex(math.tan(complex.real), math.tanh(complex.imag0)) / Complex(1, -math.tan(complex.real) * math.tanh(complex.imag0))


def asin(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.asin(operand)
    elif typeOfOperand is Complex:
        pass


def acos(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.acos(operand)
    elif typeOfOperand is Complex:
        pass


def atan(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.atan(operand)
    elif typeOfOperand is Complex:
        pass


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
        pass


def asinh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.asinh(operand)
    elif typeOfOperand is Complex:
        pass


def acosh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.acosh(operand)
    elif typeOfOperand is Complex:
        pass


def atanh(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.atanh(operand)
    elif typeOfOperand is Complex:
        pass


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
