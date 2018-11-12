from math import sqrt
from cal.MathEntity import MathEntity


class Quaternion(MathEntity):
    def __init__(self, real, imag, imag1, imag2):
        self.__values = [real, imag, imag1, imag2]

    @property
    def real(self):
        return self.__values[0]

    @property
    def imag(self):
        return self.__values[1]

    @property
    def imag1(self):
        return self.__values[2]

    @property
    def imag2(self):
        return self.__values[3]

    def __abs__(self):
        return sqrt((self.real ** 2) + (self.imag ** 2) + (self.imag1 ** 2) + (self.imag2 ** 2))

    def conjugate(self):
        return Quaternion(self.real, -self.imag, -self.imag1, -self.imag2)

    def inverse(self):
        return self.conjugate() / (abs(self) ** 2)

    def __hash__(self):
        modifier = 31

        return modifier * hash(self.real) + \
               modifier * hash(self.imag) + \
               modifier * hash(self.imag1) + \
               modifier * hash(self.imag2)

    def __str__(self):
        strRep = Quaternion.__value(self.real, "") + \
                 Quaternion.__value(self.imag, "i") + \
                 Quaternion.__value(self.imag1, "j") + \
                 Quaternion.__value(self.imag2, "k")

        if strRep.startswith("+"):
            return strRep[1:]
        else:
            return strRep

    @staticmethod
    def __value(value, axis):
        if value == 0:
            return ""
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
