import math
from cmath import log as logOfComplex
from calc.Complex import Complex
from calc.Quaternion import Quaternion


E = math.e
PI = math.pi
POSITIVE_INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf
NOT_A_NUMBER = math.nan


def pow(leftOperand, rightOperand):
    """
    Computes the result of taking the left
    parameter to the power of the right parameter

    :param leftOperand: The operand that is the
        base of this operation
    :param rightOperand: The operand that is the
        exponent of this operation
    :return: The result of taking the left parameter
        to the power of the right parameter
    """

    return leftOperand ** rightOperand


def exp(operand):
    """
    Computes the value of (e ** operand)

    :param operand: The value that e will be
        taken to the power of
    :return: The result of taking e to the power
        of the given operand
    """

    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return E ** operand
    elif typeOfOperand is Complex:
        return _expComplex(operand)
    elif typeOfOperand is Quaternion:
        return _expQuaternion(operand)


def _expComplex(complex):
    """
    Computes the exponential function of the
    given complex number

    :param complex: The complex number which
        will have the exponential function
        applied to it
    :return: The result of applying the exponential
        function to the given complex number
    """

    return (E ** complex.real) * (math.cos(complex.imag0) + Complex(0, 1) * math.cos(complex.imag0))


def _expQuaternion(quaternion):
    """
    Computes the exponential function of the
    given quaternion

    :param quaternion: The quaternion which
        will have the exponential function
        applied to it
    :return: The result of applying the exponential
        function to the given quaternion
    """

    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)
    magnitudeOfVectorPart = abs(vectorPart)

    return (E ** quaternion.real) * (math.cos(magnitudeOfVectorPart) + vectorPart.normalize() * math.sin(magnitudeOfVectorPart))


def sqrt(operand):
    """
    Computes the square root of the given operand

    :param operand: The value whose square root
        will be calculated
    :return: The square root of the operand
    """

    return operand ** 0.5


def cbrt(operand):
    """
    Computes the cube root of the given operand

    :param operand: The value whose cube root
        will be calculated
    :return: The cube root of the operand
    """

    return operand ** 0.3333333333333333


def log(operand, base=E):
    """
    Computes the logarithm of the given operand
    to the given base

    :param operand: The operand that the log function
        is being applied to
    :param base: The base of the log function. By default,
        this value is e
    :return: The result of applying the log function with
        the given base to the given operand
    """

    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.log(operand, base)
    elif typeOfOperand is Complex:
        return _logComplex(operand, base)
    elif typeOfOperand is Quaternion:
        return _logQuaternion(operand, base)


def _logComplex(complex, base):
    """
    Computes the logarithm of a complex number
    with the given base

    :param complex: The complex number that the
        log function will be applied to
    :param base: The base of the log function
    :return: The result of applying the log function
        with the given base to the given complex
        number
    """

    com = Complex.toBuiltInComplex(complex)
    result = logOfComplex(com, base)

    return Complex.fromBuiltInComplex(result)


def _logQuaternion(quaternion, base):
    """
    Computes the logarithm of the given quaternion
    with the given base

    :param quaternion: The quaternion that the log
        function will be applied to
    :param base: The base of the log function
    :return: The result of applying the log function
        with the given base to the given quaternion
    """

    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)

    return log(abs(quaternion), base) * (vectorPart / abs(vectorPart)) * acos(quaternion.real / abs(quaternion))


def log10(operand):
    """
    Computes the logarithm of the given value
    with a base of ten

    :param operand: The value that the log
        function will be applied to
    :return: The result of applying the log function
        with a base of ten to the given operand
    """

    return log(operand, 10)


def sin(operand):
    """
    Computes the result of applying the sine
    function to the given operand

    :param operand: The value that will have
        the sine function applied to it
    :return: The result of applying the sine
        function to the given operand
    """

    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.sin(operand)
    elif typeOfOperand is Complex:
        return _sinComplex(operand)


def _sinComplex(complex):
    """
    Computes the result of applying the sine
    function to a complex number

    :param complex: The complex number to have
        the sine function to it
    :return: The result of applying the sine
        function to the given complex number
    """

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

    return -imag * _logComplex(imag * complex + sqrt(1 - (complex ** 2)), E)


def acos(operand):
    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return math.acos(operand)
    elif typeOfOperand is Complex:
        return _acosComplex(operand)


def _acosComplex(complex):
    imag = Complex(0, 1)

    return -imag * _logComplex(complex + sqrt((complex ** 2) - 1), E)


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
