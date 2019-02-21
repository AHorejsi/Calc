from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.DataValueList import DataValueList
from calc.Vector import Vector
from calc.Matrix import Matrix


def __dataValueListPlusDataValueList(leftData: DataValueList, rightData: DataValueList) -> DataValueList:
    if not leftData.equalDimensions(rightData):
        raise ArithmeticError("Data value lists must contain the same number of elements to be added together")

    values = []

    for (leftValue, rightValue) in zip(leftData, rightData):
        values.append(leftValue + rightValue)

    return DataValueList(values)


def __vectorPlusVector(leftVector: Vector, rightVector: Vector) -> Vector:
    """
    Adds two vectors together

    :param leftVector: The vector on the left side of the addition sign
    :param rightVector: The vector on the right side of the addition sign
    :return: The sum of the two given vectors
    :raises ArithmeticError: Raised if the two given vectors do not have
        the same dimensions
    """

    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be added together")

    point = []

    for (leftValue, rightValue) in zip(leftVector, rightVector):
        point.append(leftValue + rightValue)

    return Vector(point)


def __matrixPlusMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> Matrix:
    """
    Adds two matrices together

    :param leftMatrix: The matrix on the left side of the addition sign
    :param rightMatrix: The matrix on the right side of the addition sign
    :return: The sum of the two given matrices
    :raises ArithmeticError: Raised if the two given matrices do not have
        the same dimensions
    """

    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be added together")

    table = []

    for (leftValue, rightValue) in zip(leftMatrix, rightMatrix):
        table.append(leftValue + rightValue)

    return Matrix.createMatrixFrom1DList(table, leftMatrix.rowLength, leftMatrix.columnLength)


addDict = {(int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt + rightQuaternion.real,
                                                                               rightQuaternion.imag0,
                                                                               rightQuaternion.imag1,
                                                                               rightQuaternion.imag2),
           (int, DataValueList): lambda leftInt, rightData: DataValueList([value + leftInt for value in rightData]),
           (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat + rightQuaternion.real,
                                                                                   rightQuaternion.imag0,
                                                                                   rightQuaternion.imag1,
                                                                                   rightQuaternion.imag2),
           (float, DataValueList): lambda leftFloat, rightData: DataValueList([value + leftFloat for value in rightData]),
           (complex, Quaternion): lambda leftComplex, rightQuaternion: Quaternion(leftComplex.real + rightQuaternion.real,
                                                                                  leftComplex.imag + rightQuaternion.imag0,
                                                                                  rightQuaternion.imag1,
                                                                                  rightQuaternion.imag2),
           (complex, DataValueList): lambda leftComplex, rightData: DataValueList([value + leftComplex for value in rightData]),
           (Quaternion, int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real + rightInt,
                                                                               leftQuaternion.imag0,
                                                                               leftQuaternion.imag1,
                                                                               leftQuaternion.imag2),
           (Quaternion, float): lambda leftQuaternion, rightFloat: Quaternion(leftQuaternion.real + rightFloat,
                                                                                     leftQuaternion.imag0,
                                                                                     leftQuaternion.imag1,
                                                                                     leftQuaternion.imag2),
           (Quaternion, complex): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real + rightComplex.real,
                                                                                  leftQuaternion.imag + rightComplex.imag0,
                                                                                  leftQuaternion.imag1,
                                                                                  leftQuaternion.imag2),
           (Quaternion, DataValueList): lambda leftQuaternion, rightData: DataValueList(
                                                                            [value + leftQuaternion for value in rightData]),
           (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(
               leftQuaternion.real + rightQuaternion.real,
               leftQuaternion.imag0 + rightQuaternion.imag0,
               leftQuaternion.imag1 + rightQuaternion.imag1,
               leftQuaternion.imag2 + rightQuaternion.imag2),
           (DataValueList, int): lambda leftData, rightInt: DataValueList([value + rightInt for value in leftData]),
           (DataValueList, float): lambda leftData, rightFloat: DataValueList([value + rightFloat for value in leftData]),
           (DataValueList, complex): lambda leftData, rightComplex: DataValueList([value + rightComplex for value in leftData]),
           (DataValueList, Quaternion): lambda leftData, rightQuaternion: DataValueList(
                                                                            [value + rightQuaternion for value in leftData]),
           (DataValueList, DataValueList): __dataValueListPlusDataValueList,
           (Vector, Vector): __vectorPlusVector,
           (Matrix, Matrix): __matrixPlusMatrix}


def doAddition(mathEntity1: Union[int, float, MathEntity],
               mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    """
    Performs addition of the two given mathematical entities. If
    the two mathematical entities cannot be added together, nan
    is returned

    :param mathEntity1: The mathematical entity on the left side
        of the addition sign
    :param mathEntity2: The mathematical entity on the right side
        of the addition sign
    :return: The sum of the two given mathematical entities if they
        can be added together. If they cannot be added together, nan
        is returned
    """

    key = (type(mathEntity1), type(mathEntity2))
    operation = addDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
