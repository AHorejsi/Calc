from typing import Union
from math import nan
from itertools import zip_longest
from calc.entities.MathEntity import MathEntity
from calc.entities.Quaternion import Quaternion
from calc.stats.NumberList import NumberList
from calc.entities.Vector import Vector
from calc.entities.Matrix import Matrix


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


def __complexDividedByQuaternion(leftComplex: complex, rightQuaternion: Quaternion) -> Quaternion:
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

    realOfResult = leftComplex.real * rightQuaternion.real + leftComplex.imag * rightQuaternion.imag0
    imagOfResult = leftComplex.imag * rightQuaternion.real - leftComplex.real * rightQuaternion.imag0
    imag1OfResult = -leftComplex.real * rightQuaternion.imag1 - leftComplex.imag * rightQuaternion.imag2
    imag2OfResult = leftComplex.imag * rightQuaternion.imag1 - leftComplex.real * rightQuaternion.imag2

    return Quaternion(realOfResult / absoluteValueOfRight,
                      imagOfResult / absoluteValueOfRight,
                      imag1OfResult / absoluteValueOfRight,
                      imag2OfResult / absoluteValueOfRight)


def __quaternionDividedByComplex(leftQuaternion: Quaternion, rightComplex: complex) -> Quaternion:
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


divDict = {(int, Quaternion): __realDividedByQuaternion,
           (int, NumberList): lambda leftInt, rightList: NumberList([leftInt / value for value in rightList]),
           (float, Quaternion): __realDividedByQuaternion,
           (float, NumberList): lambda leftFloat, rightList: NumberList([leftFloat / value for value in rightList]),
           (complex, Quaternion): __complexDividedByQuaternion,
           (complex, NumberList): lambda leftComplex, rightList: NumberList([leftComplex / value for value in rightList]),
           (Quaternion, int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real / rightInt,
                                                                          leftQuaternion.imag0 / rightInt,
                                                                          leftQuaternion.imag1 / rightInt,
                                                                          leftQuaternion.imag2 / rightInt),
           (Quaternion, float): lambda leftQuaternion, rightFloat: Quaternion(leftQuaternion.real / rightFloat,
                                                                              leftQuaternion.imag0 / rightFloat,
                                                                              leftQuaternion.imag1 / rightFloat,
                                                                              leftQuaternion.imag2 / rightFloat),
           (Quaternion, complex): __quaternionDividedByComplex,
           (Quaternion, Quaternion): __quaternionDividedByQuaternion,
           (NumberList, int): lambda leftList, rightInt: NumberList([value / rightInt for value in leftList]),
           (NumberList, float): lambda leftList, rightFloat: NumberList([value / rightFloat for value in leftList]),
           (NumberList, complex): lambda leftList, rightComplex: NumberList([value / rightComplex for value in leftList]),
           (NumberList, Quaternion): lambda leftList, rightQuaternion: NumberList([value / rightQuaternion for value in leftList]),
           (NumberList, NumberList): lambda leftList, rightList: NumberList([leftValue / rightValue
                                                                             for (leftValue, rightValue)
                                                                             in zip_longest(leftList, rightList, fillvalue=0)]),
           (Vector, int): lambda leftVector, rightInt: Vector([value / rightInt for value in leftVector]),
           (Vector, float): lambda leftVector, rightFloat: Vector([value / rightFloat for value in leftVector]),
           (Matrix, int): lambda leftMatrix, rightInt: Matrix.createMatrixFrom1DList([value / rightInt for value in leftMatrix],
                                                                                     leftMatrix.rowLength,
                                                                                     leftMatrix.columnLength),
           (Matrix, float): lambda leftMatrix, rightFloat: Matrix.createMatrixFrom1DList(
                                                            [value / rightFloat for value in leftMatrix],
                                                            leftMatrix.rowLength,
                                                            leftMatrix.columnLength),
           (Matrix, complex): lambda leftMatrix, rightComplex: Matrix.createMatrixFrom1DList(
                                                                [value / rightComplex for value in leftMatrix],
                                                                leftMatrix.rowLength,
                                                                leftMatrix.columnLength),
           (Matrix, Quaternion): lambda leftMatrix, rightQuaternion: Matrix.createMatrixFrom1DList(
                                                                        [value / rightQuaternion for value in leftMatrix],
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