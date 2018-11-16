from cal.Vector import Vector
from cal.Quaternion import Quaternion
from cal.Matrix import Matrix
from cal.Complex import Complex
from math import ceil, floor


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

        if (typeOfRight is int) or (typeOfRight is float):
            return leftOperand + rightOperand
        elif typeOfRight is Complex:
            return realPlusComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionPlusReal(rightOperand, leftOperand)
    elif typeOfLeft is Complex:
        # The below "if" statements indicate what types can be added to Complex

        if (typeOfRight is int) or (typeOfRight is float):
            return realPlusComplex(rightOperand, leftOperand)
        elif typeOfRight is Complex:
            return complexPlusComplex(leftOperand, rightOperand)
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
        elif typeOfRight is Complex:
            return quaternionPlusComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionPlusQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be added to Matrices

        if typeOfRight is Matrix:
            return matrixPlusMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " + " + str(typeOfRight) + " is not possible")


def realPlusComplex(leftReal, rightComplex):
    """
    Adds the given real number to the given complex number

    :param leftReal: The real number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The sum of the given real number and the given complex number
    """

    return Complex(leftReal + rightComplex.real, rightComplex.imag)


def complexPlusComplex(leftComplex, rightComplex):
    """
    Adds two complex numbers together

    :param leftComplex: The complex number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The sum of the two given complex numbers
    """

    return Complex(leftComplex.real + rightComplex.real, leftComplex.imag + rightComplex.imag)


