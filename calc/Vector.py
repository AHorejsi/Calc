from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from math import sqrt, acos, floor, ceil
from copy import copy


class Vector(MathEntity, Negatable):
    """
    Instances of this class represent mathematical vectors
    """

    def __init__(self, point):
        """
        Constructs a vector with the given list of real numbers

        :param point: A list of real numbers to represent this
            vector's position in space
        """

        self.__point = point

    def __len__(self):
        """
        Returns the dimensions of this vector

        :return: The dimensions of this vector
        """

        return len(self.__point)

    def equalDimensions(self, vector):
        """
        Checks if this vector has the same dimensions of another
        vector

        :param vector: The vector whose dimensions will be compared
            with this vector
        :return: True if both vectors have the same dimensions, False
            otherwise
        """

        return len(self) == len(vector)

    def __getitem__(self, index):
        """
        Returns a component of this vector based
        on its indexed position

        :param index: An integer corresponding to
            the desired component's position in the
            vector
        :return: A component of this vector based on the
            given index
        """

        return self.__point[index]

    def __setitem__(self, index, value):
        """
        Resets a component of this vector with a new value
        based on an indexed position

        :param index: An integer corresponding to
            thee desired component to be changed
        :param value: The new value for the given
            component
        :return: None
        """

        self.__point[index] = value

    def __add__(self, mathEntity):
        """
        Adds this vector to the given mathematical entity
        with this vector on the right side of the operator.
        Vectors can be added to only vectors

        :param mathEntity: The mathematical entity on the
            right side of the operator
        :return: The sum of this vector and the given
            mathematical entity
        """

        from calc._VectorMediator import _addition

        return _addition(self, mathEntity)

    def __sub__(self, mathEntity):
        """
        Subtracts another mathematical entity from this
        vector with this vector on the left side of the
        operator. Vectors can only have vectors
        subtracted from them

        :param mathEntity: The mathematical entity on
            the right side of the operator
        :return: The difference of this vector and the
            given mathematical entity
        """

        from calc._VectorMediator import _subtraction

        return _subtraction(self, mathEntity)

    def __mul__(self, mathEntity):
        """
        Multiplies this vector by another mathematical entity
        with this vector on the left side of the operator.
        Vectors can be multiplied by real numbers and matrices

        :param mathEntity: The mathematical entity on the right
            side of the operator
        :return: The product of this vector and the given
            mathematical entity
        """

        from calc._VectorMediator import _multiplication

        return _multiplication(self, mathEntity)

    def __rmul__(self, mathEntity):
        """
        Multiplies this vector by another mathematical entity
        with this vector on the right side of the operator.
        Vectors can be multiplied by real numbers and matrices.
        This method will only be called when the mathematical entity
        on the left side of the operator is an int or a float

        :param mathEntity: The mathematical entity on the left
            side of the operator
        :return: The product of the given mathematical entity
            and this vector
        """

        return self * mathEntity

    def __truediv__(self, mathEntity):
        """
        Divides this vector by another mathematical entity with
        this vector on the left side of the operator. Vectors can
        be divided by real numbers

        :param mathEntity: The mathematical entity on the right
            side of the operator
        :return: The quotient of this vector and the given
            mathematical entity
        """

        from calc._VectorMediator import _division

        return _division(self, mathEntity)

    def dot(self, vector):
        """
        Computes the dot product of two vectors

        :param vector: The other vector to be used
            to compute a dot product
        :return: The dot product of this vector and
            the given vector
        :raises ArithmeticError: Raised if both
            vectors do not have te same dimensions
        """

        if not self.equalDimensions(vector):
            raise ArithmeticError("Vectors must be of equal dimensions")

        dotProduct = 0.0

        for leftValue, rightValue in zip(self, vector):
            dotProduct += leftValue * rightValue

        return dotProduct

    def cross(self, vector):
        """
        Computes the cross product of two vectors

        :param vector: The other vector to be used
            to compute a cross product
        :return: The cross product of this vector
            and the given vector
        :raises ArithmeticError: Raised if either
            vector is not three-dimensional
        """

        if len(self) == 3 and len(vector) == 3:
            return Vector([self[1] * vector[2] - self[2] * vector[1],
                           self[2] * vector[0] - self[0] * vector[2],
                           self[0] * vector[1] - self[1] * vector[0]])

        raise ArithmeticError("Vectors must be of 3 dimensions to have a cross product")

    @property
    def magnitude(self):
        """
        Computes the magnitude of this vector

        :return: The magnitude of this vector
        """

        mag = 0.0

        for value in self:
            mag += value ** 2

        mag = sqrt(mag)

        return mag

    def normalize(self):
        """
        Returns the normalized value of this vector

        :return: The normalized value of this vector
        """

        return self / self.magnitude

    def angleBetween(self, vector):
        """
        Calculates the angle between two vectors

        :param vector: Another vector with the same
            dimensions as this vector
        :return: The angle between this vector and
            the given vector
        :raises ArithmeticError: Raised if both
            vectors do not have te same dimensions
        """

        return acos(self.dot(vector) / (self.magnitude * vector.magnitude))

    def distanceFrom(self, vector):
        """
        Calculates the distance between two vectors

        :param vector: Another vector with the same
            dimensions as this vector
        :return: The distance between this vector and
            the given vector
        :raises ArithmeticError: Raised if both vectors
            do not have the same dimensions
        """

        if not self.equalDimensions(vector):
            raise ArithmeticError("Vectors must be of equal dimensions")

        distance = 0.0

        for leftValue, rightValue in zip(self, vector):
            distance += (leftValue - rightValue) ** 2

        distance = sqrt(distance)

        return distance

    def toList(self):
        """
        Converts this vector to a list

        :return: A list with the same elements
            as this vector
        """

        return copy(self.__point)

    def __floor__(self):
        """
        Rounds all the components of this vector down

        :return: A new vector with the same values as
            this vector with all values rounded down
        """

        point = []

        for value in self:
            point.append(floor(value))

        return Vector(point)

    def __ceil__(self):
        """
        Rounds all the components of this vector up

        :return: A new vector with the same values as
            this vector with all values rounded up
        """

        point = []

        for value in self:
            point.append(ceil(value))

        return Vector(point)

    def __round__(self, numDecimals=None):
        """
        Rounds all the components of this vector to a
        given number of decimal places

        :param numDecimals: The number of decimal places
            to round each value
        :return: A new vector with the same values as
            this vector with all values rounded to a
            given number of decimal places
        """

        point = []

        for value in self:
            point.append(round(value, numDecimals))

        return Vector(point)

    def __contains__(self, searchValue):
        """
        Checks if this vector contains a specific value

        :param searchValue: The value to be searched for
            in this vector
        :return: True if the given value is contained in
            this vector, False otherwise
        """

        return searchValue in self.__point

    def __iter__(self):
        """
        Returns an iterator over the components of
        this vector

        :return: An iterator over the components of
            this vector
        """

        return iter(self.__point)

    def __hash__(self):
        """
        Computes a hash code for this vector

        :return: A hash code for this vector
        """

        hashCode = 0
        MODIFIER = 31

        for value in self:
            hashCode += MODIFIER * hash(value)

        return hashCode

    def __eq__(self, mathEntity):
        """
        Checks if this vector is mathematically equal to
        the given mathematical entity. Vector can only be equal
        to other vectors

        :param mathEntity: The mathematical entity which will
            be compared with this vector for mathematical
            equality
        :return: True if this vector is equal to the given
            mathematical entity, False otherwise
        """

        from calc._VectorMediator import _equality

        return _equality(self, mathEntity)

    def __str__(self):
        """
        Returns a string representation of this vector

        :return: A string representation of this vector
        """

        strRep = "<"

        for index in range(len(self)):
            strRep += str(self[index])

            if index == len(self) - 1:
                strRep += ">"
            else:
                strRep += ", "

        return strRep
