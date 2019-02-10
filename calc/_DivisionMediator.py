from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __realDividedByComplex(leftReal: Union[int, float], rightComplex: Complex) -> Complex:
    """
    Divides the given real number by the given complex number

    :param leftReal: The real number on the left side of the
        division sign
    :param rightComplex: The complex number on the right side
        of the division sign
    :return: The quotient of the given real number and the
        given complex number
    """

    conj = rightComplex.conjugate()

    return (leftReal * conj) / (rightComplex * conj).real


def __realDividedByQuaternion(leftReal: Union[int, float], rightQuaternion: Quaternion) -> Quaternion:
    """
    Divides the given real number by the given quaternion

    :param leftReal: The real number on the left side of
        the division sign
    :param rightQuaternion: The quaternion on the right
        side of the division sign
    :return: The quotient of the given real number and
        the given quaternion
    """

    absoluteValueOfRight = abs(rightQuaternion)

    return Quaternion((leftReal * rightQuaternion.real) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag0) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag1) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag2) / absoluteValueOfRight)


def __complexDividedByComplex(leftComplex: Complex, rightComplex: Complex) -> Complex:
    """
    Divides the first given complex number by the second
    given complex number

    :param leftComplex: The complex number on the left
        side of the division sign
    :param rightComplex: The complex number on the right
        side of the division sign
    :return: The quotient of the two given complex numbers
    """

    conj = rightComplex.conjugate()
    numerator = leftComplex * conj
    denominator = (rightComplex * conj).real

    return numerator / denominator


def __complexDividedByQuaternion(leftComplex: Complex, rightQuaternion: Quaternion) -> Quaternion:
    """
    Divides the given complex number by the given quaternion

    :param leftComplex: The complex number on the left side
        of the division sign
    :param rightQuaternion: The quaternion on the right side
        of the division sign
    :return: The quotient of the given complex number and the
        given quaternion
    """

    absoluteValueOfRight = abs(rightQuaternion)

    realOfResult = leftComplex.real * rightQuaternion.real + leftComplex.imag0 * rightQuaternion.imag0
    imagOfResult = leftComplex.imag0 * rightQuaternion.real - leftComplex.real * rightQuaternion.imag0
    imag1OfResult = -leftComplex.real * rightQuaternion.imag1 - leftComplex.imag0 * rightQuaternion.imag2
    imag2OfResult = leftComplex.imag0 * rightQuaternion.imag1 - leftComplex.real * rightQuaternion.imag2

    return Quaternion(realOfResult / absoluteValueOfRight,
                      imagOfResult / absoluteValueOfRight,
                      imag1OfResult / absoluteValueOfRight,
                      imag2OfResult / absoluteValueOfRight)


def __quaternionDividedByComplex(leftQuaternion: Quaternion, rightComplex: Complex) -> Quaternion:
    """
    Divides the given quaternion by the given complex number

    :param leftQuaternion: The quaternion on the left side of
        the division sign
    :param rightComplex: The complex number on the right side
        of the division sign
    :return: The quotient of the given quaternion and the given
        complex number
    """

    conjugateOfRightComplex = rightComplex.conjugate()
    numerator = leftQuaternion * conjugateOfRightComplex
    denominator = rightComplex * conjugateOfRightComplex
    result = numerator / denominator.real

    return result


