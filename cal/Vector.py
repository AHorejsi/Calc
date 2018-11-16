from math import sqrt, acos
from copy import copy
from cal.MathEntity import MathEntity


class Vector(MathEntity):
    """
    Instances of this class represent n-dimensional Vectors
    """

    def __init__(self, point):
        """
        Uses a list of any length that is filled with ints or floats to
        represent an n-dimensional Vector. The indices of each value
        determine the axis each value is assigned to

        :param point: List of ints or floats that will serve as the position
        of this Vector
        """

        self.__point = point

    def __len__(self):
        """
        Returns the dimensions of this Vector

        :return: The dimensions of this Vector
        """

        return len(self.__point)

    def equalDimensions(self, vector):
        """
        Checks if two Vectors have the same dimensions

        :param vector: The Vector being checked for if it has the same dimensions
            as this one
        :return: True if both Vectors have the same dimensions, False otherwise
        """

        return len(self) == len(vector)

    def __getitem__(self, index):
        """
        Returns the value along a particular axis of this Vector.
        The axis to be retrieved is determined by an index

        :param index: The index of the value to be obtained
        :return: The value along the axis corresponding to the given index
        """

        return self.__point[index]

    def __contains__(self, searchValue):
        """
        Checks if this Vector has a certain value along one of its axes

        :param searchValue: The value to be searched for
        :return: True if this Vector has the given value, False otherwise
        """

        for value in self:
            if value == searchValue:
                return True

        return False

    def component(self, index):
        """
        Returns one of this Vector's component Vectors

        :param index: The index of the component Vector to be obtained
        :return: The component Vector corresponding to the given index
        """

        point = []

        for currentIndex in range(len(self)):
            if currentIndex == index:
                point.append(self[currentIndex])
            else:
                point.append(0)

        return Vector(point)

    def allComponents(self):
        """
        Returns all of this Vector's component Vectors

        :return: All of this Vector's component Vectors
        """

        components = []

        for index in range(len(self)):
            components.append(self.component(index))

        return components

    def dot(self, vector):
        """
        Calculates the dot product of two Vectors

        :param vector: The other Vector the dot product will be calculated with
        :return: The dot product of this Vector and the argument
        :exception ArithmeticError: Raised when the two Vectors do not have the
            same dimensions
        """

        if not self.equalDimensions(vector):
            raise ArithmeticError("Two Vectors must be of equal dimensions to have a dot product")

        dotProduct = 0.0

        for value1, value2 in zip(self, vector):
            dotProduct += value1 * value2

        return dotProduct

    def cross(self, vector):
        """
        Calculates the cross product between two Vectors

        :param vector: The other Vector to be used to calculate the cross product
        :return: The cross product of this Vector and the given Vector
        :exception ArithmeticError: Raised if both Vectors are not 3-dimensional
        """

        if len(self) == 3 and len(vector) == 3:
            return Vector([self[1] * vector[2] - self[2] * vector[1],
                           self[2] * vector[0] - self[0] * vector[2],
                           self[0] * vector[1] - self[1] * vector[0]])

        raise ArithmeticError("Vectors must be of 3 dimensions to have a cross product")

    @property
    def magnitude(self):
        """
        Calculates the magnitude of this Vector

        :return: The magnitude of this Vector
        """

        mag = 0.0

        for value in self:
            mag += value ** 2

        mag = sqrt(mag)

        return mag

    def normalize(self):
        """
        Calculates a unit Vector that points in the same direction
        as this Vector

        :return: A unit Vector that points in the same direction
            as this Vector
        """

        return self / self.magnitude

    def scalarTripleProduct(self, vector1, vector2):
        """
        Calculates the scalar triple product of three Vectors

        :param vector1: A 3D Vector
        :param vector2: A 3D Vector
        :return: self `dot` (vector1 `cross` vector2). The result is a float
        """

        return self.dot(vector1.cross(vector2))

    def vectorTripleProduct(self, vector1, vector2):
        """
        Calculates the vector triple product of three Vectors

        :param vector1: A 3D Vector
        :param vector2: A 3D Vector
        :return: self `cross` (vector1 `cross` vector2). The result is a Vector
        """

        return self.cross(vector1.cross(vector2))

    def angleBetween(self, vector):
        """
        Calculates the angle between two Vectors

        :param vector: The other Vector from which the angle is being determined
        :return: The angle between this Vector and the argument
        """

        return acos(self.dot(vector) / (self.magnitude * vector.magnitude))

    def distanceFrom(self, vector):
        """
        Calculates the distance between two Vectors

        :param vector: The other Vector whose distance from the Vector
            is being determined
        :return: The distance between this Vector and the argument
        """

        distance = 0.0

        for value1, value2 in zip(self, vector):
            distance = (value1 - value2) ** 2

        distance = sqrt(distance)

        return distance

    def toList(self):
        """
        Creates a list of this Vector's values

        :return: A list of this Vector's values
        """

        return copy(self.__point)

    def __iter__(self):
        """
        Returns an iterator over this Vector's axes

        :return: An iterator over this Vector's axes
        """

        return self.__point.__iter__()

    def __hash__(self):
        """
        Calculates a hash code for this Vector

        :return: A  hash code for this Vector
        """

        hashCode = 0
        modifier = 31

        for value in self:
            hashCode += modifier * hash(value)

        return hashCode

    def __str__(self):
        """
        Creates a string representation of this Vector

        :return: A string representation of this Vector
        """

        strRep = "<"

        for index in range(len(self)):
            strRep += str(self[index])

            if index == len(self) - 1:
                strRep += ">"
            else:
                strRep += ", "

        return strRep

    def __repr__(self):
        """
        Creates a string representation of this Vector

        :return: A string representation of this Vector
        """

        return self.__str__()
