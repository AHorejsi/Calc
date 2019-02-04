from __future__ import annotations
from typing import Union, Iterable
from calc.MathEntity import MathEntity
from math import sqrt, floor, ceil


class Complex(MathEntity):
    """
    Instances of this class represent complex numbers
    """

    def __init__(self: Complex, real: Union[int, float], imag0: Union[int, float]):
        """
        Constructs a complex number with the given real
        and imaginary components

        :param real: The real component of this complex number
        :param imag0: The imaginary component of this complex number
        """
        self._real = real
        self._imag0 = imag0

    @property
    def real(self: Complex) -> Union[int, float]:
        """
        Returns the real component of this complex number

        :return: The real component of this complex number
        """

        return self._real

    @property
    def imag0(self: Complex) -> Union[int, float]:
        """
        Returns the imaginary component of this complex number

        :return: The imaginary component of this complex number
        """

        return self._imag0

    def __abs__(self: Complex) -> float:
        """
        Computes the absolute value of this complex number

        :return: The absolute value of this complex number
        """

        return sqrt((self.real ** 2) + (self.imag0 ** 2))

    def conjugate(self: Complex) -> Complex:
        """
        Returns the conjugate of this complex number

        :return: The conjugate of this complex number
        """

        return Complex(self.real, -self.imag0)

    def normalize(self: Complex) -> Complex:
        """
        Returns the normalized value of this complex number

        :return: The normalized value of this complex number
        """

        return self / abs(self)

    def __floor__(self: Complex) -> Complex:
        """
        Returns the result of rounding the real and
        imaginary components of this complex number
        down

        :return: The result of rounding the real and
            imaginary components of this complex number
            down
        """

        real = floor(self.real)
        imag0 = floor(self.imag0)

        return Complex(real, imag0)

    def __ceil__(self: Complex) -> Complex:
        """
        Returns the result of rounding the real and
        imaginary components of this complex number
        up

        :return: The result of rounding the real and
            imaginary components of this complex number
            up
        """

        real = ceil(self.real)
        imag0 = ceil(self.imag0)

        return Complex(real, imag0)

    def __round__(self: Complex, numDecimals: int=None):
        """
        Returns the result of rounding the real and
        imaginary components of this complex number
        to the given number of decimal places

        :param numDecimals: The number of decimal
            places the real and imaginary components
            will be rounded to
        :return: The result of rounding the real and
            imaginary components of this complex
            number to the given number of decimal
            places
        """

        real = round(self.real, numDecimals)
        imag0 = round(self.imag0, numDecimals)

        return Complex(real, imag0)

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

    def __complex__(self: Complex) -> complex:
        """
        Converts a variable of type Complex to a variable
        of type complex

        :return: A variable of type complex that is mathematically
            equal to the input
        """

        return Complex.toBuiltInComplex(self)

    def __iter__(self: Complex) -> Iterable[Union[int, float]]:
        """
        Returns an iterator over the real and imaginary components
        of this complex number

        :return: An iterator over the real and imaginary components
            of this complex number
        """

        return iter([self.real, self.imag0])

    def __hash__(self: Complex) -> int:
        """
        Computes a hash code for this complex number

        :return: A hash code for this complex number
        """

        MODIFIER = 31

        return MODIFIER * hash(self.real) + MODIFIER * hash(self.imag0)

    def __str__(self: Complex) -> str:
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
