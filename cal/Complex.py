from cal.MathEntity import MathEntity
from math import sqrt


class Complex(MathEntity):
    def __init__(self, real, imag):
        self.__values = [real, imag]

    @property
    def real(self):
        return self.__values[0]

    @property
    def imag(self):
        return self.__values[1]

    def __abs__(self):
        return sqrt((self.real ** 2) + (self.imag ** 2))

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __iter__(self):
        return self.__values.__iter__()

    def __hash__(self):
        modifier = 31

        hashCode = 0
        hashCode *= modifier * self.real
        hashCode *= modifier * self.imag

    def __str__(self):
        strRep = Complex.__symbol(self.real, "") + \
                 Complex.__symbol(self.imag, "i")

        if strRep.startswith("+"):
            return strRep[1:]
        elif len(strRep) == 0:
            return "0"
        else:
            return strRep

    @staticmethod
    def __symbol(value, axis):
        """
        Returns part of the string representation of a given
        component of this Complex

        :param value: The value of this Complex that is to be
            added to the string
        :param axis: The axis of the given value
        :return: A string representation of the current Complex
            component
        """

        if value == 0:
            return ""
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
