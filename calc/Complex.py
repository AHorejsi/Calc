from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from calc.Exponentable import Exponentable
from math import sqrt, floor, ceil


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

    def __str__(self):
        strRep = Complex.__symbol(self.real, "") + \
                 Complex.__symbol(self.imag0, "i")

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

    def __repr__(self):
        return str(self)
