import numpy as np
from scipy.linalg import inv, det


class Matrix:
    def __init__(self, table):
        self.table = np.array(table)

    def rowLength(self):
        return len(self.table)

    def columnLength(self):
        if self.rowLength() == 0:
            return 0
        else:
            return len(self.table[0])

    def equalDimensions(self, matrix):
        return self.rowLength() == matrix.rowLength() and self.columnLength() == matrix.columnLength()

    def __getitem__(self, indices):
        return self.table[indices]

    def __add__(self, matrix):
        if not self.equalDimensions(matrix):
            raise ArithmeticError("Matrices must be of equal dimensions to be added together")

        return Matrix(self.table + matrix.table)

    def __iadd__(self, matrix):
        return self + matrix

    def __sub__(self, matrix):
        if not self.equalDimensions(matrix):
            raise ArithmeticError("Matrices must be of equal dimensions to be subtracted from each other")

        return Matrix(self.table - matrix.table)

    def __isub__(self, matrix):
        return self - matrix

    def __mul__(self, mathEntity):
        from calc.Vector import Vector

        typeOfArg = type(mathEntity)

        if typeOfArg is Matrix:
            return Matrix(self.table @ mathEntity.table)
        elif typeOfArg is Vector:
            result = self.table @ mathEntity
            result = np.array([result]).transpose()

            return Matrix(result)
        else:
            return Matrix(self.table * mathEntity)

    def __imul__(self, mathEntity):
        return self * mathEntity

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, mathEntity):
        typeOfArg = type(mathEntity)

        if typeOfArg is Matrix:
            return self * mathEntity.inverse()
        else:
            return self * (1 / mathEntity)

    def __itruediv__(self, mathEntity):
        return self / mathEntity

    def determinant(self):
        return det(self.table)

    def inverse(self):
        return inv(self.table)

    def transpose(self):
        return self.table.transpose()

    def __iter__(self):
        return self.table.__iter__()

    def __hash__(self):
        hashCode = 0

        for row in self:
            for value in row:
                hashCode += 31 * hash(value)

        return hashCode

    def __eq__(self, matrix):
        if type(matrix) is Matrix:
            return self.table == matrix.table
        else:
            return False

    def __ne__(self, matrix):
        return not self == matrix

    def __str__(self):
        return str(self.table)
