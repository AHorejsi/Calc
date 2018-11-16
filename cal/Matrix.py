from scipy.linalg import inv, det
from cal.MathEntity import MathEntity


class Matrix(MathEntity):
    """
    Instances of this class represent Matrices. All instances of
    this class cannot be jagged
    """

    def __init__(self, table, rowLength=None, columnLength=None):
        """
        Constructs a Matrix. If a 2D list is provided, then rowLength and columnLength parameters
        should be ignored. If a 1D list is provided, then rowLength and columnLength must be
        given values so that the dimensions of the Matrix can be known

        :param table: A 1D or 2D list of numbers that this Matrix will contain
        :param rowLength: The number of rows for this Matrix. Should only be
            given a value if the "table" parameter is a 1D list
        :param columnLength: The number of columns for this Matrix. Should only be
            given a value if the "table" parameter is a 1D list
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

    @property
    def rowLength(self):
        """
        Returns the number of rows that this Matrix has

        :return: The number of rows that this Matrix has
        """

        return self.__rowLength

    @property
    def columnLength(self):
        """
        Returns the number of columns that this Matrix has

        :return: The number of columns that this Matrix has
        """

        return self.__columnLength

    def equalDimensions(self, matrix):
        """
        Checks if two Matrices have the same dimensions

        :param matrix: Another Matrix
        :return: True if both Matrices have the same dimensions, False otherwise
        """

        return self.rowLength == matrix.rowLength and self.columnLength == matrix.columnLength

    def multipliable(self, matrix):
        """
        Checks if two Matrices can be multiplied together. Note that which
        Matrix is on the left and which is on the right has an effect on whether
        multiplication is possible

        :param matrix: The Matrix to be checked for if it can be multiplied
            to this Matrix
        :return: True if (self * matrix) is possible, False otherwise
        """

        return self.columnLength == matrix.rowLength

    def divisible(self, matrix):
        """
        Checks if this Matrix can be divided by another Matrix. Note that which
        Matrix is on the left and which is on the right has an effect on whether
        division is possible

        :param matrix: The Matrix to be checked for if it can be divided
            from this Matrix
        :return: True if (self / matrix) is possible, False otherwise
        """

        return self.multipliable(matrix) and matrix.isSquare

    @property
    def isSquare(self):
        """
        Checks if this Matrix is square. A square Matrix has the same number of
        rows as it has columns

        :return: True if this Matrix has the same number of rows and columns
        """

        return self.rowLength == self.columnLength

    def __getitem__(self, coordinates):
        """
        Returns an element of this Matrix

        :param coordinates: A tuple containing the row and column indices
            of the element to be retrieved
        :return: The element in this Matrix that is located at the given
            row and column indices
        :exception Exception: Raised when the given row and column indices
            are outside of the bounds of this Matrix
        """

        if coordinates[0] < 0 or coordinates[0] >= self.rowLength or \
           coordinates[1] < 0 or coordinates[1] >= self.columnLength:
            raise Exception("Invalid indices")

        return self.__table[coordinates[0] * self.columnLength + coordinates[1]]

    def __setitem__(self, coordinates, value):
        """
        Swaps out one of the elements of this Matrix with another element

        :param coordinates: The row and column indices of the element to be
            changed
        :param value: The new value to be placed into the given position
        :return: None
        :exception Exception: Raised when the given row and column indices
            are outside of the bounds of this Matrix
        """

        if coordinates[0] < 0 or coordinates[0] >= self.rowLength or \
           coordinates[1] < 0 or coordinates[1] >= self.columnLength:
            raise Exception("Invalid indices")

        self.__table[coordinates[0] * self.columnLength + coordinates[1]] = value

    def __contains__(self, searchValue):
        """
        Checks if this Matrix contains a given value

        :param searchValue: The value to be searched for
        :return: True if this Matrix contains the provided value, False otherwise
        """

        for value in self:
            if value == searchValue:
                return True

        return False

    @property
    def determinant(self):
        """
        Calculates the determinant of this Matrix

        :return: The determinant of this Matrix
        :exception ArithmeticError: Raised if this Matrix
            is not square
        """

        if not self.isSquare:
            raise ArithmeticError("Only square Matrices have determinants")

        table = []

        for rowIndex in range(self.rowLength):
            newRow = []

            for colIndex in range(self.columnLength):
                newRow.append(self[rowIndex, colIndex])

            table.append(newRow)

        return det(table, check_finite=False)

    def inverse(self):
        """
        Calculates the inverse of this Matrix

        :return: The inverse of this Matrix
        :exception ArithmeticError: Raised if this Matrix is not square
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

    def conjugation(self):
        """
        Returns this Matrix with all nonreal numbers replaced with their conjugates.
        If this Matrix has no nonreal numbers, then a shallow copy of this Matrix
        is returned

        :return: This Matrix with all nonreal numbers replaced with their conjugates
        """

        table = []

        for value in self:
            if hasattr(value, "conjugate"):
                table.append(value.conjugate())
            else:
                table.append(value)

        return Matrix(table, self.rowLength, self.columnLength)

    def transpose(self):
        """
        Returns the transpose of this Matrix

        :return: The transpose of this Matrix
        """

        table = []

        for colIndex in range(self.rowLength):
            for rowIndex in range(self.columnLength):
                table.append(self[rowIndex, colIndex])

        return Matrix(table, self.rowLength, self.columnLength)

    def to2DList(self):
        """
        Converts this Matrix to a 2D list

        :return: A 2D list with the same values as this Matrix
        """

        table = []

        for rowIndex in range(self.rowLength):
            row = []

            for colIndex in range(self.columnLength):
                row.append(self[rowIndex, colIndex])

            table.append(row)

        return table


    def __iter__(self):
        """
        Returns an iterator over the elements of this Matrix

        :return: An iterator over the elements of this Matrix
        """

        return self.__table.__iter__()

    def __hash__(self):
        """
        Calculates a hash code for this Matrix

        :return: Calculates a hash code for this Matrix
        """

        hashCode = 0
        modifier = 31

        for value in self:
            hashCode += modifier * hash(value)

        return hashCode

    def __str__(self):
        """
        Creates a string representation of this Matrix

        :return: A string representation of this Matrix
        """

        strRep = ""
        index = 0

        while index < len(self.__table):
            strRep += str(self.__table[index : index + self.columnLength]) + "\n"
            index += self.columnLength

        return strRep

    def __repr__(self):
        """
        Creates a string representation of this Matrix

        :return: A string representation of this Matrix
        """

        return self.__str__()
