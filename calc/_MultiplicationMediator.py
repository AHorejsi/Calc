from typing import Union
from math import nan
from copy import deepcopy
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __vectorTimesMatrix(leftVector: Vector, rightMatrix: Matrix) -> Matrix:
    """
    Multiplies the given vector by the given matrix

    :param leftVector: The vector on the left side of
        the multiplication sign
    :param rightMatrix: The matrix on the right side of
        the multiplication sign
    :return: The product of the given vector and the given
        matrix
    :raises ArithmeticError: Raised on the dimensions of the
        given vector is not equal to the number of columns the
        given matrix
    """

    if len(leftVector) != rightMatrix.columnLength:
        raise ArithmeticError("Dimensions of the Vector must be the same as the column length of the Matrix")

    table = []

    for colIndex in range(rightMatrix.columnLength):
        value = 0.0

        for rowIndex in range(rightMatrix.rowLength):
            value += rightMatrix[(rowIndex, colIndex)] * leftVector[rowIndex]

        table.append(value)

    return Matrix.createMatrixFrom1DList(table, 1, rightMatrix.columnLength)


def __matrixTimesScalar(leftMatrix: Matrix, rightScalar: Union[int, float, Complex, Quaternion]) -> Matrix:
    """
    Multiplies the given matrix by the given scalar value. Scalar values
    include ints, floats, Complex numbers and Quaternions

    :param leftMatrix: The matrix on the left side of the multiplication
        sign
    :param rightScalar: The scalar value on the right side of the
        multiplication sign
    :return: The product of the given matrix and the given scalar value
    """

    newMatrix = deepcopy(leftMatrix)

    for rowIndex in range(leftMatrix.rowLength):
        for columnIndex in range(leftMatrix.columnLength):
            newMatrix[(rowIndex, columnIndex)] *= rightScalar

    return newMatrix


def __matrixTimesVector(leftMatrix: Matrix, rightVector: Vector) -> Matrix:
    """
    Multiplies the given matrix by the given vector

    :param leftMatrix: The matrix on the left side of
        the multiplication sign
    :param rightVector: The vector on the right side
        of the multiplication sign
    :return: The product of the given matrix and the
        given vector
    :raises ArithmeticError: Raised if the dimensions
        of the given vector are not equal to the number
        of rows the given matrix has
    """

    if leftMatrix.rowLength != len(rightVector):
        raise ArithmeticError("The Matrix must have the same row length as the Vector's dimensions")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        value = 0.0

        for colIndex in range(leftMatrix.columnLength):
            value += leftMatrix[(rowIndex, colIndex)] * rightVector[colIndex]

        table.append(value)

    return Matrix.createMatrixFrom1DList(table, leftMatrix.rowLength, 1)


def __matrixTimesMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> Matrix:
    """
    Multiplies the two given matrices together

    :param leftMatrix: The matrix on the left side
        of the multiplication sign
    :param rightMatrix: The matrix on the right side
        of the multiplication sign
    :return: The product of the two given matrices
    :raises ArithmeticError: Raised if the left-side
        matrix does not have the same number of columns
        as the right-side matrix has rows
    """

    if not leftMatrix.multipliable(rightMatrix):
        raise ArithmeticError("Left Matrix must have the same amount of columns and the right Matrix has rows")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        for colIndex in range(rightMatrix.columnLength):
            value = 0.0

            for index in range(leftMatrix.rowLength):
                value += leftMatrix[(rowIndex, index)] * rightMatrix[(index, colIndex)]

            table.append(value)

    return Matrix.createMatrixFrom1DList(table, leftMatrix.rowLength, rightMatrix.columnLength)


