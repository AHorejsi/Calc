from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __vectorTimesMatrix(leftVector: Vector, rightMatrix: Matrix) -> Matrix:
    if len(leftVector) != rightMatrix.columnLength:
        raise ArithmeticError("Dimensions of the Vector must be the same as the column length of the Matrix")

    table = []

    for colIndex in range(rightMatrix.columnLength):
        value = 0.0

        for rowIndex in range(rightMatrix.rowLength):
            value += rightMatrix[rowIndex, colIndex] * leftVector[rowIndex]

        table.append(value)

    return Matrix.createMatrixFrom1DList(table, 1, rightMatrix.columnLength)


def __matrixTimesScalar(leftMatrix: Matrix, rightReal: Union[int, float, Complex, Quaternion]) -> Matrix:
    newMatrix = deepcopy(leftMatrix)

    for rowIndex in range(leftMatrix.rowLength):
        for columnIndex in range(leftMatrix.columnLength):
            newMatrix[(rowIndex, columnIndex)] *= rightReal

    return newMatrix


def __matrixTimesVector(leftMatrix: Matrix, rightVector: Vector) -> Matrix:
    if leftMatrix.rowLength != len(rightVector):
        raise ArithmeticError("The Matrix must have the same row length as the Vector's dimensions")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        value = 0.0

        for colIndex in range(leftMatrix.columnLength):
            value += leftMatrix[rowIndex, colIndex] * rightVector[colIndex]

        table.append(value)

    return Matrix.createMatrixFrom1DList(table, leftMatrix.rowLength, 1)


def __matrixTimesMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> Matrix:
    if not leftMatrix.multipliable(rightMatrix):
        raise ArithmeticError("Left Matrix must have the same amount of columns and the right Matrix has rows")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        newRow = []

        for colIndex in range(rightMatrix.columnLength):
            value = 0.0

            for index in range(leftMatrix.rowLength):
                value += leftMatrix[rowIndex, index] * rightMatrix[index, colIndex]

            newRow.append(value)

        table.extend(newRow)

    return Matrix.createMatrixFrom1DList(table, leftMatrix.rowLength, rightMatrix.columnLength)


