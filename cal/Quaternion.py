from math import sqrt
from cal.MathEntity import MathEntity


class Quaternion(MathEntity):
    """
    Instances of this class represent Quaternions. This class was intentionally
    made to have the attributes "real" and "imag" just like the complex type.
    This was done because, conceptually, Quaternions are an extension of complex
    numbers. As a result, all Quaternions are complex numbers
    """

    def __init__(self, real, imag, imag1, imag2):
        """
        Constructs a Quaternion with the given values

        :param real: The real component of this Quaternion
        :param imag: The first imaginary component of this Quaternion
        :param imag1: The second imaginary component of this Quaternion
        :param imag2: The third imaginary component of this Quaternion
        """

        self.__real = real
        self.__imag = imag
        self.__imag1 = imag1
        self.__imag2 = imag2

    @property
    def real(self):
        """
        Returns the real component of this Quaternion

        :return: The real component of this Quaternion
        """

        return self.__real

    @property
    def imag(self):
        """
        Returns the first imaginary component of this Quaternion

        :return: The first imaginary component of this Quaternion
        """

        return self.__imag

    @property
    def imag1(self):
        """
        Returns the second imaginary component of this Quaternion

        :return: The second imaginary component of this Quaternion
        """

        return self.__imag1

    @property
    def imag2(self):
        """
        Returns the third imaginary component of this Quaternion

        :return: The third imaginary component of this Vector
        """

        return self.__imag2

    def __abs__(self):
        """
        Calculates the absolute value (or modulus) of this Quaternion

        :return: The absolute value of this Quaternion
        """

        return sqrt((self.real ** 2) + (self.imag ** 2) + (self.imag1 ** 2) + (self.imag2 ** 2))

    def conjugate(self):
        """
        Calculates the conjugate of this Quaternion

        :return: The conjugate of this Quaternion
        """

        return Quaternion(self.real, -self.imag, -self.imag1, -self.imag2)

    def __hash__(self):
        """
        Calculates a hash code for this Quaternion

        :return: A hash code for this Quaternion
        """

        modifier = 31

        return modifier * hash(self.real) + \
               modifier * hash(self.imag) + \
               modifier * hash(self.imag1) + \
               modifier * hash(self.imag2)

    def __iter__(self):
        """
        Returns an iterator over each component of this Quaternion

        :return: An iterator over each component of this Quaternion
        """

        return [self.real, self.imag, self.imag1, self.imag2].__iter__()

    def __str__(self):
        """
        Creates string representation of this Quaternion

        :return: A string representation of this Quaternion
        """

        strRep = Quaternion.__symbol(self.real, "") + \
                 Quaternion.__symbol(self.imag, "i") + \
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
        """
        Returns part of the string representation of a given
        component of this Quaternion

        :param value: The value of this Quaternion that is to be
            added to the string
        :param axis: The axis of the given value
        :return: A string representation of the current Quaternion
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
        Creates string representation of this Quaternion

        :return: A string representation of this Quaternion
        """

        return self.__str__()
