from math import sqrt


class Quaternion:
    def __init__(self, real, imag, imag1, imag2):
        self.real = real
        self.imag = imag
        self.imag1 = imag1
        self.imag2 = imag2

    def __abs__(self):
        return sqrt((self.real ** 2) + (self.imag ** 2) + (self.imag1 ** 2) + (self.imag2 ** 2))

    def conjugate(self):
        return Quaternion(self.real, -self.imag, -self.imag1, -self.imag2)
