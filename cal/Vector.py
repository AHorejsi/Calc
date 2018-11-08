from math import sqrt, acos


class Vector:
    def __init__(self, point):
        self.point = tuple(point)

    def __len__(self):
        return len(self.point)

    def equalDimensions(self, vector):
        return len(self) == len(vector)

    def __getitem__(self, index):
        return self.point[index]

    def dot(self, vector):
        if not self.equalDimensions(vector):
            raise ArithmeticError("Two Vectors must be of equal dimensions to have a dot product")

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

    def angleBetween(self, vector):
        return acos(self.dot(vector) / (self.magnitude() * vector.magnitude()))

    def __iter__(self):
        return self.point.__iter__()
