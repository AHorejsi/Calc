import numpy as np


class Matrix:
    def __init__(self, table):
        self.__table = np.array(table)

    def rowLength(self):
        return len(self.__table)

    def columnLength(self):
        if self.rowLength() == 0:
            return 0
        else:
            return len(self.__table[0])

    def equalDimensions(self, matrix):
        return self.rowLength() == matrix.rowLength() and self.columnLength() == matrix.columnLength()

    def __getitem__(self, coordinates):
        return self.__table[coordinates]

    def __add__(self, matrix):
        if not self.equalDimensions(matrix):
            raise ArithmeticError("Matrices must be of equal dimensions to be added together")

        return Matrix(self.__table + matrix.__table)

    def __iadd__(self, matrix):
        return self + matrix

    def __sub__(self, matrix):
        if not self.equalDimensions(matrix):
            raise ArithmeticError("Matrices must be of equal dimensions to be subtracted from each other")

        return Matrix(self.__table - matrix.__table)

    def __isub__(self, matrix):
        return self - matrix

    def transpose(self):
        return self.__table.transpose()

    def __iter__(self):
        return self.__table.__iter__()

    def __hash__(self):
        hashCode = 0

        for row in self:
            for value in row:
                hashCode += 31 * hash(value)

        return int(hashCode)

    def __eq__(self, matrix):
        if type(matrix) is Matrix:
            return self.__table == matrix.__table
        else:
            return False

    def __ne__(self, matrix):
        return not self == matrix

    def __str__(self):
        return str(self.__table)