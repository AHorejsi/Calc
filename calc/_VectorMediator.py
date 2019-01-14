from calc.Vector import Vector
from calc.Matrix import Matrix


def _addition(leftVector, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is Vector:
        return _vectorPlusVector(leftVector, rightOperand)


def _vectorPlusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be added together")

    point = []

    for leftValue, rightValue in zip(leftVector, rightVector):
        point.append(leftValue + rightValue)

    return Vector(point)


def _subtraction(leftVector, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is Vector:
        return _vectorMinusVector(leftVector, rightOperand)


def _vectorMinusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be subtracted from each other")

    point = []

    for leftValue, rightValue in zip(leftVector, rightVector):
        point.append(leftVector - rightValue)

    return Vector(point)


def _multiplication(leftVector, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _vectorTimesReal(leftVector, rightOperand)
    elif typeOfOperand is Matrix:
        return _vectorTimesMatrix(leftVector, rightOperand)


def _vectorTimesReal(leftVector, rightReal):
    point = []

    for value in leftVector:
        point.append(value * rightReal)

    return Vector(point)


def _vectorTimesMatrix(leftVector, rightMatrix):
    if len(leftVector) != rightMatrix.columnLength:
        raise ArithmeticError("Dimensions of the Vector must be the same as the column length of the Matrix")

    table = []

    for colIndex in range(rightMatrix.columnLength):
        value = 0.0

        for rowIndex in range(rightMatrix.rowLength):
            value += rightMatrix[rowIndex, colIndex] * leftVector[rowIndex]

        table.append(value)

    return Matrix(table, 1, rightMatrix.columnLength)


def _division(leftVector, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _vectorDividedByReal(leftVector, rightOperand)


def _vectorDividedByReal(leftVector, rightReal):
    return _vectorTimesReal(leftVector, 1 / rightReal)


def _equality(leftVector, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is Vector:
        return _vectorEqualsVector(leftVector, rightOperand)

    return False


def _vectorEqualsVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        return False

    for leftValue, rightValue in zip(leftVector, rightVector):
        if leftValue != rightValue:
            return False

    return True
