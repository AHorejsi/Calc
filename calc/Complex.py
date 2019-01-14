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
        Adds the complex number to another mathematical entity with
        the complex number on the right side of the operator. Complex
        numbers can be added to real numbers, complex numbers and
        quaternions

        :param mathEntity: The mathematical entity on the left side
            of the operator
        :return: The sum of the given mathematical entity and this
            complex number
        """

        return self + mathEntity

    def __sub__(self, mathEntity):
        from calc._ComplexMediator import _subtraction

        return _subtraction(self, mathEntity)

    def __rsub__(self, real):
        return Complex(real - self.real, -self.imag0)

    def __mul__(self, mathEntity):
        from calc._ComplexMediator import _multiplication

        return _multiplication(self, mathEntity)

    def __rmul__(self, mathEntity):
        return self * mathEntity

    def __truediv__(self, mathEntity):
        from calc._ComplexMediator import _division

        return _division(self, mathEntity)

    def __rtruediv__(self, real):
        conj = self.conjugate()
        numerator = real * conj
        denominator = (self * conj).real

        return Complex(numerator.real / denominator, numerator.imag0 / denominator)

    def __pow__(self, mathEntity, modulo=None):
        from calc._ComplexMediator import _exponent

        return _exponent(self, mathEntity)

    def __rpow__(self, real):
        value1 = (real ** 2) ** (self.real / 2)
        value2 = cos(log(real))
        value3 = sin(log(real))

        return Complex(value1 * value2, value1 * value3)

    def __abs__(self):
        return sqrt((self.real ** 2) + (self.imag0 ** 2))

    def conjugate(self):
        return Complex(self.real, -self.imag0)

    def __floor__(self):
        real = floor(self.real)
        imag0 = floor(self.imag0)

        return Complex(real, imag0)

    def __ceil__(self):
        real = ceil(self.real)
        imag0 = ceil(self.imag0)

        return Complex(real, imag0)

    def __round__(self, numDecimals=None):
        real = round(self.real, numDecimals)
        imag0 = round(self.imag0, numDecimals)

        return Complex(real, imag0)

    @staticmethod
    def fromBuiltInComplex(builtInComplex):
        return Complex(builtInComplex.real, builtInComplex.imag)

    @staticmethod
    def toBuiltInComplex(customComplex):
        return complex(customComplex.real, customComplex.imag0)

    def __iter__(self):
        return iter([self.real, self.imag0])

    def __hash__(self):
        modifier = 31
        hashCode = 0

        hashCode += modifier * hash(self.real)
        hashCode += modifier * hash(self.imag0)

        return hashCode

    def __eq__(self, mathEntity):
        from calc._ComplexMediator import _equality

        return _equality(self, mathEntity)

    def __str__(self):
        strRep = Complex.__symbol(self.real, "") + Complex.__symbol(self.imag0, "i")

        if strRep.startswith("+"):
            return strRep[1:]
        elif len(strRep) == 0:
            return "0"
        else:
            return strRep

    @staticmethod
    def __symbol(value, axis):
        if value == 0:
            return ""
        elif value < 0:
            return "-" + str(abs(value)) + axis
        else:
            return "+" + str(value) + axis
