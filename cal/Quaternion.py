from math import sqrt
from cal.MathEntity import MathEntity


class Quaternion(MathEntity):
    def __init__(self, real, imag, imag1, imag2):
        self.real = real
        self.imag = imag
        self.imag1 = imag1
        self.imag2 = imag2

    def __abs__(self):
        return sqrt((self.real ** 2) + (self.imag ** 2) + (self.imag1 ** 2) + (self.imag2 ** 2))

    def conjugate(self):
        return Quaternion(self.real, -self.imag, -self.imag1, -self.imag2)

    def __hash__(self):
        modifier = 31

        return modifier * hash(self.real) + \
               modifier * hash(self.imag) + \
               modifier * hash(self.imag1) + \
               modifier * hash(self.imag2)

    def __str__(self):
        return Quaternion.__value(self.real, "") + \
               Quaternion.__value(self.imag, "i") + \
               Quaternion.__value(self.imag1, "j") + \
               Quaternion.__value(self.imag2, "k")

    @staticmethod
    def __value(value, axis):
        if value == 0:
            return ""
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
