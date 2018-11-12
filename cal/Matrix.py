from scipy.linalg import inv, det
from copy import deepcopy
from cal.MathEntity import MathEntity


class Matrix(MathEntity):
    def __init__(self, table, rowLength=None, columnLength=None):
        if (rowLength is None) or (columnLength is None):
            self.__table = []
            self.__rowLength = len(table)

            if self.__rowLength == 0:
                self.__columnLength = 0
            else:
                self.__columnLength = len(table[0])

            for row in table:
                self.__table.extend(row)
        else:
            self.__table = table
            self.__rowLength = rowLength
            self.__columnLength = columnLength

    @property
    def rowLength(self):
        return self.__rowLength

    @property
    def columnLength(self):
        return self.__columnLength

    def equalDimensions(self, matrix):
        return self.rowLength == matrix.rowLength and self.columnLength == matrix.columnLength

    def multipliable(self, matrix):
        return self.columnLength == matrix.rowLength

    def isSquare(self):
        return self.rowLength == self.columnLength

    def __getitem__(self, coordinates):
        if coordinates[0] < 0 or coordinates[0] >= self.rowLength or \
           coordinates[1] < 0 or coordinates[1] >= self.columnLength:
            raise Exception("Invalid indices")

        return self.__table[coordinates[0] * self.columnLength + coordinates[1]]

    def __setitem__(self, coordinates, value):
        if coordinates[0] < 0 or coordinates[0] >= self.rowLength or \
           coordinates[1] < 0 or coordinates[1] >= self.columnLength:
            raise Exception("Invalid indices")

        self.__table[coordinates[0] * self.columnLength + coordinates[1]] = value

    def __contains__(self, searchValue):
        for value in self:
            if value == searchValue:
                return True

        return False

    def determinant(self):
        if not self.isSquare():
            raise ArithmeticError("Only square Matrices have determinants")

        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return det(table, check_finite=False)

    def inverse(self):
        if not self.isSquare():
            raise ArithmeticError("Only square Matrices have inverses")

        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return Matrix(inv(table, check_finite=False).tolist())

    def conjugation(self):
        table = []

        for value in self:
            if hasattr(value, "conjugate"):
                table.append(value.conjugate())
            else:
                table.append(value)

        return Matrix(table, self.rowLength, self.columnLength)

    def transpose(self):
        table = []

        for colIndex in range(self.rowLength):
            for rowIndex in range(self.columnLength):
                table.append(self[rowIndex, colIndex])

        return Matrix(table, self.rowLength, self.columnLength)

    def to2DList(self):
        return deepcopy(self.__table)

    def __iter__(self):
        return self.__table.__iter__()

    def __hash__(self):
        hashCode = 0
        modifier = 31

        for value in self:
            hashCode += modifier * hash(value)

        return hashCode

    def __str__(self):
        strRep = ""
        index = 0

        while index < len(self.__table):
            strRep += str(self.__table[index : index + self.columnLength]) + "\n"
            index += self.columnLength

        return strRep
