from math import sqrt, acos


class Vector:
    def __init__(self, point):
        self.__point = tuple(point)

    def __len__(self):
        return len(self.__point)

    def equalDimensions(self, vector):
        return len(self) == len(vector)

    def __getitem__(self, index):
        return self.__point[index]

    def __add__(self, vector):
        if not self.equalDimensions(vector):
            raise ArithmeticError("Vectors must be of equal dimensions to be added together")

        point = []

        for value1, value2 in zip(self, vector):
            point.append(value1 + value2)

        return Vector(point)

    def __iadd__(self, vector):
        return self + vector

    def __sub__(self, vector):
        if not self.equalDimensions(vector):
            raise ArithmeticError("Vectors must be of equal dimensions to be subtracted from each other")

        point = []

        for value1, value2 in zip(self, vector):
            point.append(value1 - value2)

        return Vector(point)

    def __isub__(self, vector):
        return self - vector

    def __mul__(self, realNumber):
        point = []

        for value in self:
            point.append(value * realNumber)

        return Vector(point)

    def __imul__(self, realNumber):
        return self * realNumber

    def __rmul__(self, realNumber):
        return self * realNumber

    def __truediv__(self, realNumber):
        return self * (1 / realNumber)

    def __itruediv__(self, realNumber):
        return self / realNumber

    def __floordiv__(self, realNumber):
        point = []

        for value in self:
            point.append(value // realNumber)

        return Vector(point)

    def __ifloordiv__(self, realNumber):
        return self // realNumber

    def __neg__(self):
        return self * -1

    def dot(self, vector):
        if not self.equalDimensions(vector):
            raise ArithmeticError("Vectors must be of equal dimensions to have a dot product")

        dotProduct = 0.0

        for value1, value2 in zip(self, vector):
            dotProduct += value1 * value2

        return dotProduct

    def magnitude(self):
        mag = 0.0

        for value in self:
            mag += value ** 2

        mag = sqrt(mag)

        return mag

    def normalize(self):
        return self / self.magnitude()

    def angleBetween(self, vector):
        return acos(self.dot(vector) / (self.magnitude() * vector.magnitude()))

    def __iter__(self):
        return self.__point.__iter__()

    def __hash__(self):
        return hash(self.__point)

    def __eq__(self, vector):
        if type(vector) is Vector:
            return self.__point == vector.__point
        else:
            return False

    def __ne__(self, vector):
        return not self == vector

    def __str__(self):
        strRep = "<"

        for index in range(len(self)):
            strRep += str(self[index])

            if index == len(self) - 1:
                strRep += ">"
            else:
                strRep += ", "

        return strRep
