from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix
from calc.MatrixFunction import expMatrix, logMatrix
from copy import deepcopy


def _multiplication(leftMatrix, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float) or (typeOfOperand is Complex) or (typeOfOperand is Quaternion):
        return _matrixTimesScalar(leftMatrix, rightOperand)
    elif typeOfOperand is Vector:
        return _matrixTimesVector(leftMatrix, rightOperand)
    elif typeOfOperand is Matrix:
        return _matrixTimesMatrix(leftMatrix, rightOperand)

    raise ArithmeticError("(Matrix * " + _typeName(typeOfOperand) + ") is not possible")


def _matrixTimesScalar(leftMatrix, rightScalar):
    table = []

    for value in leftMatrix:
        table.append(rightScalar * value)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def _matrixTimesVector(leftMatrix, rightVector):
    if leftMatrix.rowLength != len(rightVector):
        raise ArithmeticError("The Matrix must have the same row length as the Vector's dimensions")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        value = 0.0

        for colIndex in range(leftMatrix.columnLength):
            value += leftMatrix[rowIndex, colIndex] * rightVector[colIndex]

        table.append(value)

    return Matrix(table, leftMatrix.rowLength, 1)


def _matrixTimesMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.multipliable(rightMatrix):
        raise ArithmeticError("Left Matrix must have the same amount of columns and the right Matrix has rows")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        newRow = []

        for colIndex in range(rightMatrix.columnLength):
            value = __calculateValue(leftMatrix, rightMatrix, rowIndex, colIndex)
            newRow.append(value)

        table.extend(newRow)

    return Matrix(table, leftMatrix.rowLength, rightMatrix.columnLength)


def __calculateValue(leftMatrix, rightMatrix, rowIndex, colIndex):
    value = 0.0

    for index in range(leftMatrix.rowLength):
        value += leftMatrix[rowIndex, index] * rightMatrix[index, colIndex]

    return value


def _division(leftMatrix, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float) or (typeOfOperand is Complex) or (typeOfOperand is Quaternion):
        return _matrixDividedByScalar(leftMatrix, rightOperand)
    elif typeOfOperand is Matrix:
        return _matrixDividedByMatrix(leftMatrix, rightOperand)

    raise ArithmeticError("(Matrix / " + _typeName(typeOfOperand) + ") is not possible")


def _matrixDividedByScalar(leftMatrix, rightScalar):
    return _matrixTimesScalar(leftMatrix, 1 / rightScalar)


def _matrixDividedByMatrix(leftMatrix, rightMatrix):
    return leftMatrix * rightMatrix.inverse()


def _exponent(leftMatrix, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is int:
        return _matrixToPowerOfInt(leftMatrix, rightOperand)
    elif (typeOfOperand is float) or (typeOfOperand is Complex) or (typeOfOperand is Quaternion):
        return _matrixToPowerOfFloat(leftMatrix, rightOperand)
    elif typeOfOperand is Matrix:
        return _matrixToPowerOfMatrix(leftMatrix, rightOperand)


def _matrixToPowerOfInt(leftMatrix, rightInt):
    newMatrix = deepcopy(leftMatrix)

    for iteration in range(rightInt - 1):
        newMatrix *= leftMatrix

    return newMatrix


def _matrixToPowerOfFloat(leftMatrix, rightFloat):
    if rightFloat.is_integer():
        return _matrixToPowerOfInt(rightFloat)
    else:
        return expMatrix(logMatrix(leftMatrix) * rightFloat)


def _matrixToPowerOfMatrix(leftMatrix, rightMatrix):
    result = expMatrix(logMatrix(leftMatrix) * rightMatrix)
    newTable = []

    for rowIndex in range(leftMatrix.rowLength):
        for columnIndex in range(leftMatrix.columnLength):
            if type(result[(rowIndex, columnIndex)]) is complex:
                com = Complex.fromBuiltInComplex(result[(rowIndex, columnIndex)])
                newTable.append(com)

    return Matrix(newTable, leftMatrix.rowLength, leftMatrix.columnLength)


def _equality(leftMatrix, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is Matrix:
        return _matrixEqualsMatrix(leftMatrix, rightOperand)

    return False


def _matrixEqualsMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.equalDimensions(rightMatrix):
        return False

    for rowIndex in range(leftMatrix.rowLength):
        for colIndex in range(leftMatrix.columnLength):
            if leftMatrix[rowIndex, colIndex] != rightMatrix[rowIndex, colIndex]:
                return False

    return True
