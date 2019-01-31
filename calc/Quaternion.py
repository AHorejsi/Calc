from calc.MathEntity import MathEntity
from math import sqrt, floor, ceil


class Quaternion(MathEntity):
    """
    Instances of this class represent quaternions
    """

    def __init__(self, real, imag0, imag1, imag2):
        """
        Constructs a quaternion with the given real and
        imaginary components

        :param real: The real component for this quaternion
        :param imag0: The first imaginary component for this
            quaternion
        :param imag1: The second imaginary component for this
            quaternion
        :param imag2: The third imaginary component for this
            quaternion
        """

        self.__real = real
        self.__imag0 = imag0
        self.__imag1 = imag1
        self.__imag2 = imag2

    @property
    def real(self):
        """
        Returns the real component of this quaternion

        :return: The real component of this quaternion
        """

        return self.__real

    @property
    def imag0(self):
        """
        Returns the first imaginary component of
        this quaternion

        :return: The first imaginary component of
            this quaternion
        """

        return self.__imag0

    @property
    def imag1(self):
        """
        Returns the second imaginary component of
        this quaternion

        :return: The second imaginary component of
            this quaternion
        """

        return self.__imag1

    @property
    def imag2(self):
        """
        Returns the third imaginary component of
        this quaternion

        :return: The third imaginary component of
            this quaternion
        """

        return self.__imag2

    def __abs__(self):
        """
        Returns the absolute value of this quaternion

        :return: The absolute value of this quaternion
        """

        return sqrt((self.real ** 2) + (self.imag0 ** 2) + (self.imag1 ** 2) + (self.imag2 ** 2))

    def conjugate(self):
        """
        Returns the conjugate of this quaternion

        :return: The conjugate of this quaternion
        """

        return Quaternion(self.real, -self.imag0, -self.imag1, -self.imag2)

    def normalize(self):
        """
        Returns the normalized value of this quaternion

        :return: The normalized value of this quaternion
        """

        return self / abs(self)

    def __floor__(self):
        """
        Rounds the real and imaginary components of quaternion
        down

        :return: A new quaternion with the values of this quaternion
            rounded down
        """

        real = floor(self.real)
        imag0 = floor(self.imag0)
        imag1 = floor(self.imag1)
        imag2 = floor(self.imag2)

        return Quaternion(real, imag0, imag1, imag2)

    def __ceil__(self):
        """
        Rounds the real and imaginary components of quaternion
        up

        :return: A new quaternion with the values of this quaternion
            rounded up
        """

        real = ceil(self.real)
        imag0 = ceil(self.imag0)
        imag1 = ceil(self.imag1)
        imag2 = ceil(self.imag2)

        return Quaternion(real, imag0, imag1, imag2)

    def __round__(self, numDecimals=None):
        """
        Rounds the real and imaginary components of quaternion
        to the given number of decimal places

        :param numDecimals: The number of decimals that the components of this
            quaternion should be rounded to
        :return: A new quaternion with the values of this quaternion
            rounded up
        """

        real = round(self.real, numDecimals)
        imag0 = round(self.imag0, numDecimals)
        imag1 = round(self.imag1, numDecimals)
        imag2 = round(self.imag2, numDecimals)

        return Quaternion(real, imag0, imag1, imag2)

    def __iter__(self):
        """
        Returns an iterator over the components of this quaternion

        :return: An iterator over the components of this quaternion
        """

        return iter([self.real, self.imag0, self.imag1, self.imag2])

    def __hash__(self):
        """
        Returns a hash code for this quaternion

        :return: A hash code for this quaternion
        """

        MODIFIER = 31

        return MODIFIER * hash(self.real) + \
               MODIFIER * hash(self.imag0) + \
               MODIFIER * hash(self.imag1) + \
               MODIFIER * hash(self.imag2)

    def __str__(self):
        """
        Returns a string representation of this quaternion

        :return: A string representation of this quaternion
        """

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
        """
        Computes the string representation of a given component
        of this quaternion

        :param value: The value of the component to be represented
        :param axis: The axis of the component to be represented
        :return: A string representation of a given component
            of this quaternion
        """

        if value == 0:
            return "+0" + axis
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
