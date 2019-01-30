import math
from math import log as logOfComplex
from calc.Complex import Complex


def signumComplex(complex):
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


def expComplex(complex):
    return (math.e ** complex.real) * (math.cos(complex.imag0) + Complex(0, 1) * math.cos(complex.imag0))


def logComplex(complex, base=math.e):
    com = Complex.toBuiltInComplex(complex)
    result = logOfComplex(com, base)

    return Complex.fromBuiltInComplex(result)


def log10Complex(complex):
    return logComplex(complex, 10)


def sqrtComplex(complex):
    return complex ** 0.5


def sinComplex(complex):
    return Complex(math.sin(complex.real) * math.cosh(complex.imag0), math.cos(complex.real) * math.sinh(complex.imag0))


def cosComplex(complex):
    return Complex(math.cos(complex.real) * math.cosh(complex.imag0),
                   -math.sin(complex.real) * math.sinh(complex.imag0))


def tanComplex(complex):
    return Complex(math.tan(complex.real),
                   math.tanh(complex.imag0)) / Complex(1, -math.tan(complex.real) * math.tanh(complex.imag0))


def asinComplex(complex):
    imag = Complex(0, 1)

    return -imag * logComplex(imag * complex + sqrtComplex(1 - (complex ** 2)))


def acosComplex(complex):
    imag = Complex(0, 1)

    return -imag * logComplex(complex + sqrtComplex((complex ** 2) - 1))


def atanComplex(complex):
    imag = Complex(0, 1)

    return (1 / Complex(0, 2)) * logComplex((1 + imag * complex) / (1 - imag * complex))


def sinhComplex(complex):
    return Complex(math.sinh(complex.real) * math.cos(complex.imag0), math.cosh(complex.real) * math.sin(complex.imag0))


def coshComplex(complex):
    return Complex(math.cosh(complex.real) * math.cos(complex.imag0), math.sinh(complex.real) * math.sin(complex.imag0))


def tanhComplex(complex):
    return Complex(math.tanh(complex.real), math.tan(complex.imag0)) / Complex(1, math.tanh(complex.real) * math.tan(complex.imag0))


def asinhComplex(complex):
    return logComplex(complex + sqrtComplex(1 + (complex ** 2)))


def acoshComplex(complex):
    return logComplex(complex + sqrtComplex(complex + 1) * sqrtComplex(complex - 1))


def atanhComplex(complex):
    return (logComplex(1 + complex) - logComplex(1 - complex)) / 2


def floorComplex(complex):
    return math.floor(complex)


def ceilComplex(complex):
    return math.ceil(complex)
