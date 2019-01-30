from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def _typeName(type):
    typeStr = str(type)
    index = len(typeStr) - 1

    while index >= 0:
        if typeStr[index] == '.':
            start = index
        if typeStr[index] == '\'':
            end = index
            break

        index -= 1

    return typeStr[start : end]


def _addition(leftMatrix, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is Matrix:
        return _matrixPlusMatrix(leftMatrix, rightOperand)

    raise ArithmeticError("(Matrix + " + _typeName(typeOfOperand) + ") is not possible")


def _matrixPlusMatrix(leftMatrix, rightMatrix):
    table = []

    for leftValue, rightValue in zip(leftMatrix, rightMatrix):
        table.append(leftValue + rightValue)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def _subtraction(leftMatrix, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is Matrix:
        return _matrixMinusMatrix(leftMatrix, rightOperand)

    raise ArithmeticError("(Matrix - " + _typeName(typeOfOperand) + ") is not possible")


def _matrixMinusMatrix(leftMatrix, rightMatrix):
    table = []

    for leftValue, rightValue in zip(leftMatrix, rightMatrix):
        table.append(leftValue - rightValue)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


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
