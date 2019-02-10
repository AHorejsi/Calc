from __future__ import annotations
from typing import Union, Iterable
from calc.MathEntity import MathEntity
from math import sqrt


class Complex(MathEntity):
    """
    Instances of this class represent complex numbers
    """

    def __init__(self, real: Union[int, float], imag0: Union[int, float]):
        """
        Constructs a complex number with the given real
        and imaginary components

        :param real: The real component of this complex number
        :param imag0: The imaginary component of this complex number
        """
        self.__real = real
        self.__imag0 = imag0

    @property
    def real(self) -> Union[int, float]:
        """
        Returns the real component of this complex number

        :return: The real component of this complex number
        """

        return self.__real

    @property
    def imag0(self) -> Union[int, float]:
        """
        Returns the imaginary component of this complex number

        :return: The imaginary component of this complex number
        """

        return self.__imag0

    def __abs__(self) -> float:
        """
        Computes the absolute value of this complex number

        :return: The absolute value of this complex number
        """

        return sqrt((self.real ** 2) + (self.imag0 ** 2))

    def conjugate(self) -> Complex:
        """
        Returns the conjugate of this complex number

        :return: The conjugate of this complex number
        """

        return Complex(self.real, -self.imag0)

    def normalize(self) -> Complex:
        """
        Returns the normalized value of this complex number

        :return: The normalized value of this complex number
        """

        return self / abs(self)

    @staticmethod
    def fromBuiltInComplex(builtInComplex: complex) -> Complex:
        """
        Converts a variable of type complex to a variable
        of type Complex

        :param builtInComplex: The variable of type complex
            to be converted
        :return: A variable of type Complex that is mathematically
            equal to the input
        """

        return Complex(builtInComplex.real, builtInComplex.imag)

    @staticmethod
    def toBuiltInComplex(customComplex: Complex) -> complex:
        """
        Converts a variable of type Complex to a variable
        of type complex

        :param customComplex: The variable of type Complex
            to be converted
        :return: A variable of type complex that is mathematically
            equal to the input
        """

        return complex(customComplex.real, customComplex.imag0)

    def __complex__(self) -> complex:
        """
        Converts a variable of type Complex to a variable
        of type complex

        :return: A variable of type complex that is mathematically
            equal to the input
        """

        return Complex.toBuiltInComplex(self)

    def __iter__(self) -> Iterable[Union[int, float]]:
        """
        Returns an iterator over the real and imaginary components
        of this complex number

        :return: An iterator over the real and imaginary components
            of this complex number
        """

        return iter([self.real, self.imag0])

    def __hash__(self) -> int:
        """
        Computes a hash code for this complex number

        :return: A hash code for this complex number
        """

        MODIFIER = 31

        return MODIFIER * hash(self.real) + MODIFIER * hash(self.imag0)

    def __str__(self) -> str:
        """
        Returns a string representation of this complex number

        :return: A string representation of this complex number
        """

        strRep = Complex.__symbol(self.real, "") + Complex.__symbol(self.imag0, "i")

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
        of this complex number

        :param value: The value of the component to be represented
        :param axis: The axis of the component to be represented
        :return: A string representation of a given component
            of this complex number
        """

        if value == 0:
            return "+0" + axis
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