multDict = {(int, Complex): lambda leftInt, rightComplex: Complex(leftInt * rightComplex.real,
                                                                       leftInt * rightComplex.imag0),
            (int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt * rightQuaternion.real,
                                                                                leftInt * rightQuaternion.imag0,
                                                                                leftInt * rightQuaternion.imag1,
                                                                                leftInt * rightQuaternion.imag2),
            (int, Vector): lambda leftInt, rightVector: Vector([leftInt * value for value in rightVector]),
            (int, Matrix): lambda leftInt, rightMatrix: Matrix.createMatrixFrom1DList([leftInt * value for value in rightMatrix],
                                                                                      rightMatrix.rowLength,
                                                                                      rightMatrix.columnLength),
            (float, Complex): lambda leftInt, rightComplex: Complex(leftInt * rightComplex.real,
                                                                         leftInt * rightComplex.imag0),
            (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat * rightQuaternion.real,
                                                                                    leftFloat * rightQuaternion.imag0,
                                                                                    leftFloat * rightQuaternion.imag1,
                                                                                    leftFloat * rightQuaternion.imag2),
            (float, Vector): lambda leftFloat, rightVector: Vector([leftFloat * value for value in rightVector]),
            (float, Matrix): lambda leftFloat, rightMatrix: Matrix.createMatrixFrom1DList([leftFloat * value for value in rightMatrix],
                                                                                          rightMatrix.rowLength,
                                                                                          rightMatrix.columnLength),
            (Complex, int): lambda leftComplex, rightInt: Complex(leftComplex.real * rightInt,
                                                                  leftComplex.imag0 * rightInt),
            (Complex, float): lambda leftComplex, rightFloat: Complex(leftComplex.real * rightFloat,
                                                                      leftComplex.imag0 * rightFloat),
            (Complex, Complex): lambda leftComplex, rightComplex: Complex(
                   leftComplex.real * rightComplex.real - leftComplex.imag0 * rightComplex.imag0,
                   leftComplex.real * rightComplex.imag0 + leftComplex.imag0 * rightComplex.real),
            (Complex, Quaternion): lambda leftComplex, rightQuaternion: Quaternion(
                      leftComplex.real * rightQuaternion.real - leftComplex.imag0 * rightQuaternion.imag0,
                      leftComplex.real * rightQuaternion.imag0 + rightQuaternion.real * leftComplex.imag0,
                      leftComplex.real * rightQuaternion.imag1 - leftComplex.imag0 * rightQuaternion.imag2,
                      leftComplex.real * rightQuaternion.imag2 + leftComplex.imag0 * rightQuaternion.imag1),
            (Complex, Matrix): lambda leftComplex, rightMatrix: Matrix.createMatrixFrom1DList([leftComplex * value for value in rightMatrix],
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
            (Quaternion, Complex): lambda leftQuaternion, rightComplex: Quaternion(
                      leftQuaternion.real * rightComplex.real - leftQuaternion.imag0 * rightComplex.imag0,
                      leftQuaternion.real * rightComplex.imag0 + leftQuaternion.imag0 * rightComplex.real,
                      leftQuaternion.imag1 * rightComplex.real + leftQuaternion.imag2 * rightComplex.imag0,
                      -leftQuaternion.imag1 * rightComplex.imag0 + leftQuaternion.imag2 * rightComplex.real),
            (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(
                      leftQuaternion.real * rightQuaternion.real - leftQuaternion.imag0 * rightQuaternion.imag0 -
                      leftQuaternion.imag1 * rightQuaternion.imag1 - leftQuaternion.imag2 * rightQuaternion.imag2,
                      leftQuaternion.real * rightQuaternion.imag0 + leftQuaternion.imag0 * rightQuaternion.real -
                      leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1,
                      leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag0 * rightQuaternion.imag2 +
                      leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag0,
                      leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag0 * rightQuaternion.imag1 +
                      leftQuaternion.imag1 * rightQuaternion.imag0 + leftQuaternion.imag2 * rightQuaternion.real),
            (Quaternion, Matrix): lambda leftQuaternion, rightMatrix: Matrix.createMatrixFrom1DList([leftQuaternion * value for value in rightMatrix],
                                                                                                    rightMatrix.rowLength,
                                                                                                    rightMatrix.columnLength),
            (Vector, int): lambda leftVector, rightInt: Vector([rightInt * value for value in leftVector]),
            (Vector, float): lambda leftVector, rightFloat: Vector([rightFloat * value for value in leftVector]),
            (Vector, Matrix): __vectorTimesMatrix,
            (Matrix, int): lambda leftMatrix, rightInt: Matrix.createMatrixFrom1DList([value * rightInt for value in leftMatrix],
                                                                                      leftMatrix.rowLength,
                                                                                      leftMatrix.columnLength),
            (Matrix, float): lambda leftMatrix, rightFloat: Matrix.createMatrixFrom1DList([value * rightFloat for value in leftMatrix],
                                                                                          leftMatrix.rowLength,
                                                                                          leftMatrix.columnLength),
            (Matrix, Complex): lambda leftMatrix, rightComplex: Matrix.createMatrixFrom1DList([value * rightComplex for value in leftMatrix],
                                                                                              leftMatrix.rowLength,
                                                                                              leftMatrix.columnLength),
            (Matrix, Quaternion): lambda leftMatrix, rightQuaternion: Matrix.createMatrixFrom1DList([value * rightQuaternion for value in leftMatrix],
                                                                                                    leftMatrix.rowLength,
                                                                                                    leftMatrix.columnLength),
            (Matrix, Vector): __matrixTimesVector,
            (Matrix, Matrix): __matrixTimesMatrix}


def doMultiplication(mathEntity1: Union[int, float, MathEntity],
                     mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    key = (type(mathEntity1), type(mathEntity2))
    operation = multDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
