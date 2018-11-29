from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from math import sqrt, acos, floor, ceil
from copy import copy


class Vector(MathEntity, Negatable):
    def __init__(self, point):
        self.__point = point

    def __len__(self):
        return len(self.__point)

    def equalDimensions(self, vector):
        return len(self) == len(vector)

    def __getitem__(self, index):
        return self.__point[index]

    def __add__(self, mathEntity):
        from calc._VectorMediator import _addition

        return _addition(self, mathEntity)

    def __radd__(self, mathEntity):
        return self + mathEntity

    def __sub__(self, mathEntity):
        from calc._VectorMediator import _subtraction

        return _subtraction(self, mathEntity)

    def __rsub__(self, mathEntity):
        return -self + mathEntity

    def __mul__(self, mathEntity):
        from calc._VectorMediator import _multiplication

        return _multiplication(self, mathEntity)

    def __rmul__(self, mathEntity):
        return self * mathEntity

    def __truediv__(self, mathEntity):
        from calc._VectorMediator import _division

        return _division(self, mathEntity)

    def dot(self, vector):
        if not self.equalDimensions(vector):
            raise ArithmeticError("Vectors must be of equal dimensions")

        dotProduct = 0.0

        for leftValue, rightValue in zip(self, vector):
            dotProduct += leftValue * rightValue

        return dotProduct

    def cross(self, vector):
        if len(self) == 3 and len(vector) == 3:
            return Vector([self[1] * vector[2] - self[2] * vector[1],
                           self[2] * vector[0] - self[0] * vector[2],
                           self[0] * vector[1] - self[1] * vector[0]])

        raise ArithmeticError("Vectors must be of 3 dimensions to have a cross product")

    def scalarTripleProduct(self, vector1, vector2):
        return self.dot(vector1.cross(vector2))

    def vectorTripleProduct(self, vector1, vector2):
        return self.cross(vector1.cross(vector2))

    @property
    def magnitude(self):
        mag = 0.0

        for value in self:
            mag += value ** 2

        mag = sqrt(mag)

        return mag

    def normalize(self):
        return self / self.magnitude

    def angleBetween(self, vector):
        return acos(self.dot(vector) / (self.magnitude * vector.magnitude))

    def distanceFrom(self, vector):
        distance = 0.0

        for leftValue, rightValue in zip(self, vector):
            distance += (leftValue - rightValue) ** 2

        distance = sqrt(distance)

        return distance

    def toList(self):
        return copy(self.__point)

    def __floor__(self):
        point = []

        for value in self:
            point.append(floor(value))

        return Vector(point)

    def __ceil__(self):
        point = []

        for value in self:
            point.append(ceil(value))

        return Vector(point)

    def __round__(self, numDecimals=None):
        point = []

        for value in self:
            point.append(round(value, numDecimals))

        return Vector(point)

    def __contains__(self, searchValue):
        for value in self:
            if value == searchValue:
                return True

        return False

    def __iter__(self):
        return self.__point.__iter__()

    def __hash__(self):
        hashCode = 0
        modifier = 31

        for value in self:
            hashCode += modifier * hash(value)

        return hashCode

    def __eq__(self, mathEntity):
        from calc._VectorMediator import _equality

        return _equality(self, mathEntity)

    def __str__(self):
        strRep = "<"

        for index in range(len(self)):
            strRep += str(self[index])

            if index == len(self) - 1:
                strRep += ">"
            else:
                strRep += ", "

        return strRep

    def __repr__(self):
        return str(self)
