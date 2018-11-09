from cal.Vector import Vector
from cal.Quaternion import Quaternion
from cal.Matrix import Matrix


def addition(leftOperand, rightOperand):
    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if typeOfLeft is Vector:
        # The below "if" statements indicate what types can be added to Vectors

        if typeOfRight is Vector:
            return vectorPlusVector(leftOperand, rightOperand)
    elif typeOfLeft is Quaternion:
        # The below "if" statements indicate what types can be added to Quaternions

        if (typeOfRight is int) or (typeOfRight is float):
            return quaternionPlusReal(leftOperand, rightOperand)
        elif typeOfRight is complex:
            return quaternionPlusComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionPlusQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be added to Matrices

        if typeOfRight is Matrix:
            return matrixPlusMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " + " + str(typeOfRight) + " is not possible")


def vectorPlusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be added together")

    point = []

    for value1, value2 in zip(leftVector, rightVector):
        point.append(value1 + value2)

    return Vector(point)


def quaternionPlusReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real + rightReal,
                      leftQuaternion.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionPlusComplex(leftQuaternion, rightComplex):
    return Quaternion(leftQuaternion.real + rightComplex.real,
                      leftQuaternion.imag + rightComplex.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionPlusQuaternion(leftQuaternion, rightQuaternion):
    return Quaternion(leftQuaternion.real + rightQuaternion.real,
                      leftQuaternion.imag + rightQuaternion.imag,
                      leftQuaternion.imag1 + rightQuaternion.imag1,
                      leftQuaternion.imag2 + rightQuaternion.imag2)


def matrixPlusMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be added together")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        newRow = []

        for colIndex in range(leftMatrix.columnLength):
            result = addition(leftMatrix[rowIndex, colIndex], rightMatrix[rowIndex, colIndex])
            newRow.append(result)

        table.extend(newRow)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def subtraction(leftOperand, rightOperand):
    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if typeOfLeft is Vector:
        # The below "if" statements indicate what types can be subtracted from Vectors

        if typeOfRight is Vector:
            return vectorMinusVector(leftOperand, rightOperand)
    elif typeOfLeft is Quaternion:
        # The below "if" statements indicate what types can be subtracted from Quaternions

        if (typeOfRight is int) or (typeOfRight is float):
            return quaternionMinusReal(leftOperand, rightOperand)
        elif typeOfRight is complex:
            return quaternionMinusComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionMinusQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be subtracted from Matrices

        if typeOfRight is Matrix:
            return matrixMinusMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " - " + str(typeOfRight) + " is not possible")


def vectorMinusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be subtracted from each other")

    point = []

    for value1, value2 in zip(leftVector, rightVector):
        point.append(value1 - value2)

    return Vector(point)


def quaternionMinusReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real - rightReal,
                      leftQuaternion.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionMinusComplex(leftQuaternion, rightComplex):
    return Quaternion(leftQuaternion.real - rightComplex.real,
                      leftQuaternion.imag - rightComplex.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionMinusQuaternion(leftQuaternion, rightQuaternion):
    return Quaternion(leftQuaternion.real - rightQuaternion.real,
                      leftQuaternion.imag - rightQuaternion.imag,
                      leftQuaternion.imag1 - rightQuaternion.imag1,
                      leftQuaternion.imag2 - rightQuaternion.imag2)


def matrixMinusMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be subtracted from each other")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        newRow = []

        for colIndex in range(leftMatrix.columnLength):
            result = subtraction(leftMatrix[rowIndex, colIndex], rightMatrix[rowIndex, colIndex])
            newRow.append(result)

        table.extend(newRow)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def multiplication(leftOperand, rightOperand):
    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if typeOfLeft is Vector:
        # The below "if" statements indicate what types can be multiplied to Vectors

        if (typeOfRight is int) or (typeOfRight is float):
            return vectorTimesReal(leftOperand, rightOperand)
    elif typeOfLeft is Quaternion:
        # The below "if" statements indicate what types can be multiplied to Quaternions

        if (typeOfRight is int) or (typeOfRight is float):
            return quaternionTimesReal(leftOperand, rightOperand)
        elif typeOfRight is complex:
            return quaternionTimesComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionTimesQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be multiplied to Matrices

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex) or (typeOfRight is Quaternion):
            return matrixTimesScalar(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixTimesMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " * " + str(typeOfRight) + " is not possible")


def vectorTimesReal(leftVector, rightReal):
    point = []

    for value in leftVector:
        point.append(value * rightReal)

    return Vector(point)


def quaternionTimesReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real * rightReal,
                      leftQuaternion.imag * rightReal,
                      leftQuaternion.imag1 * rightReal,
                      leftQuaternion.imag2 * rightReal)


def quaternionTimesComplex(leftQuaternion, rightComplex):
    return Quaternion(leftQuaternion.real * rightComplex.real - leftQuaternion.imag * rightComplex.imag,
                      leftQuaternion.real * rightComplex.imag + leftQuaternion.imag * rightComplex.real,
                      leftQuaternion.imag1 * rightComplex.real + leftQuaternion.imag2 * rightComplex.imag,
                      -leftQuaternion.imag1 * rightComplex.imag + leftQuaternion.imag2 * rightComplex.real)


