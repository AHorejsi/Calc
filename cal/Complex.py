from cal.MathEntity import MathEntity
from math import sqrt


class Complex(MathEntity):
    """
    Instances of this class represent complex numbers
    """

    def __init__(self, real, imag):
        """
        Constructs the complex number with the given real and imaginary components

        :param real: A number representing the real component of this complex number
        :param imag: A number representing the imaginary component of this complex number
        """

        self.__real = real
        self.__imag = imag

    @property
    def real(self):
        """
        Returns the real component of this Complex

        :return: The real component of this Complex
        """

        return self.__real

    @property
    def imag(self):
        """
        Returns the imaginary component of this Complex

        :return: The imaginary component of this Complex
        """

        return self.__imag

    def __abs__(self):
        """
        Returns the absolute value (or modulus) of this Complex

        :return: The absolute value of this Complex
        """

        return sqrt((self.real ** 2) + (self.imag ** 2))

    def conjugate(self):
        """
        Returns the conjugate of this Complex

        :return: The conjugate of this Complex
        """

        return Complex(self.real, -self.imag)

    @staticmethod
    def fromBuiltInComplex(cmplx):
        """
        Creates a Complex from one of the Python built in "complex" type

        :param cmplx: a number of type "complex"
        :return: A Complex equal to the given "complex" value
        """

        return Complex(cmplx.real, cmplx.imag)

    def __iter__(self):
        """
        Returns iterator over the components of this Complex

        :return: An iterator over the components of this Complex
        """

        return [self.real, self.imag].__iter__()

    def __hash__(self):
        """
        Computes a hash code for this Complex

        :return: A hash code for this Complex
        """

        modifier = 31

        hashCode = 0
        hashCode *= modifier * self.real
        hashCode *= modifier * self.imag

        return hashCode

    def __str__(self):
        """
        Creates a string representation of this Complex

        :return: A string representation of this Complex
        """

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

    def __repr__(self):
        """
        Creates a string representation of this Complex

        :return: A string representation of this Complex
        """

        return self.__str__()
