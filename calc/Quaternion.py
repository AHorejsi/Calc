from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from calc.Exponentable import Exponentable
from math import sqrt, floor, ceil


class Quaternion(MathEntity, Negatable, Exponentable):
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

    def __add__(self, mathEntity):
        """
        Adds this quaternion to the given mathematical entity
        with this quaternion on the left side of the operator.
        Quaternions can be added to real numbers, complex
        numbers and quaternions

        :param mathEntity: The mathematical entity on the
            right side of the operator
        :return: The sum of this quaternion and the given
            mathematical entity
        """

        from calc._QuaternionMediator import _addition

        return _addition(self, mathEntity)

    def __radd__(self, real):
        """
        Adds this quaternion to another mathematical entity with
        the complex number on the right side of the operator.
        Quaternions can be added to real numbers, complex numbers and
        quaternions. This method will only be called when the number on the
        left side of the operator is an int or a float

        :param real: The mathematical entity on the left side
            of the operator
        :return: The sum of the given mathematical entity and this
            complex number
        """

        return self + real

    def __sub__(self, mathEntity):
        """
        Subtracts a mathematical entity from this quaternion
        with this quaternion on the left side of the operator.
        Real numbers, complex numbers and quaternions can be
        subtracted from quaternions

        :param mathEntity: The mathematical entity on the right
            side of the operator
        :return: The difference of this quaternion and the given
            mathematical entity
        """

        from calc._QuaternionMediator import _subtraction

        return _subtraction(self, mathEntity)

    def __rsub__(self, real):
        """
        Subtracts this quaternion from another mathematical
        entity with this quaternion on the right side of the
        operator. Real numbers, complex numbers and quaternions
        can have quaternions subtracted from them. This method
        will only be called when the number on the left side of
        the operator is an int or a float

        :param real: The mathematical entity on the left side of
            the operator
        :return: The difference of the given mathematical entity
            and this quaternion
        """

        return Quaternion(real - self.real, -self.imag0, -self.imag1, -self.imag2)

    def __mul__(self, mathEntity):
        """
        Multiplies this quaternion by the given mathematical
        entity with this quaternion on the left side of the
        operator. Real numbers, complex numbers, quaternions
        and matrices can be multiplied by quaternions

        :param mathEntity: The mathematical entity on the right
            side of the operator
        :return: The product of this quaternion and the given
            mathematical entity
        """

        from calc._QuaternionMediator import _multiplication

        return _multiplication(self, mathEntity)

    def __rmul__(self, real):
        """
        Multiplies this quaternion by the given mathematical
        entity with this quaternion on the right side of the
        operator. Real numbers, complex numbers, quaternions
        and matrices can be multiplied by quaternions. This method
        will only be called when the number on the left side of
        the operator is an int or a float

        :param real: The mathematical entity on the left side
            of the operator
        :return: The product of the given mathematical entity
            and this quaternion
        """

        return self * real

    def __truediv__(self, mathEntity):
        """
        Divides this quaternion by the given mathematical entity
        with this quaternion on the left side of the operator.
        Real numbers, complex numbers and quaternions can be
        divided from quaternions

        :param mathEntity: The mathematical entity on the right
            side of the operator
        :return: The quotient of this quaternion and the given
            mathematical entity
        """

        from calc._QuaternionMediator import _division

        return _division(self, mathEntity)

    def __rtruediv__(self, real):
        """
        Divides another mathematical entity by this quaternion
        with this quaternion on the right side of the operator.
        Real numbers, complex numbers, quaternions and matrices
        can have quaternions divided from them. This method
        will only be called when the number on the left side of
        the operator is an int or a float

        :param real: The mathematical entity on the left side
            of the operator
        :return: The quotient of the given mathematical entity
            and this quaternion
        """

        absoluteValueOfRight = abs(self)

        return Quaternion((real * self.real) / absoluteValueOfRight,
                          (-real * self.imag0) / absoluteValueOfRight,
                          (-real * self.imag1) / absoluteValueOfRight,
                          (-real * self.imag2) / absoluteValueOfRight)

    def __pow__(self, mathEntity, modulo=None):
        """
        Takes this quaternion to the power of the given mathematical
        entity with this quaternion on the left side of the operator.
        Quaternions can be taken to the power of real numbers

        :param mathEntity: The mathematical entity on the left side
            of the operator
        :param modulo: The value that this quaternion will be modded
                by after the exponent is applied
        :return: The result of taking this quaternion to the power
            of the given mathematical entity
        """

        from calc._QuaternionMediator import _exponent

        return _exponent(self, mathEntity)

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

        modifier = 31

        return modifier * hash(self.real) + \
               modifier * hash(self.imag0) + \
               modifier * hash(self.imag1) + \
               modifier * hash(self.imag2)

    def __eq__(self, mathEntity):
        """
        Checks if this quaternion is mathematically equal to
        the given mathematical entity. Quaternions can be equal
        to real numbers, complex numbers and quaternions

        :param mathEntity: The mathematical entity to be compared
            with this quaternion for equality
        :return: True if this quaternion is equal to the given
            mathematical entity, False otherwise
        """

        from calc._QuaternionMediator import _equality

        return _equality(self, mathEntity)

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
