from __future__ import annotations
from calc.MathEntity import MathEntity
from math import sqrt
from typing import Union, Iterator


class Quaternion(MathEntity):
    """
    Instances of this class represent quaternions
    """

    def __init__(self, real: Union[int, float], imag0: Union[int, float], imag1: Union[int, float], imag2: Union[int, float]):
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
    def real(self) -> Union[int, float]:
        """
        Returns the real component of this quaternion

        :return: The real component of this quaternion
        """

        return self.__real

    @property
    def imag0(self) -> Union[int, float]:
        """
        Returns the first imaginary component of
        this quaternion

        :return: The first imaginary component of
            this quaternion
        """

        return self.__imag0

    @property
    def imag1(self) -> Union[int, float]:
        """
        Returns the second imaginary component of
        this quaternion

        :return: The second imaginary component of
            this quaternion
        """

        return self.__imag1

    @property
    def imag2(self) -> Union[int, float]:
        """
        Returns the third imaginary component of
        this quaternion

        :return: The third imaginary component of
            this quaternion
        """

        return self.__imag2

    def __abs__(self) -> float:
        """
        Returns the absolute value of this quaternion

        :return: The absolute value of this quaternion
        """

        return sqrt((self.real ** 2) + (self.imag0 ** 2) + (self.imag1 ** 2) + (self.imag2 ** 2))

    def conjugate(self) -> Quaternion:
        """
        Returns the conjugate of this quaternion

        :return: The conjugate of this quaternion
        """

        return Quaternion(self.real, -self.imag0, -self.imag1, -self.imag2)

    def normalize(self) -> Quaternion:
        """
        Returns the normalized value of this quaternion

        :return: The normalized value of this quaternion
        """

        return self / abs(self)

    def __iter__(self) -> Iterator[Union[int, float]]:
        """
        Returns an iterator over the components of this quaternion

        :return: An iterator over the components of this quaternion
        """

        return iter([self.real, self.imag0, self.imag1, self.imag2])

    def __hash__(self) -> int:
        """
        Returns a hash code for this quaternion

        :return: A hash code for this quaternion
        """

        MODIFIER = 31

        return MODIFIER * hash(self.real) + \
               MODIFIER * hash(self.imag0) + \
               MODIFIER * hash(self.imag1) + \
               MODIFIER * hash(self.imag2)

    def __str__(self) -> str:
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
    def __symbol(value: Union[int, float], axis: str) -> str:
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
