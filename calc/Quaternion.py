from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from calc.Exponentable import Exponentable
from math import sqrt, floor, ceil


class Quaternion(MathEntity, Negatable, Exponentable):
    def __init__(self, real, imag0, imag1, imag2):
        self.__real = real
        self.__imag0 = imag0
        self.__imag1 = imag1
        self.__imag2 = imag2

    @property
    def real(self):
        return self.__real

    @property
    def imag0(self):
        return self.__imag0

    @property
    def imag1(self):
        return self.__imag1

    @property
    def imag2(self):
        return self.__imag2

    def __abs__(self):
        return sqrt((self.real ** 2) + (self.imag0 ** 2) + (self.imag1 ** 2) + (self.imag2 ** 2))

    def conjugate(self):
        return Quaternion(self.real, -self.imag0, -self.imag1, -self.imag2)

    def __floor__(self):
        real = floor(self.real)
        imag0 = floor(self.imag0)
        imag1 = floor(self.imag1)
        imag2 = floor(self.imag2)

        return Quaternion(real, imag0, imag1, imag2)

    def __ceil__(self):
        real = ceil(self.real)
        imag0 = ceil(self.imag0)
        imag1 = ceil(self.imag1)
        imag2 = ceil(self.imag2)

        return Quaternion(real, imag0, imag1, imag2)

    def __round__(self, numDecimals=None):
        real = round(self.real, numDecimals)
        imag0 = round(self.imag0, numDecimals)
        imag1 = round(self.imag1, numDecimals)
        imag2 = round(self.imag2, numDecimals)

        return Quaternion(real, imag0, imag1, imag2)

    def __hash__(self):
        modifier = 31

        return modifier * hash(self.real) + \
               modifier * hash(self.imag0) + \
               modifier * hash(self.imag1) + \
               modifier * hash(self.imag2)

    def __str__(self):
        strRep = Quaternion.__symbol(self.real, "") + \
                 Quaternion.__symbol(self.imag0, "i") + \
                 Quaternion.__symbol(self.imag1, "j") + \
                 Quaternion.__symbol(self.imag2, "k")

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
