from cal.Vector import Vector
from cal.Quaternion import Quaternion
from cal.Matrix import Matrix


def addition(leftOperand, rightOperand):
    """
    Handles all addition operations between two mathematical entities

    :param leftOperand: The entity to the left of the operator
    :param rightOperand: The entity to the right of the operator
    :return: The sum of the left and right operands
    :exception TypeError: Raised if (leftOperand + rightOperand) is not possible
    :exception ArithmeticError: Raised if the expression is valid, but some mathematical
        rule prevents the operation from being possible
    """

    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if (typeOfLeft is int) or (typeOfLeft is float):
        # The below "if" statements indicate what types can be added to real numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand + rightOperand
        elif typeOfRight is Quaternion:
            return quaternionPlusReal(rightOperand, leftOperand)
    elif typeOfLeft is complex:
        # The below "if" statements indicate what types can be added to Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand + rightOperand
        elif typeOfRight is Quaternion:
            return quaternionPlusComplex(rightOperand, leftOperand)
    elif typeOfLeft is Vector:
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
    """
    Adds to Vectors together

    :param leftVector: The Vector on the left side of the operator
    :param rightVector: The Vector on the right side of the operator
    :return: The sum of the two given Vectors
    :exception ArithmeticError: Raised if the two given Vectors do not
        have the same dimensions
    """

    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be added together")

    point = []

    for value1, value2 in zip(leftVector, rightVector):
        point.append(value1 + value2)

    return Vector(point)


