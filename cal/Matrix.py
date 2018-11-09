from scipy.linalg import det, inv


class Matrix:
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

    def determinant(self):
        if not self.isSquare():
            raise ArithmeticError("Only square Matrices have determinants")

        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return det(table)

    def inverse(self):
        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return inv(table)

    def __getitem__(self, coordinates):
        return self.table[coordinates[0] * self.columnLength + coordinates[1]]
