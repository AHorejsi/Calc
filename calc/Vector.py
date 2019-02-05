from __future__ import annotations
from typing import Union, List, Iterable, Optional
from calc.MathEntity import MathEntity
from math import sqrt, acos, floor, ceil
from copy import copy


class Vector(MathEntity):
    """
    Instances of this class represent mathematical vectors
    """

    def __init__(self, point: List[Union[int, float]]):
        """
        Constructs a vector with the given list of real numbers

        :param point: A list of real numbers to represent this
            vector's position in space
        """

        self.__point = point

    def __len__(self) -> int:
        """
        Returns the dimensions of this vector

        :return: The dimensions of this vector
        """

        return len(self.__point)

    def equalDimensions(self, vector: Vector) -> bool:
        """
        Checks if this vector has the same dimensions of another
        vector

        :param vector: The vector whose dimensions will be compared
            with this vector
        :return: True if both vectors have the same dimensions, False
            otherwise
        """

        return len(self) == len(vector)

    def __getitem__(self, index: int) -> Union[int, float]:
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

    def __setitem__(self, index: int, value: Union[int, float]) -> None:
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

    def dot(self, vector: Vector) -> float:
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

        for (leftValue, rightValue) in zip(self, vector):
            dotProduct += leftValue * rightValue

        return dotProduct

    def cross(self, vector: Vector) -> Vector:
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
    def magnitude(self) -> float:
        """
        Computes the magnitude of this vector

        :return: The magnitude of this vector
        """

        mag = 0.0

        for value in self:
            mag += value ** 2

        mag = sqrt(mag)

        return mag

    def normalize(self) -> Vector:
        """
        Returns the normalized value of this vector

        :return: The normalized value of this vector
        """

        return self / self.magnitude

    def angleBetween(self, vector: Vector) -> float:
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

    def distanceFrom(self, vector: Vector) -> float:
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

        for (leftValue, rightValue) in zip(self, vector):
            distance += (leftValue - rightValue) ** 2

        distance = sqrt(distance)

        return distance

    def toList(self) -> List[Union[int, float]]:
        """
        Converts this vector to a list

        :return: A list with the same elements
            as this vector
        """

        return copy(self.__point)

    def __floor__(self) -> Vector:
        """
        Rounds all the components of this vector down

        :return: A new vector with the same values as
            this vector with all values rounded down
        """

        point = []

        for value in self:
            point.append(floor(value))

        return Vector(point)

    def __ceil__(self) -> Vector:
        """
        Rounds all the components of this vector up

        :return: A new vector with the same values as
            this vector with all values rounded up
        """

        point = []

        for value in self:
            point.append(ceil(value))

        return Vector(point)

    def __round__(self, numDecimals: Optional[int]=None) -> Vector:
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

    def __contains__(self, searchValue: Union[int, float]) -> bool:
        """
        Checks if this vector contains a specific value

        :param searchValue: The value to be searched for
            in this vector
        :return: True if the given value is contained in
            this vector, False otherwise
        """

        return searchValue in self.__point

    def __iter__(self) -> Iterable[Union[int, float]]:
        """
        Returns an iterator over the components of
        this vector

        :return: An iterator over the components of
            this vector
        """

        return iter(self.__point)

    def __copy__(self) -> Vector:
        """
        Creates a shallow copy of this vector

        :return: A shallow copy of this vector
        """

        return Vector(self.__point)

    def __deepcopy__(self, memodict: dict={}) -> Vector:
        """
        Creates a deep copy of this vector

        :param memodict: N/A
        :return: A deep copy of this vector
        """

        return Vector(copy(self.__point))

    def __hash__(self) -> int:
        """
        Computes a hash code for this vector

        :return: A hash code for this vector
        """

        hashCode = 0
        MODIFIER = 31

        for value in self:
            hashCode += MODIFIER * hash(value)

        return hashCode

    def __str__(self) -> str:
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
