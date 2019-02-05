from __future__ import annotations
from typing import Union, List, Optional, Tuple, Iterable
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from copy import copy, deepcopy


class Matrix(MathEntity):
    """
    Instances of this class represent mathematical
    matrices. Matrices are containers of real numbers,
    complex numbers and/or quaternions which are arranged
    into rows and columns
    """

    def __init__(self, table: List[List[Union[int, float, Complex, Quaternion]]]):
        """
        Constructs a matrix based on the 2D list of real numbers,
        complex numbers and quaternions

        :param table: The table of values to be represented as a
            mathematical matrix
        """
        self.__table = []
        self.__rowLength = len(table)

        if self.__rowLength == 0:
            self.__columnLength = 0
        else:
            self.__columnLength = len(table[0])

        for row in table:
            self.__table.extend(row)

    def setNewTable(self, newTable: List[List[Union[int, float, Complex, Quaternion]]]) -> None:
        """
        Reconstructs this matrix with a new table of values

        :param newTable: The new table of values for this
            matrix
        :param rowLength: The new number of rows for this matrix
        :param columnLength: The new number of columns for this matrix
        :return: None
        """

        self.__table = []
        self.__rowLength = len(newTable)

        if self.__rowLength == 0:
            self.__columnLength = 0
        else:
            self.__columnLength = len(newTable[0])

        for row in newTable:
            self.__table.extend(row)

    @staticmethod
    def createMatrixFrom1DList(table: List[Union[int, float, Complex, Quaternion]], rowLength: int, columnLength: int) -> Matrix:
        mat = Matrix([[]])
        mat.__table = table
        mat.__rowLength = rowLength
        mat.__columnLength = columnLength

        return mat

    def __len__(self) -> int:
        return self.rowLength * self.columnLength

    @property
    def rowLength(self) -> int:
        """
        Returns the number of rows that this matrix
        has

        :return: The number of rows that this matrix
            has
        """

        return self.__rowLength

    @property
    def columnLength(self) -> int:
        """
        Returns the number of columns that this
        matrix has

        :return: The number of columns that this
            matrix has
        """

        return self.__columnLength

    def equalDimensions(self, matrix: Matrix) -> bool:
        """
        Checks if two matrices have the same number
        of rows and the same number of columns

        :param matrix: The matrix to be compared with
            this matrix
        :return: True if this matrix has the same dimensions
            as the given matrix, False otherwise
        """

        return self.rowLength == matrix.rowLength and self.columnLength == matrix.columnLength

    def multipliable(self, matrix: Matrix) -> bool:
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

    def divisible(self, matrix: Matrix) -> bool:
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
    def isSquare(self) -> bool:
        """
        Checks if the number of rows that this matrix has is equal
        to the number of columns it has

        :return: True if the number of rows that this matrix has is
            equal to the number of columns it has
        """

        return self.rowLength == self.columnLength

    def __getitem__(self, coordinates: Tuple[int, int]) -> Union[int, float, Complex, Quaternion]:
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

    def __setitem__(self, coordinates: Tuple[int, int], value: Union[int, float, Complex, Quaternion]) -> None:
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

    def __contains__(self, searchValue: Union[int, float, Complex, Quaternion]) -> bool:
        """
        Checks if this matrix contains a certain value

        :param searchValue: The value to be searched
            for
        :return: True if this matrix contains the
            given value, False otherwise
        """

        return searchValue in self.__table

    @staticmethod
    def identity(size: int) -> Matrix:
        """
        Returns a square identity matrix of the
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

        return Matrix.createMatrixFrom1DList(table, size, size)

    def conjugate(self) -> Matrix:
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

        return Matrix.createMatrixFrom1DList(newTable, self.rowLength, self.columnLength)

    @property
    def determinant(self) -> float:
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
    def __determinant(table: List[Union[int, float, Complex, Quaternion]], size: int) -> float:
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

    def inverse(self) -> Matrix:
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

    def transpose(self) -> Matrix:
        """
        Returns the transpose of this matrix

        :return: The transpose of this matrix
        """

        table = []

        for colIndex in range(self.columnLength):
            for rowIndex in range(self.rowLength):
                table.append(self[(rowIndex, colIndex)])

        return Matrix.createMatrixFrom1DList(table, self.columnLength, self.rowLength)

    def to2DList(self) -> List[List[Union[int, float, Complex, Quaternion]]]:
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

    def __floor__(self) -> Matrix:
        """
        Rounds all elements of this matrix
        down

        :return: A new matrix with each element
            of this matrix rounded down
        """

        table = []

        for value in self:
            table.append(value.__floor__())

        return Matrix.createMatrixFrom1DList(table, self.rowLength, self.columnLength)

    def __ceil__(self) -> Matrix:
        """
        Rounds all elements of this matrix
        up

        :return: A new matrix with each element
            of this matrix rounded up
        """

        table = []

        for value in self:
            table.append(value.__ceil__())

        return Matrix.createMatrixFrom1DList(table, self.rowLength, self.columnLength)

    def __round__(self, numDecimals: Optional[int]=None) -> Matrix:
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

        return Matrix.createMatrixFrom1DList(table, self.rowLength, self.columnLength)

    def __iter__(self) -> Iterable[Union[int, float, Complex, Quaternion]]:
        """
        Returns a row-by-row iterator over the elements
        of this matrix

        :return: A row-by-row iterator over the elements
            of this matrix
        """

        return iter(self.__table)

    def __copy__(self: Matrix) -> Matrix:
        """
        Creates a shallow copy of this matrix

        :return: A shallow copy of this matrix
        """

        return Matrix.createMatrixFrom1DList(self.__table, self.rowLength, self.columnLength)

    def __deepcopy__(self, memodict: dict={}) -> Matrix:
        """
        Creates a deep copy of this matrix

        :param memodict: N/A
        :return: A deep copy of this matrix
        """

        return Matrix.createMatrixFrom1DList(copy(self.__table), self.rowLength, self.columnLength)

    def __hash__(self) -> int:
        """
        Computes a hash code for this matrix

        :return: A hash code for this matrix
        """

        hashCode = 0
        MODIFIER = 31

        for value in self:
            hashCode += MODIFIER * hash(value)

        return hashCode

    def __str__(self) -> str:
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