def __quaternionDividedByQuaternion(leftQuaternion: Quaternion, rightQuaternion: Quaternion) -> Quaternion:
    """
    Divides the first given quaternion by the second given
    quaternion

    :param leftQuaternion: The quaternion on the left side of
        the division sign
    :param rightQuaternion: The quaternion on the right side
        of the division sign
    :return: The quotient of the two quaternions
    """

    absoluteValueOfLeft = abs(rightQuaternion)

    realOfResult = leftQuaternion.real * rightQuaternion.real + leftQuaternion.imag0 * rightQuaternion.imag0 + \
                   leftQuaternion.imag1 * rightQuaternion.imag1 + leftQuaternion.imag2 * rightQuaternion.imag2
    imagOfResult = leftQuaternion.real * rightQuaternion.imag0 - leftQuaternion.imag0 * rightQuaternion.real - \
                   leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1
    imag1OfResult = leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag0 * rightQuaternion.imag2 - \
                    leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag0
    imag2OfResult = leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag0 * rightQuaternion.imag1 + \
                    leftQuaternion.imag1 * rightQuaternion.imag0 - leftQuaternion.imag2 * rightQuaternion.real

    return Quaternion(realOfResult / absoluteValueOfLeft,
                      imagOfResult / absoluteValueOfLeft,
                      imag1OfResult / absoluteValueOfLeft,
                      imag2OfResult / absoluteValueOfLeft)


divDict = {(int, Complex): __realDividedByComplex,
           (int, Quaternion): __realDividedByQuaternion,
           (float, Complex): __realDividedByComplex,
           (float, Quaternion): __realDividedByQuaternion,
           (Complex, int): lambda leftComplex, rightInt: Complex(leftComplex.real / rightInt,
                                                                 leftComplex.imag0 / rightInt),
           (Complex, float): lambda leftComplex, rightInt: Complex(leftComplex.real / rightInt,
                                                                   leftComplex.imag0 / rightInt),
           (Complex, Complex): __complexDividedByComplex,
           (Complex, Quaternion): __complexDividedByQuaternion,
           (Quaternion, int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real / rightInt,
                                                                          leftQuaternion.imag0 / rightInt,
                                                                          leftQuaternion.imag1 / rightInt,
                                                                          leftQuaternion.imag2 / rightInt),
           (Quaternion, float): lambda leftQuaternion, rightFloat: Quaternion(leftQuaternion.real / rightFloat,
                                                                              leftQuaternion.imag0 / rightFloat,
                                                                              leftQuaternion.imag1 / rightFloat,
                                                                              leftQuaternion.imag2 / rightFloat),
           (Quaternion, Complex): __quaternionDividedByComplex,
           (Quaternion, Quaternion): __quaternionDividedByQuaternion,
           (Vector, int): lambda leftVector, rightInt: Vector([value / rightInt for value in leftVector]),
           (Vector, float): lambda leftVector, rightFloat: Vector([value / rightFloat for value in leftVector]),
           (Matrix, int): lambda leftMatrix, rightInt: Matrix.createMatrixFrom1DList([value / rightInt for value in leftMatrix],
                                                                                     leftMatrix.rowLength,
                                                                                     leftMatrix.columnLength),
           (Matrix, float): lambda leftMatrix, rightFloat: Matrix.createMatrixFrom1DList([value / rightFloat for value in leftMatrix],
                                                                                         leftMatrix.rowLength,
                                                                                         leftMatrix.columnLength),
           (Matrix, Complex): lambda leftMatrix, rightComplex: Matrix.createMatrixFrom1DList([value / rightComplex for value in leftMatrix],
                                                                                             leftMatrix.rowLength,
                                                                                             leftMatrix.columnLength),
           (Matrix, Quaternion): lambda leftMatrix, rightQuaternion: Matrix.createMatrixFrom1DList([value / rightQuaternion for value in leftMatrix],
                                                                                                   leftMatrix.rowLength,
                                                                                                   leftMatrix.columnLength),
           (Matrix, Matrix): lambda leftMatrix, rightMatrix: leftMatrix * rightMatrix.inverse()}


def doDivision(mathEntity1: Union[int, float, MathEntity],
               mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    """
    Divides the first given mathematical entity by the
    second given mathematical entity

    :param mathEntity1: The mathematical entity on the
        left side of the division sign
    :param mathEntity2: The mathematical entity on the
        right side of the division sign
    :return: The quotient of the two given mathematical
        entities. If the first cannot be divided by the
        second, nan is returned
    """

    key = (type(mathEntity1), type(mathEntity2))
    operation = divDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan