from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from calc.Exponentable import Exponentable
from math import sqrt, floor, ceil, sin, cos, log


class Complex(MathEntity, Negatable, Exponentable):
    def __init__(self, real, imag0):
        self.__real = real
        self.__imag0 = imag0

    @property
    def real(self):
        return self.__real

    @property
    def imag0(self):
        return self.__imag0

    def __add__(self, mathEntity):
        from calc._ComplexMediator import _addition

        return _addition(self, mathEntity)

    def __radd__(self, real):
        return self + real

    def __sub__(self, mathEntity):
        from calc._ComplexMediator import _subtraction

        return _subtraction(self, mathEntity)

    def __rsub__(self, real):
        return Complex(real - self.real, -self.imag0)

    def __mul__(self, mathEntity):
        from calc._ComplexMediator import _multiplication

        return _multiplication(self, mathEntity)

    def __rmul__(self, real):
        return self * real

    def __truediv__(self, mathEntity):
        from calc._ComplexMediator import _division

        return _division(self, mathEntity)

    def __rtruediv__(self, real):
        conj = self.conjugate()
        numerator = real * conj
        denominator = (self * conj).real

        return Complex(numerator.real / denominator, numerator.imag0 / denominator)

    def __pow__(self, mathEntity, modulo=None):
        from calc._ComplexMediator import _exponent

        return _exponent(self, mathEntity)

    def __rpow__(self, real):
        value1 = (real ** 2) ** (self.real / 2)
        value2 = cos(log(real))
        value3 = sin(log(real))

        return Complex(value1 * value2, value1 * value3)

    def __abs__(self):
        return sqrt((self.real ** 2) + (self.imag0 ** 2))

    def conjugate(self):
        return Complex(self.real, -self.imag0)

    def __floor__(self):
        real = floor(self.real)
        imag0 = floor(self.imag0)

        return Complex(real, imag0)

    def __ceil__(self):
        real = ceil(self.real)
        imag0 = ceil(self.imag0)

        return Complex(real, imag0)

    def __round__(self, numDecimals=None):
        real = round(self.real, numDecimals)
        imag0 = round(self.imag0, numDecimals)

        return Complex(real, imag0)

    @staticmethod
    def fromBuiltInComplex(builtInComplex):
        return Complex(builtInComplex.real, builtInComplex.imag)

    @staticmethod
    def toBuiltInComplex(customComplex):
        return complex(customComplex.real, customComplex.imag0)

    def __iter__(self):
        return iter([self.real, self.imag0])

    def __hash__(self):
        modifier = 31
        hashCode = 0

        hashCode += modifier * hash(self.real)
        hashCode += modifier * hash(self.imag0)

        return hashCode

    def __eq__(self, mathEntity):
        from calc._ComplexMediator import _equality

        return _equality(self, mathEntity)

    def __str__(self):
        strRep = Complex.__symbol(self.real, "") + Complex.__symbol(self.imag0, "i")

        if strRep.startswith("+"):
            return strRep[1:]
        elif len(strRep) == 0:
            return "0"
        else:
            return strRep

    @staticmethod
    def __symbol(value, axis):
        if value == 0:
            return ""
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
