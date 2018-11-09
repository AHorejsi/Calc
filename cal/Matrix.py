import numpy as np
from cal.MathEntity import MathEntity


class Matrix(MathEntity):
    def __init__(self, table, rowLength=None, columnLength=None):
        if (rowLength is None) and (columnLength is None):
            self.table = []
            self.rowLength = len(table)

            if self.rowLength == 0:
                self.columnLength = 0
            else:
                self.columnLength = len(table[0])

            for row in table:
                self.table.extend(row)
        else:
            self.table = table
            self.rowLength = rowLength
            self.columnLength = columnLength

    def equalDimensions(self, matrix):
        return self.rowLength == matrix.rowLength and self.columnLength == matrix.columnLength

    def multipliable(self, matrix):
        return self.columnLength == matrix.rowLength

    def isSquare(self):
        return self.rowLength == self.columnLength

    def __getitem__(self, coordinates):
        return self.table[coordinates[0] * self.columnLength + coordinates[1]]

    def determinant(self):
        if not self.isSquare():
            raise ArithmeticError("Only square Matrices have determinants")

        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return np.linalg.det(table)

    def inverse(self):
        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return Matrix(np.linalg.inv(table).tolist())

    def __iter__(self):
        return self.table.__iter__()

    def __hash__(self):
        hash = 0
        modifier = 31

        for value in self:
            hash += modifier * hash(value)

        return hash

    def __str__(self):
        return str(self.table)
