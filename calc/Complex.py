from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from calc.Exponentable import Exponentable
from math import sqrt, floor, ceil, sin, cos, log


class Complex(MathEntity, Negatable, Exponentable):
    """
    Instances of this class represent complex numbers
    """

    def __init__(self, real, imag0):
        """
        Constructs a complex number with the given real
        and imaginary components

        :param real: The real component of this complex number
        :param imag0: The imaginary component of this complex number
        """
        self.__real = real
        self.__imag0 = imag0

    @property
    def real(self):
        """
        Returns the real component of this complex number

        :return: The real component of this complex number
        """

        return self.__real

    @property
    def imag0(self):
        """
        Returns the imaginary component of this complex number

        :return: The imaginary component of this complex number
        """

        return self.__imag0

    def __add__(self, mathEntity):
        """
        Adds this complex number to another mathematical entity with
        this complex number on the left side of the operator. Complex
        numbers can be added to real numbers, complex numbers and
        quaternions

        :param mathEntity: The mathematical entity on the right side
            of the operator
        :return: The sum of this complex number and the given mathematical
            entity
        """

        from calc._ComplexMediator import _addition

        return _addition(self, mathEntity)

    def __radd__(self, mathEntity):
        """
        Adds this complex number to another mathematical entity with
        the complex number on the right side of the operator. Complex
        numbers can be added to real numbers, complex numbers and
        quaternions. This method will only be called when the number on the
        left side of the operator is an int or a float

        :param mathEntity: The mathematical entity on the left side
            of the operator
        :return: The sum of the given mathematical entity and this
            complex number
        """

        return self + mathEntity

    def __sub__(self, mathEntity):
        """
        Subtracts a mathematical entity from this complex number with this
        complex number on the left side of the operator. Real number, complex
        numbers and quaternions can be subtracted from complex numbers

        :param mathEntity: The mathematical entity on the right side
            of the operator
        :return: The difference of this complex number and the given
            mathematical entity
        """

        from calc._ComplexMediator import _subtraction

        return _subtraction(self, mathEntity)

    def __rsub__(self, real):
        """
        Subtracts this complex number from the given mathematical entity
        with this complex number on the right side of the operator. Complex
        numbers can be subtracted from real number, complex numbers and
        quaternions. This method will only be called when the number on the
        left side of the operator is an int or a float

        :param real: The real number that is being subtracted by this complex
            number
        :return: The difference of the given real number and this complex
            number
        """

        return Complex(real - self.real, -self.imag0)

    def __mul__(self, mathEntity):
        """
        Multiplies this complex number by another mathematical entity with
        this complex number on the left side of the operator. Complex numbers
        can be multiplied by real number, complex numbers, quaternions and
        matrices

        :param mathEntity: The mathematical entity on the right side of
            the operator
        :return: The product of this complex number and the given
            mathematical entity
        """

        from calc._ComplexMediator import _multiplication

        return _multiplication(self, mathEntity)

    def __rmul__(self, mathEntity):
        """
        Multiplies this complex number with another mathematical entity
        with this complex number on the right side of the operator.
        Complex numbers can be multiplied to real numbers, complex numbers,
        quaternions and matrices

        :param mathEntity: The mathematical entity on the left side of
            the operator
        :return: The product of the given mathematical entity and this
            complex number
        """

        return self * mathEntity

    def __truediv__(self, mathEntity):
        """
        Divides this complex number by another mathematical entity with
        this complex number on the left side of the operator. Complex numbers
        can be divided real numbers, complex numbers and quaternions

        :param mathEntity: The mathematical entity on the left side of the
            operator
        :return: The quotient of this complex number and the given
            mathematical entity
        """

        from calc._ComplexMediator import _division

        return _division(self, mathEntity)

    def __rtruediv__(self, real):
        """
        Divides another mathematical entity by this complex number with
        this complex number on the right side of the operator. Complex numbers
        can be divided from real numbers, complex numbers, quaternions and
        matrices. This method will only be called when the mathematical entity
        on the left side of the operator is an int or a float

        :param real: The real number on the left side of the operator
        :return: The quotient of the given real number and this complex
            number
        """

        conj = self.conjugate()
        numerator = real * conj
        denominator = (self * conj).real

        return Complex(numerator.real / denominator, numerator.imag0 / denominator)

    def __pow__(self, mathEntity, modulo=None):
        """
        Takes this complex number to the power of the given mathematical
        entity with this complex number on the left side of the operator.
        Complex numbers can be taken to the power of real numbers, complex
        numbers and quaternions

        :param mathEntity: The mathematical entity on the left side
            of the operator
        :param modulo: The value that this complex number will be modded
             by after the exponent is applied
        :return: The result of taking this complex number to the power
            of the given mathematical entity
        """

        from calc._ComplexMediator import _exponent

        result = _exponent(self, mathEntity)

        if modulo is None:
            return result
        else:
            return result % modulo

    def __rpow__(self, real):
        """
        Takes another mathematical entity to the power of this
        complex numbers with this complex number on the right
        side of the operator. Complex numbers can be the exponent
        of real numbers, complex numbers and quaternions. This method
        will only be called when the mathematical entity on the left side
        of the operator is an int or a float

        :param real: The real number on the left side of the operator
        :return: The result of taking the given real number to the
            power of this complex number
        """

        value1 = (real ** 2) ** (self.real / 2)
        value2 = cos(log(real))
        value3 = sin(log(real))

        return Complex(value1 * value2, value1 * value3)

    def __abs__(self):
        """
        Computes the absolute value of this complex number

        :return: The absolute value of this complex number
        """

        return sqrt((self.real ** 2) + (self.imag0 ** 2))

    def conjugate(self):
        """
        Returns the conjugate of this complex number

        :return: The conjugate of this complex number
        """

        return Complex(self.real, -self.imag0)

    def __floor__(self):
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

    def __ceil__(self):
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

    def __round__(self, numDecimals=None):
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
    def fromBuiltInComplex(builtInComplex):
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
    def toBuiltInComplex(customComplex):
        """
        Converts a variable of type Complex to a variable
        of type complex

        :param customComplex: The variable of type Complex
            to be converted
        :return: A variable of type complex that is mathematically
            equal to the input
        """

        return complex(customComplex.real, customComplex.imag0)

    def __iter__(self):
        """
        Returns an iterator over the real and imaginary components
        of this complex number

        :return: An iterator over the real and imaginary components
            of this complex number
        """

        return iter([self.real, self.imag0])

    def __hash__(self):
        """
        Computes a hash code for this complex number

        :return: A hash code for this complex number
        """

        modifier = 31
        hashCode = 0

        hashCode += modifier * hash(self.real)
        hashCode += modifier * hash(self.imag0)

        return hashCode

    def __eq__(self, mathEntity):
        """
        Checkes if this complex number is mathematically equal to
        another mathematical entity. Complex numbers can be equal to
        real numbers, complex numbers and quaternions

        :param mathEntity: The mathematical entity which will
            be compared with this complex number for mathematical
            equality
        :return: True if this complex number and the given
            mathematical entity are equal, False otherwise
        """

        from calc._ComplexMediator import _equality

        return _equality(self, mathEntity)

    def __str__(self):
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
    def __symbol(value, axis):
        """
        Computes the string representation of a given component
        of this complex number

        :param value: The value of the component to be represented
        :param axis: The axis of the component to be represented
        :return: A string representation of a given component
            of this complex number
        """

        if value == 0:
            return "0" + axis
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
