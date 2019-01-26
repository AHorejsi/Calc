from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from scipy.linalg import inv
from math import floor, ceil


class Matrix(MathEntity, Negatable):
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

    def __add__(self, mathEntity):
        """
        Adds this matrix to another mathematical entity with
        this matrix on the left side of the operator. Matrices
        can only be added to other matrices

        :param mathEntity: The mathematical entity on the right
            side of the operator
        :return: The sum of this matrix and the given mathematical
            entity
        :raises ArithmeticError: Raised if this matrix and the
            given matrix do not have the same dimensions
        """

        from calc._MatrixMediator import _addition

        return _addition(self, mathEntity)

    def __sub__(self, mathEntity):
        """
        Subtracts another mathematical entity from this matrix with
        this matrix on the left side of the operator. Matrices can
        have only other matrices subtracted from them

        :param mathEntity: The mathematical entity on the
            right side of the operator
        :return: The difference of this matrix and the given
            mathematical entity
        :raises ArithmeticError: Raised if this matrix and the given
            matrix do not have the same dimensions
        """

        from calc._MatrixMediator import _subtraction

        return _subtraction(self, mathEntity)

    def __mul__(self, mathEntity):
        """
        Multiplies this matrix by another mathematical entity with
        this matrix on the left side of the operator. Matrices can
        be multiplied by real numbers, complex numbers, quaternions,
        vectors and matrices

        :param mathEntity: The mathematical entity on the right side
            of the operator
        :return: The product of this matrix and the given mathematical
            entity
        :raises ArithmeticError: Raised if the given mathematical entity
            is a matrix and does not satisfy the conditions for matrix
            multiplication
        """

        from calc._MatrixMediator import _multiplication

        return _multiplication(self, mathEntity)

    def __truediv__(self, mathEntity):
        """
        Divides this matrix by another mathematical entity with
        this matrix on the left side of the operator. Matrices
        can be divided by real numbers, complex numbers, quaternions
        and matrices

        :param mathEntity: The mathematical entity on the right side
            of the operator
        :return: The quotient of this matrix and the given mathematical
            entity
        :raises ArithmeticError: Raised if the given mathematical entity
            is a matrix and does not satisfy the conditions for matrix
            division
        """

        from calc._MatrixMediator import _division

        return _division(self, mathEntity)

    def __contains__(self, searchValue):
        return searchValue in self.__table

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
        if size == 1:
            return table[0]
        elif size == 2:
            return table[0] * table[3] - table[2] * table[1]
        else:
            det = 0.0

            for column in range(size):
                subtable = []
                rowIndex = 1

                while rowIndex < size:
                    for columnIndex in range(size):
                        if columnIndex != column:
                            subtable.append(table[rowIndex * size + columnIndex])

                    rowIndex += 1

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

        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return Matrix(inv(table, check_finite=False).tolist())

    def transpose(self):
        """
        Returns the transpose of this matrix

        :return: The transpose of this matrix
        """

        table = []

        for colIndex in range(self.rowLength):
            for rowIndex in range(self.columnLength):
                table.append(self[rowIndex, colIndex])

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

    def __hash__(self):
        """
        Computes a hash code for this matrix

        :return: A hash code for this matrix
        """

        hashCode = 0
        modifier = 31

        for value in self:
            hashCode += modifier * hash(value)

        return hashCode

    def __eq__(self, mathEntity):
        """
        Checks if this matrix is equal to the given mathematical
        entity. Matrices can only be equal to other matrices

        :param mathEntity: The mathematical entity to be compared with
            this matrix for equality
        :return: True if this matrix and the given mathematical entity
            are mathematically equal, False otherwise
        """

        from calc._MatrixMediator import _equality

        return _equality(self, mathEntity)

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
                strRep += ", "

        return strRep
