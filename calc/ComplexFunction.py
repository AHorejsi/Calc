import math
from typing import Union
from cmath import log as logOfComplex
from calc.Complex import Complex
from calc.MathConstant import IMAG_0


def signumComplex(complex: Complex) -> int:
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
    return (math.e ** complex.real) * (math.cos(complex.imag0) + IMAG_0 * math.cos(complex.imag0))


def logComplex(complex: Complex, base: Union[int, float]=math.e) -> Complex:
    com = Complex.toBuiltInComplex(complex)
    result = logOfComplex(com, base)

    return Complex.fromBuiltInComplex(result)


def log10Complex(complex: Complex) -> Complex:
    return logComplex(complex, 10)


def sqrtComplex(complex: Complex) -> Complex:
    return complex ** 0.5


def sinComplex(complex: Complex) -> Complex:
    return Complex(math.sin(complex.real) * math.cosh(complex.imag0), math.cos(complex.real) * math.sinh(complex.imag0))


def cosComplex(complex: Complex) -> Complex:
    return Complex(math.cos(complex.real) * math.cosh(complex.imag0),
                   -math.sin(complex.real) * math.sinh(complex.imag0))


def tanComplex(complex: Complex) -> Complex:
    return Complex(math.tan(complex.real),
                   math.tanh(complex.imag0)) / Complex(1, -math.tan(complex.real) * math.tanh(complex.imag0))


def asinComplex(complex: Complex) -> Complex:
    return -IMAG_0 * logComplex(IMAG_0 * complex + sqrtComplex(1 - (complex ** 2)))


def acosComplex(complex: Complex) -> Complex:
    return -IMAG_0 * logComplex(complex + sqrtComplex((complex ** 2) - 1))


def atanComplex(complex: Complex) -> Complex:
    return (1 / (2 * IMAG_0)) * logComplex((1 + IMAG_0 * complex) / (1 - IMAG_0 * complex))


def sinhComplex(complex: Complex) -> Complex:
    return Complex(math.sinh(complex.real) * math.cos(complex.imag0), math.cosh(complex.real) * math.sin(complex.imag0))


def coshComplex(complex: Complex) -> Complex:
    return Complex(math.cosh(complex.real) * math.cos(complex.imag0), math.sinh(complex.real) * math.sin(complex.imag0))


def tanhComplex(complex: Complex) -> Complex:
    return Complex(math.tanh(complex.real), math.tan(complex.imag0)) / Complex(1, math.tanh(complex.real) * math.tan(complex.imag0))


def asinhComplex(complex: Complex) -> Complex:
    return logComplex(complex + sqrtComplex(1 + (complex ** 2)))


def acoshComplex(complex: Complex) -> Complex:
    return logComplex(complex + sqrtComplex(complex + 1) * sqrtComplex(complex - 1))


def atanhComplex(complex: Complex) -> Complex:
    return (logComplex(1 + complex) - logComplex(1 - complex)) / 2


def floorComplex(complex: Complex) -> Complex:
    return complex.__floor__()


def ceilComplex(complex: Complex) -> Complex:
    return complex.__ceil__()
