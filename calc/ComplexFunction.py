import math
from typing import Union
from cmath import log as logOfComplex
from calc.Complex import Complex
from calc.MathConstant import IMAG_0


def signumComplex(complex: Complex) -> int:
    """
    Computes the sign of this complex number

    :param complex: The complex number whose
        sign is to be computed
    :return: The sign of the given complex
        number
    """

    if complex.real > 0:
        return 1
    elif complex.real < 0:
        return -1
    else:
        if complex.imag0 > 0:
            return 1
        elif complex.imag0 < 0:
            return -1
        else:
            return 0


def expComplex(complex: Complex) -> Complex:
    """
    Computes the exponential of the given complex
    number

    :param complex: The complex number whose exponential
        will be computed
    :return: The exponential of the given complex number
    """

    return (math.e ** complex.real) * (math.cos(complex.imag0) + IMAG_0 * math.cos(complex.imag0))


def logComplex(complex: Complex, base: Union[int, float]=math.e) -> Complex:
    """
    Computes the logarithm of the complex number
    with the given base

    :param complex: The complex number that the
        logarithm function
    :param base: The base of the logarithm to
        be computed
    :return: The logarithm of the given complex
        number with the given base
    """

    com = Complex.toBuiltInComplex(complex)
    result = logOfComplex(com, base)

    return Complex.fromBuiltInComplex(result)


def log10Complex(complex: Complex) -> Complex:
    """
    Computes the logarithm of the complex number
    with a base of 10

    :param complex: The complex number that the
        logarithm function
    :return: The logarithm of the given complex
        number with a base of 10
    """

    return logComplex(complex, 10)


def sqrtComplex(complex: Complex) -> Complex:
    """
    Computes the square root of the given complex
    number

    :param complex: The complex number whose square
        root will be calculated
    :return: The square root of the given complex
        number
    """

    return complex ** 0.5


def sinComplex(complex: Complex) -> Complex:
    """
    Applies the sine function to the given complex
    number

    :param complex: The complex number which will
        have the sine function applied to it
    :return: The sine of the given complex number
    """

    return Complex(math.sin(complex.real) * math.cosh(complex.imag0), math.cos(complex.real) * math.sinh(complex.imag0))


def cosComplex(complex: Complex) -> Complex:
    """
    Applies the cosine function to the given complex
    number

    :param complex: The complex number which will
        have the cosine function applied to it
    :return: The cosine of the given complex
        number
    """

    return Complex(math.cos(complex.real) * math.cosh(complex.imag0),
                   -math.sin(complex.real) * math.sinh(complex.imag0))


def tanComplex(complex: Complex) -> Complex:
    """
    Applies the tangent function to the given complex
    number

    :param complex: The complex number which will
        have the tangent function applied to it
    :return: The tangent of the given complex
        number
    """

    return Complex(math.tan(complex.real),
                   math.tanh(complex.imag0)) / Complex(1, -math.tan(complex.real) * math.tanh(complex.imag0))


def asinComplex(complex: Complex) -> Complex:
    """
    Applies the arcsine function to the given
    complex number

    :param complex: The complex number which will
        have the arcsine function applied to it
    :return: The arcsine of the given complex
        number
    """

    return -IMAG_0 * logComplex(IMAG_0 * complex + sqrtComplex(1 - (complex ** 2)))


def acosComplex(complex: Complex) -> Complex:
    """
    Applies the arccosine function to the given
    complex number

    :param complex: The complex number which will
        have the arccosine function applied to it
    :return: The arccosine of the given complex
        number
    """

    return -IMAG_0 * logComplex(complex + sqrtComplex((complex ** 2) - 1))


def atanComplex(complex: Complex) -> Complex:
    """
    Applies the arctangent function to the given
    complex number

    :param complex: The complex number which will
        have the arctangent function applied to it
    :return: The arctangent of the given complex
        number
    """

    return (1 / (2 * IMAG_0)) * logComplex((1 + IMAG_0 * complex) / (1 - IMAG_0 * complex))


def sinhComplex(complex: Complex) -> Complex:
    """
    Applies the hyperbolic sine function to the
    given complex number

    :param complex: The complex number which will have
        the hyperbolic sine function applied to it
    :return: The hyperbolic sine of the given complex
        number
    """

    return Complex(math.sinh(complex.real) * math.cos(complex.imag0), math.cosh(complex.real) * math.sin(complex.imag0))


def coshComplex(complex: Complex) -> Complex:
    """
    Applies the hyperbolic cosine function to the
    given complex number

    :param complex: The complex number which will have
        the hyperbolic cosine function applied to it
    :return: The hyperbolic cosine of the given complex
        number
    """

    return Complex(math.cosh(complex.real) * math.cos(complex.imag0), math.sinh(complex.real) * math.sin(complex.imag0))


def tanhComplex(complex: Complex) -> Complex:
    """
    Applies the hyperbolic tangent function to the
    given complex number

    :param complex: The complex number which will have
        the hyperbolic tangent function applied to it
    :return: The hyperbolic tangent of the given complex
        number
    """

    return Complex(math.tanh(complex.real), math.tan(complex.imag0)) / Complex(1, math.tanh(complex.real) * math.tan(complex.imag0))


def asinhComplex(complex: Complex) -> Complex:
    """
    Applies the hyperbolic arcsine function to the
    given complex number

    :param complex: The complex number which will have
        the hyperbolic arcsine function applied to it
    :return: The hyperbolic arcsine of the given complex
        number
    """

    return logComplex(complex + sqrtComplex(1 + (complex ** 2)))


def acoshComplex(complex: Complex) -> Complex:
    """
    Applies the hyperbolic arccosine function to the
    given complex number

    :param complex: The complex number which will have
        the hyperbolic arccosine function applied to it
    :return: The hyperbolic arccosine of the given complex
        number
    """

    return logComplex(complex + sqrtComplex(complex + 1) * sqrtComplex(complex - 1))


def atanhComplex(complex: Complex) -> Complex:
    """
    Applies the hyperbolic arctangent function to the
    given complex number

    :param complex: The complex number which will have
        the hyperbolic arctangent function applied to it
    :return: The hyperbolic arctangent of the given complex
        number
    """

    return (logComplex(1 + complex) - logComplex(1 - complex)) / 2


def argComplex(complex: Complex) -> float:
    """
    Computes the complex argument of the given complex
    number

    :param complex: The complex number whose complex
        argument will be computed
    :return: The complex argument of the given complex
        number
    """

    return math.atan(complex.imag0 / complex.real)