def vectorPlusVector(leftVector, rightVector):
    """
    Adds two Vectors together

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

        if (typeOfRight is int) or (typeOfRight is float):
            return leftOperand - rightOperand
        elif typeOfRight is Complex:
            return realMinusComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return realMinusQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Complex:
        # The below "if" statements indicates what types can be subtracted from Complex

        if (typeOfRight is int) or (typeOfRight is float):
            return complexMinusReal(leftOperand, rightOperand)
        elif typeOfRight is Complex:
            return complexMinusComplex(leftOperand, rightOperand)
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
        elif typeOfRight is Complex:
            return quaternionMinusComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionMinusQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be subtracted from Matrices

        if typeOfRight is Matrix:
            return matrixMinusMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " - " + str(typeOfRight) + " is not possible")


def realMinusComplex(leftReal, rightComplex):
    """
    Subtracts the given real number from the given complex number

    :param leftReal: The real number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The difference between the given real number and the given complex number
    """

    return Complex(leftReal - rightComplex.real, -rightComplex.imag)


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


def complexMinusReal(leftComplex, rightReal):
    """
    Subtracts the given complex number by the given real number

    :param leftComplex: The complex number on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The difference between the given complex number and the given real
        number
    """

    return Complex(leftComplex.real - rightReal, leftComplex.imag)


def complexMinusComplex(leftComplex, rightComplex):
    """
    Subtracts a complex number by another complex number

    :param leftComplex: The complex number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The difference between the two given complex numbers
    """

    return Complex(leftComplex.real - rightComplex.real, leftComplex.imag - rightComplex.imag)


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

        if (typeOfRight is int) or (typeOfRight is float):
            return leftOperand * rightOperand
        elif typeOfRight is Complex:
            return realTimesComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionTimesReal(rightOperand, leftOperand)
        elif typeOfRight is Vector:
            return vectorTimesReal(rightOperand, leftOperand)
        elif typeOfRight is Matrix:
            return matrixTimesScalar(rightOperand, leftOperand)
    elif typeOfLeft is Complex:
        # The below "if" statements indicate what types can be multiplied to Complex

        if (typeOfRight is int) or (typeOfRight is float):
            return realTimesComplex(rightOperand, leftOperand)
        elif typeOfRight is Complex:
            return complexTimesComplex(leftOperand, rightOperand)
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
        elif typeOfRight is Complex:
            return quaternionTimesComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionTimesQuaternion(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixTimesScalar(rightOperand, leftOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be multiplied to Matrices

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is Complex) or (typeOfRight is Quaternion):
            return matrixTimesScalar(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixTimesMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " * " + str(typeOfRight) + " is not possible")


def realTimesComplex(leftReal, rightComplex):
    """
    Multiplies the given real number by the given complex number

    :param leftReal: The real number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The product of the given real number and the given complex number
    """

    return Complex(leftReal * rightComplex.real, leftReal * rightComplex.imag)


def complexTimesComplex(leftComplex, rightComplex):
    """
    Multiplies two complex numbers together

    :param leftComplex: The complex number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The product of the two given complex numbers
    """

    return Complex(leftComplex.real * rightComplex.real - leftComplex.imag * rightComplex.imag,
                   leftComplex.real * rightComplex.imag + leftComplex.imag * rightComplex.real)


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

        if (typeOfRight is int) or (typeOfRight is float):
            return leftOperand / rightOperand
        elif typeOfRight is Complex:
            return realDividedByComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return realDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Complex:
        # The below "if" statements indicate what types can be divided from Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float):
            return complexDividedByReal(leftOperand, rightOperand)
        elif typeOfRight is Complex:
            return complexDividedByComplex(leftOperand, rightOperand)
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

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is Complex) or (typeOfRight is Quaternion):
            return matrixDividedByScalar(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixDividedByMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " / " + str(typeOfRight) + " is not possible")


def realDividedByComplex(leftReal, rightComplex):
    """
    Divides the given real number by the given complex number

    :param leftReal: The real number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The quotient of the given real number and the given complex number
    """

    conj = rightComplex.conjugate()
    numerator = leftReal * conj
    denominator = (rightComplex * conj).real

    return Complex(numerator.real / denominator, numerator.imag / denominator)


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


def complexDividedByReal(leftComplex, rightReal):
    """
    Divides the given complex number by the given real number

    :param leftComplex: The complex number on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The quotient of the given complex number and the given real number
    """

    return Complex(leftComplex.real / rightReal, leftComplex.imag / rightReal)


def complexDividedByComplex(leftComplex, rightComplex):
    """
    Divides a complex number by another complex number

    :param leftComplex: The complex number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The quotient of the two given complex numbers
    """

    conj = rightComplex.conjugate()
    numerator = complexTimesComplex(leftComplex, conj)
    denominator = (rightComplex * conj).real

    return Complex(numerator.real / denominator, numerator.imag / denominator)


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

        if (typeOfRight is int) or (typeOfRight is float):
            return leftOperand // rightOperand
        elif typeOfRight is Complex:
            return realFloorDividedByComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return realFloorDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Complex:
        # The below "if" statements indicate what types can be floor divided by Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float):
            return complexFloorDividedReal(leftOperand, rightOperand)
        elif typeOfRight is Complex:
            return complexFloorDividedByComplex(leftOperand, rightOperand)
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
        elif typeOfRight is Complex:
            return quaternionFloorDividedByComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionFloorDividedByQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be floor divided from Matrices

        if (typeOfRight is int) or (typeOfRight is float) or (typeOfRight is Complex) or (typeOfRight is Quaternion):
            return matrixFloorDividedByScalar(leftOperand, rightOperand)
        elif typeOfRight is Matrix:
            return matrixFloorDividedByMatrix(leftOperand, rightOperand)

    raise TypeError(str(typeOfLeft) + " // " + str(typeOfRight) + " is not possible")


def realFloorDividedByComplex(leftReal, rightComplex):
    """
    Floor divides the given real number by the given complex number

    :param leftReal: The real number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The floor quotient of the given real number and the given complex number
    """

    trueDivided = realDividedByComplex(leftReal, rightComplex)
    floorDivided = flooring(trueDivided)

    return floorDivided


def realFloorDividedByQuaternion(leftReal, rightQuaternion):
    """
    Floor divides the given real number by the given Quaternion

    :param leftReal: The real number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The floor quotient of the given real number and the given
        Quaternion
    """

    trueDivided = realDividedByQuaternion(leftReal, rightQuaternion)
    trueDivided = flooring(trueDivided)

    return trueDivided


def complexFloorDividedByReal(leftComplex, rightReal):
    """
    Floor divides the given complex number by the given real number

    :param leftComplex: The complex number on the left side of the operator
    :param rightReal: The real number on the right side of the operator
    :return: The floor quotient of the given complex number and the given real number
    """

    result = complexDividedByReal(leftComplex, rightReal)
    result = flooring(result)

    return result


def complexFloorDividedByComplex(leftComplex, rightComplex):
    """
    Floor divides a complex number by another complex number

    :param leftComplex: The complex number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: The floor quotient of the two complex numbers
    """

    trueDivided = complexDividedByComplex(leftComplex, rightComplex)
    floorDivided = flooring(trueDivided)

    return floorDivided


def complexFloorDividedByQuaternion(leftComplex, rightQuaternion):
    """
    Floor divides the given complex number vt the given Quaternion

    :param leftComplex: The complex number on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The floor quotient of the given complex number and the given
        Quaternion
    """

    trueDivided = complexDividedByQuaternion(leftComplex, rightQuaternion)
    trueDivided = flooring(trueDivided)

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
    trueDivided = flooring(trueDivided)

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
    trueDivided = flooring(trueDivided)

    return trueDivided


def quaternionFloorDividedByQuaternion(leftQuaternion, rightQuaternion):
    """
    Floor divides a Quaternion by another Quaternion

    :param leftQuaternion: The Quaternion on the left side of the operator
    :param rightQuaternion: The Quaternion on the right side of the operator
    :return: The floor quotient of two Quaternions
    """

    trueDivided = quaternionDividedByQuaternion(leftQuaternion, rightQuaternion)
    trueDivided = flooring(trueDivided)

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
            result[rowIndex, colIndex] = flooring(result[rowIndex, colIndex])

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
            trueDivided[rowIndex, colIndex] = flooring(trueDivided[rowIndex, colIndex])

    return trueDivided


def negation(operand):
    """
    Handles all of the negation operations performed on any
    mathematical entity

    :param operand: The entity to be negated
    :return: The negation of the given entity
    """

    typeOfOperand = type(operand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return -operand
    elif typeOfOperand is Complex:
        return negateComplex(operand)
    elif typeOfOperand is Vector:
        return negateVector(operand)
    elif typeOfOperand is Quaternion:
        return negateQuaternion(operand)
    elif typeOfOperand is Matrix:
        return negateMatrix(operand)

    raise TypeError(str(typeOfOperand) + "s do not have a negation")


def negateComplex(complex):
    """
    Negates the given complex number

    :param complex: The complex number to be negated
    :return: The negation of the given complex number
    """

    return Complex(-complex.real, -complex.imag)


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

        if (typeOfRight is int) or (typeOfRight is float):
            return leftOperand == rightOperand
        elif typeOfRight is Complex:
            return realEqualsComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionEqualsReal(rightOperand, leftOperand)
    elif typeOfLeft is Complex:
        # The below "if" statements indicate what types can be equal to Complex Numbers

        if (typeOfRight is int) or (typeOfRight is float):
            return realEqualsComplex(rightOperand, leftOperand)
        elif typeOfRight is Complex:
            return complexEqualsComplex(leftOperand, rightOperand)
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
        elif typeOfRight is Complex:
            return quaternionEqualsComplex(leftOperand, rightOperand)
        elif typeOfRight is Quaternion:
            return quaternionEqualsQuaternion(leftOperand, rightOperand)
    elif typeOfLeft is Matrix:
        # The below "if" statements indicate what types can be equal to Matrices

        if typeOfRight is Matrix:
            return matrixEqualsMatrix(leftOperand, rightOperand)

    return False


def realEqualsComplex(leftReal, rightComplex):
    """
    Checks if  the given real number is equal to the given complex number.
    For a real number to be equal to a complex number, the real number must
    be equal to the complex number's real component and the complex number's
    imaginary component must be equal to zero

    :param leftReal: The real number on the left side of the operator
    :param rightComplex: The complex on the right side of the operator
    :return: True if the given real number is equal to the given
        complex number, False otherwise
    """

    return leftReal == rightComplex.real and rightComplex.imag == 0


def complexEqualsComplex(leftComplex, rightComplex):
    """
    Checks if two complex numbers are equal to each other. All components
    must be the same for the two complex numbers to be equal

    :param leftComplex: The complex number on the left side of the operator
    :param rightComplex: The complex number on the right side of the operator
    :return: True if both complex numbers are equal, False otherwise
    """

    return leftComplex.real == rightComplex.real and leftComplex.imag == rightComplex.imag


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


def ceiling(operand):
    """
    Handles all rounding up operations on mathematical entities.
    If an entity consists of multiple components, each component
    will be rounded individually

    :param operand: The entity to be rounded
    :return: The entity rounded up
    """

    typeOfOperand = type(operand)

    if typeOfOperand is int:
        return operand
    elif typeOfOperand is float:
        return ceil(operand)
    elif typeOfOperand is Complex:
        return ceilComplex(operand)
    elif typeOfOperand is Quaternion:
        return ceilQuaternion(operand)
    elif typeOfOperand is Vector:
        return ceilVector(operand)
    elif typeOfOperand is Matrix:
        return ceilMatrix(operand)

    raise TypeError(str(typeOfOperand) + "s cannot be rounded")


def ceilComplex(complex):
    """
    Rounds the real and imaginary components of
    the given complex number

    :param complex: The complex number to be rounded
    :return: The given complex number with its components
        rounded up
    """

    real = ceil(complex.real)
    imag = ceil(complex.imag)

    return Complex(real, imag)


def ceilQuaternion(quaternion):
    """
    Rounds the real and imaginary components of the given Quaternion up

    :param quaternion: The Quaternion to be rounded
    :return: The given Quaternion with its components rounded up
    """

    real = ceil(quaternion.real)
    imag = ceil(quaternion.imag)
    imag1 = ceil(quaternion.imag1)
    imag2 = ceil(quaternion.imag2)

    return Quaternion(real, imag, imag1, imag2)


def ceilVector(vector):
    """
    Rounds each of the values in the given Vector upward

    :param vector: The Vector to have its values rounded up
    :return: The given Vector with its values rounded up
    """

    point = []

    for value in vector:
        result = ceil(value)
        point.append(result)

    return Vector(point)


def ceilMatrix(matrix):
    """
    Rounds the values in the given Matrix upward

    :param matrix: The Matrix to have its values rounded up
    :return: The given Matrix with its values rounded up
    """

    table = []

    for value in matrix:
        result = ceiling(value)
        table.append(result)

    return Matrix(table, matrix.rowLength, matrix.columnLength)


def flooring(operand):
    """
        Handles all rounding down operations on mathematical entities.
        If an entity consists of multiple components, each component
        will be rounded individually

        :param operand: The entity to be rounded
        :return: The entity rounded down
        """

    typeOfOperand = type(operand)

    if typeOfOperand is int:
        return operand
    elif typeOfOperand is float:
        return floor(operand)
    elif typeOfOperand is Complex:
        return floorComplex(operand)
    elif typeOfOperand is Quaternion:
        return floorQuaternion(operand)
    elif typeOfOperand is Vector:
        return floorVector(operand)
    elif typeOfOperand is Matrix:
        return floorMatrix(operand)


def floorComplex(complex):
    """
    Rounds the real and imaginary components of
    the given complex number down

    :param complex: The complex number to be rounded
    :return: The given complex number with its components
        rounded down
    """

    real = floor(complex.real)
    imag = floor(complex.imag)

    return Complex(real, imag)


def floorQuaternion(quaternion):
    """
    Rounds the real and imaginary components of the given Quaternion down

    :param quaternion: The Quaternion to be rounded
    :return: The given Quaternion with its components rounded down
    """

    real = floor(quaternion.real)
    imag = floor(quaternion.imag)
    imag1 = floor(quaternion.imag1)
    imag2 = floor(quaternion.imag2)

    return Quaternion(real, imag, imag1, imag2)


def floorVector(vector):
    """
    Rounds each of the values in the given Vector downward

    :param vector: The Vector to have its values rounded down
    :return: The given Vector with its values rounded down
    """

    point = []

    for value in vector:
        result = floor(value)
        point.append(result)

    return Vector(point)


def floorMatrix(matrix):
    """
    Rounds the values in the given Matrix downward

    :param matrix: The Matrix to have its values rounded down
    :return: The given Matrix with its values rounded down
    """

    table = []

    for value in matrix:
        result = flooring(value)
        table.append(result)

    return Matrix(table, matrix.rowLength, matrix.columnLength)


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
    elif typeOfOperand is Complex:
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

    return Complex(real, imag)


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