def quaternionTimesQuaternion(leftQuaterion, rightQuaternion):
    return Quaternion(leftQuaterion.real * rightQuaternion.real - leftQuaterion.imag * rightQuaternion.imag -
                      leftQuaterion.imag1 * rightQuaternion.imag1 - leftQuaterion.imag2 * rightQuaternion.imag2,
                      leftQuaterion.real * rightQuaternion.imag + leftQuaterion.imag * rightQuaternion.real -
                      leftQuaterion.imag1 * rightQuaternion.imag2 + leftQuaterion.imag2 * rightQuaternion.imag1,
                      leftQuaterion.real * rightQuaternion.imag1 + leftQuaterion.imag * rightQuaternion.imag2 +
                      leftQuaterion.imag1 * rightQuaternion.real - leftQuaterion.imag2 * rightQuaternion.imag,
                      leftQuaterion.real * rightQuaternion.imag2 - leftQuaterion.imag * rightQuaternion.imag1 +
                      leftQuaterion.imag1 * rightQuaternion.imag + leftQuaterion.imag2 * rightQuaternion.real)


def matrixTimesScalar(leftMatrix, rightScalar):
    table = []

    for rowIndex in range(leftMatrix.rowLength):
        newRow = []

        for colIndex in range(leftMatrix.columnLength):
            result = multiplication(leftMatrix[rowIndex, colIndex], rightScalar)
            newRow.append(result)

        table.extend(newRow)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def matrixTimesMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.multipliable(rightMatrix):
        raise ArithmeticError("Left Matrix must have the same amount of columns and the right Matrix has rows")

    table = []

    for rowIndex in range(leftMatrix.rowLength):
        newRow = []

        for colIndex in range(rightMatrix.columnLength):
            value = _calculateValue(leftMatrix, rightMatrix, rowIndex, colIndex)
            newRow.append(value)

        table.extend(newRow)

    return Matrix(table, leftMatrix.rowLength, rightMatrix.columnLength)


def _calculateValue(leftMatrix, rightMatrix, rowIndex, colIndex):
    value = 0.0

    for index in range(leftMatrix.rowLength):
        value += leftMatrix[rowIndex, index] * rightMatrix[index, colIndex]

    return value


def division(leftOperand, rightOperand):
    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if typeOfLeft is Vector:
        # The below "if" statements indicate what types can be divided from Vectors

        if (typeOfRight is int) or (typeOfRight is float):
            return vectorDividedByReal(leftOperand, rightOperand)
    elif typeOfLeft is Quaternion:
        # The below "if" statements indicate what types can be divided from Quaternions

        if (typeOfRight is int) or (typeOfRight is float):
            return quaternionDividedByReal(leftOperand, rightOperand)
        elif typeOfRight is complex:
            return quaternionDividedByComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be divided from Matrices

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex) or (typeOfRight is Quaternion):
            return matrixDividedByScalar(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixDividedByMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " / " + str(typeOfRight) + " is not possible")


def vectorDividedByReal(leftVector, rightReal):
    return vectorTimesReal(leftVector, 1 / rightReal)


def quaternionDividedByReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real / rightReal,
                      leftQuaternion.imag / rightReal,
                      leftQuaternion.imag1 / rightReal,
                      leftQuaternion.imag2 / rightReal)


def quaternionDividedByComplex(leftQuaternion, rightComplex):
    conjugateOfRightComplex = rightComplex.conjugate()
    numerator = quaternionTimesComplex(leftQuaternion, conjugateOfRightComplex)
    denominator = rightComplex * conjugateOfRightComplex
    result = quaternionDividedByReal(numerator, denominator)

    return result


def quaternionDividedByQuaternion(leftQuaternion, rightQuaternion):
    absoluteValueOfLeft = abs(leftQuaternion)

    realOfResult = leftQuaternion.real * rightQuaternion.real + leftQuaternion.imag * rightQuaternion.imag + \
                   leftQuaternion.imag1 * rightQuaternion.imag1 + leftQuaternion.imag2 * rightQuaternion.imag2
    imagOfResult = leftQuaternion.real * rightQuaternion.imag - leftQuaternion.imag * rightQuaternion.real - \
                   leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1
    imag1OfResult = leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag * rightQuaternion.imag2 - \
                    leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag
    imag2OfResult = leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag * rightQuaternion.imag1 + \
                    leftQuaternion.imag1 * rightQuaternion.imag - leftQuaternion.imag2 * rightQuaternion.real

    return Quaternion(realOfResult / absoluteValueOfLeft,
                      imagOfResult / absoluteValueOfLeft,
                      imag1OfResult / absoluteValueOfLeft,
                      imag2OfResult / absoluteValueOfLeft)


def matrixDividedByScalar(leftMatrix, rightScalar):
    return matrixTimesScalar(leftMatrix, 1 / rightScalar)


def matrixDividedByMatrix(leftMatrix, rightMatrix):
    return matrixTimesMatrix(leftMatrix, rightMatrix.inverse())


def negation(operand):
    typeOfOperand = type(operand)

    if typeOfOperand is Vector:
        return negateVector(operand)
    elif typeOfOperand is Quaternion:
        return negateQuaternion(operand)
    elif typeOfOperand is Matrix:
        return negateMatrix(operand)

    raise TypeError(str(typeOfOperand) + "s do not have a negation")


def negateVector(vector):
    return vectorTimesReal(vector, -1)


def negateQuaternion(quaternion):
    return quaternionTimesReal(quaternion, -1)


def negateMatrix(matrix):
    return matrixTimesScalar(matrix, -1)
