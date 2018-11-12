from math import sqrt, acos
from cal.MathEntity import MathEntity


class Vector(MathEntity):
    def __init__(self, point):
        self.point = tuple(point)

    def __len__(self):
        return len(self.point)

    def equalDimensions(self, vector):
        return len(self) == len(vector)

    def __getitem__(self, index):
        return self.point[index]

    def __contains__(self, searchValue):
        for value in self:
            if value == searchValue:
                return True

        return False

    def component(self, index):
        point = []

        for currentIndex in range(len(self)):
            if currentIndex == index:
                point.append(self[currentIndex])
            else:
                point.append(0)

        return Vector(point)

    def allComponents(self):
        components = []

        for index in range(len(self)):
            components.append(self.component(index))

        return components

    def dot(self, vector):
        if not self.equalDimensions(vector):
            raise ArithmeticError("Two Vectors must be of equal dimensions to have a dot product")

        dotProduct = 0.0

        for value1, value2 in zip(self, vector):
            dotProduct += value1 * value2

        return dotProduct

    def cross(self, vector):
        if len(self) == 3 or len(vector) == 3:
            point = []

            point.append(self[1] * vector[2] - self[2] * vector[1])
            point.append(self[2] * vector[0] - self[0] * vector[2])
            point.append(self[0] * vector[1] - self[1] * vector[0])

            return Vector(point)

        raise ArithmeticError("Vectors must be of 3 dimensions to have a cross product")

    def linearlyInterpolate(self, vector, floatValue):
        return (self * floatValue) + (vector * (1.0 - floatValue))

    def magnitude(self):
        mag = 0.0

        for value in self:
            mag += value ** 2

        mag = sqrt(mag)

        return mag

    def normalize(self):
        return self / self.magnitude()

    def scalarTripleProduct(self, vector1, vector2):
        return self.dot(vector1.cross(vector2))

    def vectorTripleProduct(self, vector1, vector2):
        return self.cross(vector1.cross(vector2))

    def angleBetween(self, vector):
        return acos(self.dot(vector) / (self.magnitude() * vector.magnitude()))

    def distanceFrom(self, vector):
        distance = 0.0

        for value1, value2 in zip(self, vector):
            distance = (value1 - value2) ** 2

        distance = sqrt(distance)

        return distance

    def __iter__(self):
        return self.point.__iter__()

    def __hash__(self):
        hashCode = 0
        modifier = 31

        for value in self:
            hashCode += modifier * value

        return hashCode

    def __str__(self):
        strRep = "<"

        for index in range(len(self)):
            strRep += str(self[index])

            if index == len(self) - 1:
                strRep += ">"
            else:
                strRep += ", "

        return strRep