multDict = {(int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt * rightQuaternion.real,
                                                                                leftInt * rightQuaternion.imag0,
                                                                                leftInt * rightQuaternion.imag1,
                                                                                leftInt * rightQuaternion.imag2),
            (int, Vector): lambda leftInt, rightVector: Vector([leftInt * value for value in rightVector]),
            (int, Matrix): lambda leftInt, rightMatrix: Matrix.createMatrixFrom1DList(
                    [leftInt * value for value in rightMatrix],
                    rightMatrix.rowLength,
                    rightMatrix.columnLength),
            (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat * rightQuaternion.real,
                                                                                    leftFloat * rightQuaternion.imag0,
                                                                                    leftFloat * rightQuaternion.imag1,
                                                                                    leftFloat * rightQuaternion.imag2),
            (float, Vector): lambda leftFloat, rightVector: Vector([leftFloat * value for value in rightVector]),
            (float, Matrix): lambda leftFloat, rightMatrix: Matrix.createMatrixFrom1DList(
                    [leftFloat * value for value in rightMatrix],
                    rightMatrix.rowLength,
                    rightMatrix.columnLength),
            (complex, Quaternion): lambda leftComplex, rightQuaternion: Quaternion(
                      leftComplex.real * rightQuaternion.real - leftComplex.imag * rightQuaternion.imag0,
                      leftComplex.real * rightQuaternion.imag0 + rightQuaternion.real * leftComplex.imag,
                      leftComplex.real * rightQuaternion.imag1 - leftComplex.imag * rightQuaternion.imag2,
                      leftComplex.real * rightQuaternion.imag2 + leftComplex.imag * rightQuaternion.imag1),
            (complex, Matrix): lambda leftComplex, rightMatrix: Matrix.createMatrixFrom1DList(
                    [leftComplex * value for value in rightMatrix],
                    rightMatrix.rowLength,
                    rightMatrix.columnLength),
            (Quaternion, int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real * rightInt,
                                                                           leftQuaternion.imag0 * rightInt,
                                                                           leftQuaternion.imag1 * rightInt,
                                                                           leftQuaternion.imag2 * rightInt),
            (Quaternion, float): lambda leftQuaternion, rightFloat: Quaternion(leftQuaternion.real * rightFloat,
                                                                               leftQuaternion.imag0 * rightFloat,
                                                                               leftQuaternion.imag1 * rightFloat,
                                                                               leftQuaternion.imag2 * rightFloat),
            (Quaternion, complex): lambda leftQuaternion, rightComplex: Quaternion(
                      leftQuaternion.real * rightComplex.real - leftQuaternion.imag0 * rightComplex.imag,
                      leftQuaternion.real * rightComplex.imag + leftQuaternion.imag0 * rightComplex.real,
                      leftQuaternion.imag1 * rightComplex.real + leftQuaternion.imag2 * rightComplex.imag,
                      -leftQuaternion.imag1 * rightComplex.imag + leftQuaternion.imag2 * rightComplex.real),
            (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(
                      leftQuaternion.real * rightQuaternion.real - leftQuaternion.imag0 * rightQuaternion.imag0 -
                      leftQuaternion.imag1 * rightQuaternion.imag1 - leftQuaternion.imag2 * rightQuaternion.imag2,
                      leftQuaternion.real * rightQuaternion.imag0 + leftQuaternion.imag0 * rightQuaternion.real -
                      leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1,
                      leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag0 * rightQuaternion.imag2 +
                      leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag0,
                      leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag0 * rightQuaternion.imag1 +
                      leftQuaternion.imag1 * rightQuaternion.imag0 + leftQuaternion.imag2 * rightQuaternion.real),
            (Quaternion, Matrix): lambda leftQuaternion, rightMatrix: Matrix.createMatrixFrom1DList(
                    [leftQuaternion * value for value in rightMatrix],
                    rightMatrix.rowLength,
                    rightMatrix.columnLength),
            (Vector, int): lambda leftVector, rightInt: Vector([rightInt * value for value in leftVector]),
            (Vector, float): lambda leftVector, rightFloat: Vector([rightFloat * value for value in leftVector]),
            (Vector, Matrix): __vectorTimesMatrix,
            (Matrix, int): lambda leftMatrix, rightInt: Matrix.createMatrixFrom1DList(
                    [value * rightInt for value in leftMatrix],
                    leftMatrix.rowLength,
                    leftMatrix.columnLength),
            (Matrix, float): lambda leftMatrix, rightFloat: Matrix.createMatrixFrom1DList(
                    [value * rightFloat for value in leftMatrix],
                    leftMatrix.rowLength,
                    leftMatrix.columnLength),
            (Matrix, complex): lambda leftMatrix, rightComplex: Matrix.createMatrixFrom1DList(
                    [value * rightComplex for value in leftMatrix],
                    leftMatrix.rowLength,
                    leftMatrix.columnLength),
            (Matrix, Quaternion): lambda leftMatrix, rightQuaternion: Matrix.createMatrixFrom1DList(
                    [value * rightQuaternion for value in leftMatrix],
                    leftMatrix.rowLength,
                    leftMatrix.columnLength),
            (Matrix, Vector): __matrixTimesVector,
            (Matrix, Matrix): __matrixTimesMatrix}


def doMultiplication(mathEntity1: Union[int, float, MathEntity],
                     mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    """
    Multiplies the two given mathematical entities together.
    If the two mathematical entities cannot be multiplied
    together, nan is returned

    :param mathEntity1: The mathematical entity on the left
        side of the multiplication sign
    :param mathEntity2: The mathematical entity on the right
        side of the multiplication sign
    :return: The product of the two mathematical entities
        if they can be multiplied together. If they cannot
        be multiplied together, nan is returned
    """

    key = (type(mathEntity1), type(mathEntity2))
    operation = multDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