def quaternionPlusReal(leftQuaternion, rightReal):
    """
    Calculates the sum of the given Quaternion and the given real number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The sum of the given Quaternion and the given real number
    """

    return Quaternion(leftQuaternion.real + rightReal,
                      leftQuaternion.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionPlusComplex(leftQuaternion, rightComplex):
    """
    Calculates the sum of the given Quaternion and the given complex number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The sum of the given Quaternion and the given complex number
    """

    return Quaternion(leftQuaternion.real + rightComplex.real,
                      leftQuaternion.imag + rightComplex.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionPlusQuaternion(leftQuaternion, rightQuaternion):
    """
    Calculates the sum of the two given Quaternions

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The sum of the two given Quaternions
    """

    return Quaternion(leftQuaternion.real + rightQuaternion.real,
                      leftQuaternion.imag + rightQuaternion.imag,
                      leftQuaternion.imag1 + rightQuaternion.imag1,
                      leftQuaternion.imag2 + rightQuaternion.imag2)


def matrixPlusMatrix(leftMatrix, rightMatrix):
    """
    Calculates the sum of the two given Matrices

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightMatrix: The Matrix on the right side of the operator
    :return: The sum of the two given Matrices
    :exception ArithmeticError: Raised if the two given Matrices
    do not have the same dimensions
    """

    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be added together")

    table = []

    for value1, value2 in zip(leftMatrix, rightMatrix):
        result = addition(value1, value2)
        table.append(result)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def subtraction(leftOperand, rightOperand):
    """
    Handles all of the subtraction operations between two mathematical entities

    :param leftOperand: The entity on the left side of the operator
    :param rightOperand: The entity on the right side of the operator
    :return: The difference between the left and right entities
    :exception TypeError: Raised if (leftOperand - rightOperand) is not possible
    :exception ArithmeticError: Raised if the expression is valid, but some
        mathematical rule prevents the operation from being possible
    """

    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if (typeOfLeft is int) or (typeOfLeft is float):
        # The below "if" statements indicate what types can be subtracted from real numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand - rightOperand
        elif typeOfRight is Quaternion:
            return realMinusQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is complex:
        # The below "if" statements indicates what types can be subtracted from Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand - rightOperand
        elif typeOfRight is Quaternion:
            return complexMinusQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Vector:
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


def realMinusQuaternion(leftReal, rightQuaternion):
    """
    Subtracts the real number by the given Quaternion

    :param leftReal: The real number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The difference between the given real number and the given Quaternion
    """

    return Quaternion(leftReal - rightQuaternion.real,
                      -rightQuaternion.imag,
                      -rightQuaternion.imag1,
                      -rightQuaternion.imag2)


def complexMinusQuaternion(leftComplex, rightQuaternion):
    """
    Subtracts the given complex number by the given Quaternion

    :param leftComplex: The complex number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The difference between the given complex number and the given Quaternion
    """

    return Quaternion(leftComplex.real - rightQuaternion.real,
                      leftComplex.imag - rightQuaternion.imag,
                      -rightQuaternion.imag1,
                      -rightQuaternion.imag2)


def vectorMinusVector(leftVector, rightVector):
    """
    Subtracts one Vector from another Vector

    :param leftVector: The Vector on the left side of the operator
    :param rightVector: The Vector on the right side of the operator
    :return: The difference between the given Vectors
    :exception ArithmeticError: Raised if the two given Vector do not
        have the same dimensions
    """

    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be subtracted from each other")

    point = []

    for value1, value2 in zip(leftVector, rightVector):
        point.append(value1 - value2)

    return Vector(point)


def quaternionMinusReal(leftQuaternion, rightReal):
    """
    Subtracts the given Quaternion by the given real number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The difference between the given Quaternion and the given real number
    """

    return Quaternion(leftQuaternion.real - rightReal,
                      leftQuaternion.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionMinusComplex(leftQuaternion, rightComplex):
    """
    Subtracts the given Quaternion by the given complex number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The difference between the given Quaternion and the given complex number
    """

    return Quaternion(leftQuaternion.real - rightComplex.real,
                      leftQuaternion.imag - rightComplex.imag,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def quaternionMinusQuaternion(leftQuaternion, rightQuaternion):
    """
    Subtracts one Quaternion by another Quaternion

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The difference between the two Quaternions
    """

    return Quaternion(leftQuaternion.real - rightQuaternion.real,
                      leftQuaternion.imag - rightQuaternion.imag,
                      leftQuaternion.imag1 - rightQuaternion.imag1,
                      leftQuaternion.imag2 - rightQuaternion.imag2)


def matrixMinusMatrix(leftMatrix, rightMatrix):
    """
    Subtracts one Matrix by another Matrix

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightMatrix: The Matrix on the right side of the operator
    :return: The difference between the two Matrices
    :exception ArithmeticError: Raised if the two given Matrices do not
        have the same dimensions
    """

    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be subtracted from each other")

    table = []

    for value1, value2 in zip(leftMatrix, rightMatrix):
        result = subtraction(value1, value2)
        table.append(result)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def multiplication(leftOperand, rightOperand):
    """
    Handles al of the multiplication operations between two mathematical entities

    :param leftOperand: The entity on the left side of the operator
    :param rightOperand: The entity on the right side of the operator
    :return: The product of both left and right entities
    :exception TypeError: Raised if (leftOperand * rightOperand) is not possible
    :exception ArithmeticError: Raised if the expression is valid, but some
        mathematical rule prevents the operation from being possible
    """

    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if (typeOfLeft is int) or (typeOfLeft is float):
        # The below "if" statements indicate what types can be multiplied to real numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand * rightOperand
        elif typeOfRight is Quaternion:
            return quaternionTimesReal(rightOperand, leftOperand)
        elif typeOfRight is Vector:
            return vectorTimesReal(rightOperand, leftOperand)
        elif typeOfRight is Matrix:
            return matrixTimesScalar(rightOperand, leftOperand)
    elif typeOfLeft is complex:
        # The below "if" statements indicate what types can be multiplied to Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand + rightOperand
        elif typeOfRight is Quaternion:
            return complexTimesQuaternion(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixTimesScalar(rightOperand, leftOperand)
    elif typeOfLeft is Vector:
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
        elif typeOfRight is Matrix:
            return matrixTimesScalar(rightOperand, leftOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be multiplied to Matrices

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex) or (typeOfRight is Quaternion):
            return matrixTimesScalar(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixTimesMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " * " + str(typeOfRight) + " is not possible")


def complexTimesQuaternion(leftComplex, rightQuaternion):
    """
    Multiplies the given complex number by the given Quaternion

    :param leftComplex: The complex number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The product of the given complex number and the given Quaternion
    """

    return Quaternion(leftComplex.real * rightQuaternion.real - leftComplex.imag * rightQuaternion.imag,
                      leftComplex.real * rightQuaternion.imag + rightQuaternion.real * leftComplex.imag,
                      leftComplex.real * rightQuaternion.imag1 - leftComplex.imag * rightQuaternion.imag2,
                      leftComplex.real * rightQuaternion.imag2 + leftComplex.imag * rightQuaternion.imag1)


def vectorTimesReal(leftVector, rightReal):
    """
    Multiplies the given Vector by the given real number

    :param leftVector: The Vector on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The scalar product of the given Vector and the given real number
    """

    point = []

    for value in leftVector:
        point.append(value * rightReal)

    return Vector(point)


def quaternionTimesReal(leftQuaternion, rightReal):
    """
    Multiplies the given Quaternion by the given real number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The product of the given Quaternion and the given real number
    """

    return Quaternion(leftQuaternion.real * rightReal,
                      leftQuaternion.imag * rightReal,
                      leftQuaternion.imag1 * rightReal,
                      leftQuaternion.imag2 * rightReal)


def quaternionTimesComplex(leftQuaternion, rightComplex):
    """
    Multiplies the given Quaternion by the given complex number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The product of the given Quaternion and the given complex number
    """

    return Quaternion(leftQuaternion.real * rightComplex.real - leftQuaternion.imag * rightComplex.imag,
                      leftQuaternion.real * rightComplex.imag + leftQuaternion.imag * rightComplex.real,
                      leftQuaternion.imag1 * rightComplex.real + leftQuaternion.imag2 * rightComplex.imag,
                      -leftQuaternion.imag1 * rightComplex.imag + leftQuaternion.imag2 * rightComplex.real)


def quaternionTimesQuaternion(leftQuaternion, rightQuaternion):
    """
    Multiplies the two given Quaternions together

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The product of the two given Quaternions
    """

    return Quaternion(leftQuaternion.real * rightQuaternion.real - leftQuaternion.imag * rightQuaternion.imag -
                      leftQuaternion.imag1 * rightQuaternion.imag1 - leftQuaternion.imag2 * rightQuaternion.imag2,
                      leftQuaternion.real * rightQuaternion.imag + leftQuaternion.imag * rightQuaternion.real -
                      leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1,
                      leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag * rightQuaternion.imag2 +
                      leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag,
                      leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag * rightQuaternion.imag1 +
                      leftQuaternion.imag1 * rightQuaternion.imag + leftQuaternion.imag2 * rightQuaternion.real)


def matrixTimesScalar(leftMatrix, rightScalar):
    """
    Multiplies the given Matrix by the given scalar value. Scalar values
    include int, float, complex and Quaternion

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightScalar: The scalar value on the right side of the operator
    :return: The scalar product of the given Matrix and the given scalar value
    """

    table = []

    for value in leftMatrix:
        result = multiplication(value, rightScalar)
        table.append(result)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def matrixTimesMatrix(leftMatrix, rightMatrix):
    """
    Multiplies the two given Matrices together

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightMatrix: The Matrix on the right side of the operator
    :return: The product of the two given Matrices
    :exception ArithmeticError: Raised when the left Matrix does not have the
        same number of columns as the right Matrix has rows
    """

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
    """
    Calculates the value of a particular entry in the product
    of two Matrices

    :param leftMatrix: The Matrix on the left side of the multiplication operator
    :param rightMatrix: The Matrix on the right side of the multiplication operator
    :param rowIndex: The row index of the entry to be computed
    :param colIndex: The column index of the entry to be computed
    :return: An entry in the product of Two Matrices
    """

    value = 0.0

    for index in range(leftMatrix.rowLength):
        value += leftMatrix[rowIndex, index] * rightMatrix[index, colIndex]

    return value


def division(leftOperand, rightOperand):
    """
    Handles all division operations between mathematical entities

    :param leftOperand: The entity on the left side of the operator
    :param rightOperand: The entity on the right side of the operator
    :return: The quotient of the left entity and the right entity
    :exception TypeError: Raised if (leftOperand / rightOperand) is not possible
    :exception ArithmeticError: Raised if the expression is valid, but some
        mathematical rule prevents the operation from being possible
    """

    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if (typeOfLeft is int) or (typeOfLeft is float):
        # The below "if" statements indicate what types can be divided from real numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand / rightOperand
        elif typeOfRight is Quaternion:
            return realDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is complex:
        # The below "if" statements indicate what types can be divided from Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand / rightOperand
        elif typeOfLeft is Quaternion:
            return complexDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Vector:
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


def realDividedByQuaternion(leftReal, rightQuaternion):
    """
    Divides the given real number by the given Quaternion

    :param leftReal: The real number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The quotient of the given real number and the given Quaternion
    """

    absoluteValueOfRight = abs(rightQuaternion)

    return Quaternion((leftReal * rightQuaternion.real) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag1) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag2) / absoluteValueOfRight)


def complexDividedByQuaternion(leftComplex, rightQuaternion):
    """
    Divides the given complex number by the given Quaternion

    :param leftComplex: The complex number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The quotient of the given complex number and the given Quaternion
    """

    absoluteValueOfRight = abs(rightQuaternion)

    realOfResult = leftComplex.real * rightQuaternion.real + leftComplex.imag * rightQuaternion.imag
    imagOfResult = leftComplex.imag * rightQuaternion.real - leftComplex.real * rightQuaternion.imag
    imag1OfResult = -leftComplex.real * rightQuaternion.imag1 - leftComplex.imag * rightQuaternion.imag2
    imag2OfResult = leftComplex.imag * rightQuaternion.imag1 - leftComplex.real * rightQuaternion.imag2

    return Quaternion(realOfResult / absoluteValueOfRight,
                      imagOfResult / absoluteValueOfRight,
                      imag1OfResult / absoluteValueOfRight,
                      imag2OfResult / absoluteValueOfRight)


def vectorDividedByReal(leftVector, rightReal):
    """
    Divides the given Vector by the given real number

    :param leftVector: The Vector on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The quotient of the given Vector and the given real number
    """

    return vectorTimesReal(leftVector, 1 / rightReal)


def quaternionDividedByReal(leftQuaternion, rightReal):
    """
    Divides the given Quaternion by the given real number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The quotient of the given Quaternion and the given real number
    """

    return Quaternion(leftQuaternion.real / rightReal,
                      leftQuaternion.imag / rightReal,
                      leftQuaternion.imag1 / rightReal,
                      leftQuaternion.imag2 / rightReal)


def quaternionDividedByComplex(leftQuaternion, rightComplex):
    """
    Divides the given Quaternion by the given complex number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The quotient of the given Quaternion and the given complex number
    """

    conjugateOfRightComplex = rightComplex.conjugate()
    numerator = quaternionTimesComplex(leftQuaternion, conjugateOfRightComplex)
    denominator = rightComplex * conjugateOfRightComplex
    result = quaternionDividedByReal(numerator, denominator.real)

    return result


def quaternionDividedByQuaternion(leftQuaternion, rightQuaternion):
    """
    Divides a Quaternion by another Quaternion

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The quotient of the two Quaternions
    """

    absoluteValueOfLeft = abs(rightQuaternion)

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
    """
    Scalar divides the given Matrix by the given scalar value

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightScalar: The scalar value on the right side of the operator
    :return: The quotient of the given Matrix and the given scalar value
    """

    return matrixTimesScalar(leftMatrix, 1 / rightScalar)


def matrixDividedByMatrix(leftMatrix, rightMatrix):
    """
    Divides one Matrix by another Matrix. The left Matrix
    must have the same number of columns as the right Matrix
    has rows and the right Matrix must be square

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightMatrix: The Matrix on the right side of the operator
    :return: The quotient of the two given Matrices
    :exception ArithmeticError: Raised when the right Matrix is not square
        or the left Matrix does not have the same number of columns as the
        right Matrix has rows
    """

    return matrixTimesMatrix(leftMatrix, rightMatrix.inverse())


def floorDivision(leftOperand, rightOperand):
    """
    Handles all floor division operations between mathematical entities

    :param leftOperand: The entity on the left side of the operator
    :param rightOperand: The entity on the left side of the operator
    :return: The floor quotient of the operands
    :exception TypeError: Raised if (leftOperand / rightOperand) is not possible
    :exception ArithmeticError: Raised if the expression is valid, but some
        mathematical rule prevents the operation from being possible
    """

    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if (typeOfLeft is int) or (typeOfLeft is float):
        # The below "if" statements indicate what types can be floor divided by real numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand // rightOperand
        elif typeOfRight is Quaternion:
            return realFloorDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is complex:
        # The below "if" statements indicate what types can be floor divided by Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand // rightOperand
        elif typeOfRight is Quaternion:
            return complexFloorDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Vector:
        # The below "if" statements indicate what types can be floor divided from Vectors

        if (typeOfRight is int) or (typeOfRight is float):
            return vectorFloorDividedByReal(leftOperand, rightOperand)
    elif typeOfLeft is Quaternion:
        # The below "if" statements indicate what types can be floor divided from Quaternions

        if (typeOfRight is int) or (typeOfRight is float):
            return quaternionFloorDividedByReal(leftOperand, rightOperand)
        elif typeOfRight is complex:
            return quaternionFloorDividedByComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionFloorDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be floor divided from Matrices

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return matrixFloorDividedByScalar(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixFloorDividedByMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " // " + str(typeOfRight) + " is not possible")


def realFloorDividedByQuaternion(leftReal, rightQuaternion):
    """
    Floor divides the given real number by the given Quaternion

    :param leftReal: The real number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The floor quotient of the given real number and the given
        Quaternion
    """

    trueDivided = realDividedByQuaternion(leftReal, rightQuaternion)
    trueDivided = rounding(trueDivided)

    return trueDivided


def complexFloorDividedByQuaternion(leftComplex, rightQuaternion):
    """
    Floor divides the given complex number vt the given Quaternion

    :param leftComplex: The complex number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The floor quotient of the given complex number and the given
        Quaternion
    """

    trueDivided = complexDividedByQuaternion(leftComplex, rightQuaternion)
    trueDivided = rounding(trueDivided)

    return trueDivided


def vectorFloorDividedByReal(leftVector, rightReal):
    """
    Floor divides the given Vector by the given real number

    :param leftVector: The Vector on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The floor quotient of the given Vector and the given real number
    """

    point = []

    for value in leftVector:
        point.append(value // rightReal)

    return Vector(point)


def quaternionFloorDividedByReal(leftQuaternion, rightReal):
    """
    Floor divides the given Quaternion by the given real number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The floor quotient of the given Quaternion and the given
        real number
    """

    trueDivided = quaternionDividedByReal(leftQuaternion, rightReal)
    trueDivided = rounding(trueDivided)

    return trueDivided


def quaternionFloorDividedByComplex(leftQuaternion, rightComplex):
    """
    Floor divides the given Quaternion by the given complex number

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The floor quotient of the given Quaternion and the given complex
        number
    """

    trueDivided = quaternionDividedByComplex(leftQuaternion, rightComplex)
    trueDivided = rounding(trueDivided)

    return trueDivided


def quaternionFloorDividedByQuaternion(leftQuaternion, rightQuaternion):
    """
    Floor divides a Quaternion by another Quaternion

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The floor quotient of two Quaternions
    """

    trueDivided = quaternionDividedByQuaternion(leftQuaternion, rightQuaternion)
    trueDivided = rounding(trueDivided)

    return trueDivided


def matrixFloorDividedByScalar(leftMatrix, rightScalar):
    """
    Floor divides the given Matrix by the given scalar value

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightScalar: The scalar value on the right side of the operator
    :return: The floor quotient of the given Matrix and the given scalar value
    """

    result = matrixDividedByScalar(leftMatrix, rightScalar)

    for rowIndex in result.rowLength:
        for colIndex in result.columnLength:
            result[rowIndex, colIndex] = rounding(result[rowIndex, colIndex])

    return result


def matrixFloorDividedByMatrix(leftMatrix, rightMatrix):
    """
    Floor divides a Matrix by another Matrix

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightMatrix: The Matrix on the right side of the operator
    :return: The floor quotient of the given Matrices
    """

    trueDivided = matrixDividedByMatrix(leftMatrix, rightMatrix)

    for rowIndex in range(trueDivided.rowLength):
        for colIndex in range(trueDivided.columnLength):
            trueDivided[rowIndex, colIndex] = rounding(trueDivided[rowIndex, colIndex])

    return trueDivided


def negation(operand):
    """
    Handles all of the negation operations performed on any
    mathematical entity

    :param operand: The entity to be negated
    :return: The negation of the given entity
    """

    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float) or (typeOfOperand is complex):
        return -operand
    elif typeOfOperand is Vector:
        return negateVector(operand)
    elif typeOfOperand is Quaternion:
        return negateQuaternion(operand)
    elif typeOfOperand is Matrix:
        return negateMatrix(operand)

    raise TypeError(str(typeOfOperand) + "s do not have a negation")


def negateVector(vector):
    """
    Negates the given Vector

    :param vector: The Vector to be negated
    :return: The negation of the given Vector
    """

    return vectorTimesReal(vector, -1)


def negateQuaternion(quaternion):
    """
    Negates the given Quaternion

    :param quaternion: The Quaternion to be negated
    :return: The negation of the given Quaternion
    """

    return quaternionTimesReal(quaternion, -1)


def negateMatrix(matrix):
    """
    Negates the given Matrix

    :param matrix: The Matrix to be negated
    :return: The negation of the given Matrix
    """

    return matrixTimesScalar(matrix, -1)


def equality(leftOperand, rightOperand):
    """
    Handles all equality operations between mathematical entities

    :param leftOperand: The entity on the left side of the operator
    :param rightOperand: The entity on the right side of the operator
    :return: True if the two entities are equal, False otherwise
    """

    typeOfLeft = type(leftOperand)
    typeOfRight = type(rightOperand)

    if (typeOfLeft is int) or (typeOfLeft is float):
        # The below "if" statements indicate what types can be equal to real numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand == rightOperand
        elif typeOfRight is Quaternion:
            return quaternionEqualsReal(rightOperand, leftOperand)
    elif typeOfLeft is complex:
        # The below "if" statements indicate what types can be equal to Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is complex):
            return leftOperand == rightOperand
        elif typeOfRight is Quaternion:
            return quaternionEqualsComplex(rightOperand, leftOperand)
    elif typeOfLeft is Vector:
        # The below "if" statements indicate what types can be equal to Vectors

        if typeOfRight is Vector:
            return vectorEqualsVector(leftOperand, rightOperand)
    elif typeOfLeft is Quaternion:
        # The below "if" statements indicates what types can be equal to Quaternions

        if (typeOfRight is int) or (typeOfRight is float):
            return quaternionEqualsReal(leftOperand, rightOperand)
        elif typeOfRight is complex:
            return quaternionEqualsComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionEqualsQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be equal to Matrices

        if typeOfRight is Matrix:
            return matrixEqualsMatrix(leftOperand, rightOperand)

    return False


def vectorEqualsVector(leftVector, rightVector):
    """
    Checks if the two given Vectors have the same position
    in space and the same dimensions

    :param leftVector: The Vector on the left side of the operator
    :param rightVector: The Vector on the right side of the operator
    :return: True if both Vectors are equal, False otherwise
    """

    return leftVector.point == rightVector.point


def quaternionEqualsReal(leftQuaternion, rightReal):
    """
    Checks if the given Quaternion is equal to the given real number.
    For a Quaternion of the form a + bi + cj + dk to be equal to a real number,
    a must be equal to the given real number and b, c and d must be equal to zero

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: True if the given Quaternion is equal to the given real number,
        False otherwise
    """

    return leftQuaternion.real == rightReal and \
           leftQuaternion.imag == 0 and \
           leftQuaternion.imag1 == 0 and \
           leftQuaternion.imag2 == 0


def quaternionEqualsComplex(leftQuaternion, rightComplex):
    """
    Checks if the given Quaternion is equal to the given complex number.
    For a Quaternion of the form a + bi + cj+ dk to be equal to a complex number,
    a must be equal to the real component of the complex number, b must be equal to the
    imaginary component of the complex number and c and d must be equal to zero

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return:
    """

    return leftQuaternion.real == rightComplex.real and \
           leftQuaternion.imag == rightComplex.imag and \
           leftQuaternion.imag1 == 0 and \
           leftQuaternion.imag2 == 0


def quaternionEqualsQuaternion(leftQuaternion, rightQuaternion):
    """
    Checks if two Quaternions are equal. For two Quaternions to be equal,
    all four components must be the same

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: True if both Quaternions are equal, False otherwise
    """

    return leftQuaternion.real == rightQuaternion.real and \
           leftQuaternion.imag == rightQuaternion.imag and \
           leftQuaternion.imag1 == rightQuaternion.imag1 and \
           leftQuaternion.imag2 == rightQuaternion.imag2


def matrixEqualsMatrix(leftMatrix, rightMatrix):
    """
    Checks if two Matrices are equal. For two Matrices to be equal,
    they must have the same dimensions and have the same values in
    the same locations

    :param leftMatrix: The Matrix on the left side of the operator
    :param rightMatrix: The Matrix on the right side of the operator
    :return: True if both Matrices are equal, False otherwise
    """

    if not leftMatrix.equalDimensions(rightMatrix):
        return False

    for rowIndex in range(leftMatrix.rowLength):
        for colIndex in range(leftMatrix.columnLength):
            if not equality(leftMatrix[rowIndex, colIndex], rightMatrix[rowIndex, colIndex]):
                return False

    return True


def inequality(leftOperand, rightOperand):
    """
    Handles all inequality operations on mathematical entities

    :param leftOperand: The entity on the left side of the operator
    :param rightOperand: The entity on the right side of the operator
    :return: True if both entities are not equal, False otherwise
    """

    return not equality(leftOperand, rightOperand)


def rounding(operand, decimalNum=None):
    """
    Performs all rounding operations on mathematical entities.
    If an entity consists of multiple components, each component
    will be rounded individually

    :param operand: The entity to be rounded
    :param decimalNum: The number of decimal places to round to
    :return: A mathematically accurate entity with all components
        rounded to the desired number of decimal places
    """

    typeOfOperand = type(operand)

    if typeOfOperand is int:
        return operand
    elif typeOfOperand is float:
        return round(operand, decimalNum)
    elif typeOfOperand is complex:
        return roundComplex(operand, decimalNum)
    elif typeOfOperand is Quaternion:
        return roundQuaternion(operand, decimalNum)
    elif typeOfOperand is Vector:
        return roundVector(operand, decimalNum)
    elif typeOfOperand is Matrix:
        return roundMatrix(operand, decimalNum)

    raise TypeError(str(typeOfOperand) + "s cannot be rounded")


def roundComplex(cmplx, decimalNum):
    """
    Rounds the real and imaginary components of a complex number

    :param cmplx: The complex number to be rounded
    :param decimalNum: The number of decimal places to round to
    :return: A complex number with its components rounded
    """

    real = round(cmplx.real, decimalNum)
    imag = round(cmplx.imag, decimalNum)

    return complex(real, imag)


def roundQuaternion(quaternion, decimalNum):
    """
    Rounds the real and imaginary components of the given Quaternion

    :param quaternion: The Quaternion to be rounded
    :param decimalNum: The number of decimal places to round to
    :return: A Quaternion with its components rounded
    """

    real = round(quaternion.real, decimalNum)
    imag = round(quaternion.imag, decimalNum)
    imag1 = round(quaternion.imag1, decimalNum)
    imag2 = round(quaternion.imag2, decimalNum)

    return Quaternion(real, imag, imag1, imag2)


def roundVector(vector, decimalNum):
    """
    Rounds all components of the given Vector

    :param vector: The Vector to be rounded
    :param decimalNum: The number of decimal places tp round to
    :return: A Vector with all of its components rounded
    """

    point = []

    for value in vector:
        point.append(round(value, decimalNum))

    return Vector(point)


def roundMatrix(matrix, decimalNum):
    """
    Rounds all values contained in the given Matrix

    :param matrix: The Matrix to be rounded
    :param decimalNum: The number of decimal places to round to
    :return: A Matrix with all of its values rounded
    """

    table = []

    for value in matrix:
        result = rounding(value, decimalNum)
        table.append(result)

    return Matrix(table, matrix.rowLength, matrix.columnLength)
