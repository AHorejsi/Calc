from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from calc.Exponentable import Exponentable
from math import floor, ceil
from copy import copy, deepcopy


class Matrix(MathEntity, Negatable, Exponentable):
    """
    Instances of this class represent mathematical
    matrices. Matrices are containers of real numbers,
    complex numbers and/or quaternions which are arranged
    into rows and columns
    """

    def __init__(self, table, rowLength=None, columnLength=None):
        """
        Constructs a matrix based on the 2D list of real numbers,
        complex numbers and quaternions

        :param table: The table of values to be represented as a
            mathematical matrix
        :param rowLength: The number of rows for this matrix. Should
            only be filled if the table that was input is 1D
        :param columnLength: The number of columns for this matrix. Should
            only be filled if the table that was input is 1D
        """

        if (rowLength is None) and (columnLength is None):
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

    def __len__(self):
        return self.rowLength * self.columnLength

    @property
    def rowLength(self):
        """
        Returns the number of rows that this matrix
        has

        :return: The number of rows that this matrix
            has
        """

        return self.__rowLength

    @property
    def columnLength(self):
        """
        Returns the number of columns that this
        matrix has

        :return: The number of columns that this
            matrix has
        """

        return self.__columnLength

    def equalDimensions(self, matrix):
        """
        Checks if two matrices have the same number
        of rows and the same number of columns

        :param matrix: The matrix to be compared with
            this matrix
        :return: True if this matrix has the same dimensions
            as the given matrix, False otherwise
        """

        return self.rowLength == matrix.rowLength and self.columnLength == matrix.columnLength

    def multipliable(self, matrix):
        """
        Checks if this matrix can be multiplied by another
        matrix with this matrix on the left side of the
        multiplication operator

        :param matrix: The matrix to be checked for if it
            can be multiplied to this matrix with it on
            the right side of the multiplication operator
        :return: True if (self * matrix) is possible, False
            otherwise
        """

        return self.columnLength == matrix.rowLength

    def divisible(self, matrix):
        """
        Checks if this matrix can be divided by another
        matrix with this matrix on the left side of the
        division operator

        :param matrix: The matrix to be checked for if it
            can be divided from this matrix with it on
            the right side of the division operator
        :return: True if (self / matrix) is possible, False
            otherwise
        """

        return self.multipliable(matrix) and matrix.isSquare

    @property
    def isSquare(self):
        """
        Checks if the number of rows that this matrix has is equal
        to the number of columns it has

        :return: True if the number of rows that this matrix has is
            equal to the number of columns it has
        """

        return self.rowLength == self.columnLength

    def __getitem__(self, coordinates):
        """
        Returns the element at the given row and column indices

        :param coordinates: A tuple containing the row and column
            indices of the element to be returned
        :return: The elements at the given row and column indices
        :raises IndexError: Raised if the given row and column
            indices are outside the bounds of this matrix
        """

        if coordinates[0] < 0 or coordinates[0] >= self.rowLength or \
           coordinates[1] < 0 or coordinates[1] >= self.columnLength:
            raise IndexError("Invalid indices")

        return self.__table[coordinates[0] * self.columnLength + coordinates[1]]

    def __setitem__(self, coordinates, value):
        """
        Sets the elements at the given row and column indices

        :param coordinates: A tuple containing the row and
            column indices of the element to be returned
        :param value: The new value for the element at the
            given row and column indices
        :return: None
        :raises IndexError: Raised if the given row and column
            indices are outside the bounds of this matrix
        """

        if coordinates[0] < 0 or coordinates[0] >= self.rowLength or \
           coordinates[1] < 0 or coordinates[1] >= self.columnLength:
            raise IndexError("Invalid indices")

        self.__table[coordinates[0] * self.columnLength + coordinates[1]] = value

    def __contains__(self, searchValue):
        """
        Checks if this matrix contains a certain value

        :param searchValue: The value to be searched
            for
        :return: True if this matrix contains the
            given value, False otherwise
        """

        return searchValue in self.__table

    @staticmethod
    def identity(size):
        """
        Returns aa square identity matrix of the
        given size

        :param size: The number of rows and columns
            that the generated matrix will have
        :return: A square identity matrix
        """

        table = []

        for rowIndex in range(size):
            for columnIndex in range(size):
                if rowIndex == columnIndex:
                    table.append(1)
                else:
                    table.append(0)

        return Matrix(table, size, size)

    def conjugate(self):
        """
        Returns a matrix with all of the values
        that have conjugates as conjugates

        :return: A copy of this matrix with all
            of the value swapped with their conjugates,
            if they have one
        """

        newTable = []

        for value in self:
            if hasattr(value, "conjugate"):
                newTable.append(value.conjugate())

        return Matrix(newTable, self.rowLength, self.columnLength)

    @property
    def determinant(self):
        """
        Returns the determinant of this matrix

        :return: The determinant of this matrix
        :raises ArithmeticError: Raised if this matrix
            is not square
        """

        if not self.isSquare:
            raise ArithmeticError("Only square matrices have determinants")

        return Matrix.__determinant(self.__table, self.rowLength)

    @staticmethod
    def __determinant(table, size):
        """
        Computes the determinant of the matrix represented
        by the given table

        :param table: The matrix whose determinant is to be
            computed
        :param size: The number of rows in the table
        :return: The determinant of the matrix represented
            by the table
        """

        if size == 1:
            return table[0]
        elif size == 2:
            return table[0] * table[3] - table[2] * table[1]
        else:
            det = 0.0

            # Move through the first row of this matrix
            # Ignore values in the current column
            for column in range(size):
                subtable = []

                for rowIndex in range(1, size):  # Start with 1 to ignore first row
                    for columnIndex in range(size):

                        # Ignore the value that is in the column being ignore
                        if columnIndex != column:
                            subtable.append(table[rowIndex * size + columnIndex])

                det += ((-1) ** column) * table[column] * Matrix.__determinant(subtable, size - 1)

            return det

    def inverse(self):
        """
        Returns the inverse of this matrix

        :return: The inverse of this matrix
        :raises ArithmeticError: Raised if this
            matrix is not square
        """

        if not self.isSquare:
            raise ArithmeticError("Only square Matrices have inverses")

        tempMatrix = deepcopy(self)
        newMatrix = Matrix.identity(self.rowLength)

        for index1 in range(tempMatrix.rowLength):
            divisor = tempMatrix[(index1, index1)]

            for index2 in range(tempMatrix.columnLength):
                tempMatrix[(index1, index2)] /= divisor
                newMatrix[(index1, index2)] /= divisor

            for index2 in range(tempMatrix.rowLength):
                if tempMatrix[(index1, index2)] != 1:
                    coefficient = tempMatrix[(index2, index1)]

                    for index3 in range(tempMatrix.columnLength):
                        tempMatrix[(index2, index3)] -= coefficient * tempMatrix[(index1, index3)]
                        newMatrix[(index2, index3)] -= coefficient * newMatrix[(index1, index3)]

        return newMatrix

    def transpose(self):
        """
        Returns the transpose of this matrix

        :return: The transpose of this matrix
        """

        table = []

        for colIndex in range(self.rowLength):
            for rowIndex in range(self.columnLength):
                table.append(self[(rowIndex, colIndex)])

        return Matrix(table, self.rowLength, self.columnLength)

    def to2DList(self):
        """
        Converts this matrix to a 2D list

        :return: A 2D list with the same contents
            of this matrix
        """

        table = []

        for rowIndex in range(self.rowLength):
            row = []

            for colIndex in range(self.columnLength):
                row.append(self[rowIndex, colIndex])

            table.append(row)

        return table

    def __floor__(self):
        """
        Rounds all elements of this matrix
        down

        :return: A new matrix with each element
            of this matrix rounded down
        """

        table = []

        for value in self:
            table.append(floor(value))

        return Matrix(table, self.rowLength, self.columnLength)

    def __ceil__(self):
        """
        Rounds all elements of this matrix
        up

        :return: A new matrix with each element
            of this matrix rounded up
        """

        table = []

        for value in self:
            table.append(ceil(value))

        return Matrix(table, self.rowLength, self.columnLength)

    def __round__(self, numDecimals=None):
        """
        Rounds all elements of this matrix
        to a given number of decimal places

        :param numDecimals: The number of decimals
            this matrix's elements should be rounded
            to
        :return: A new matrix with each element
            of this matrix rounded to the given number
            of decimal places
        """

        table = []

        for value in self:
            table.append(round(value, numDecimals))

        return Matrix(table, self.rowLength, self.columnLength)

    def __iter__(self):
        """
        Returns a row-by-row iterator over the elements
        of this matrix

        :return: A row-by-row iterator over the elements
            of this matrix
        """

        return iter(self.__table)

    def __copy__(self):
        """
        Creates a shallow copy of this matrix

        :return: A shallow copy of this matrix
        """

        return Matrix(self.__table, self.rowLength, self.columnLength)

    def __deepcopy__(self, memodict={}):
        """
        Creates a deep copy of this matrix

        :param memodict: N/A
        :return: A deep copy of this matrix
        """

        return Matrix(copy(self.__table), self.rowLength, self.columnLength)

    def __hash__(self):
        """
        Computes a hash code for this matrix

        :return: A hash code for this matrix
        """

        hashCode = 0
        MODIFIER = 31

        for value in self:
            hashCode += MODIFIER * hash(value)

        return hashCode

    def __str__(self):
        """
        Returns a string representation of this matrix

        :return: A string representation of this matrix
        """

        strRep = "["

        for rowIndex in range(self.rowLength):
            strRep += "["

            for colIndex in range(self.columnLength):
                strRep += str(self[rowIndex, colIndex])

                if colIndex == self.columnLength - 1:
                    strRep += "]"
                else:
                    strRep += ", "

            if rowIndex == self.rowLength - 1:
                strRep += "]"
            else:
                strRep += "\n"

        return strRep + "\n\n"
