from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.DataValueList import DataValueList
from calc.Vector import Vector
from calc.Matrix import Matrix


def __dataValueListMinusDataValueList(leftData: DataValueList, rightData: DataValueList) -> DataValueList:
    if not leftData.equalDimensions(rightData):
        raise ArithmeticError("Data value lists must contain the same number of elements to be subtracted from each other")

    values = []

    for (leftValue, rightValue) in zip(leftData, rightData):
        values.append(leftValue - rightValue)

    return DataValueList(values)


def __vectorMinusVector(leftVector: Vector, rightVector: Vector) -> Vector:
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be subtracted from each other")

    point = []

    for (leftValue, rightValue) in zip(leftVector, rightVector):
        point.append(leftValue - rightValue)

    return Vector(point)


def __matrixMinusMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> Matrix:
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be subtracted from each other")

    table = []

    for (leftValue, rightValue) in zip(leftMatrix, rightMatrix):
        table.append(leftValue - rightValue)

    return Matrix.createMatrixFrom1DList(table, leftMatrix.rowLength, leftMatrix.columnLength)


subtDict = {(int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt - rightQuaternion.real,
                                                                                -rightQuaternion.imag0,
                                                                                -rightQuaternion.imag1,
                                                                                -rightQuaternion.imag2),
            (int, DataValueList): lambda leftInt, rightData: DataValueList([leftInt - value for value in rightData]),
            (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat - rightQuaternion.real,
                                                                                    -rightQuaternion.imag0,
                                                                                    -rightQuaternion.imag1,
                                                                                    -rightQuaternion.imag2),
            (float, DataValueList): lambda leftFloat, rightData: DataValueList([leftFloat - value for value in rightData]),
            (complex, Quaternion): lambda leftComplex, rightQuaternion: Quaternion(leftComplex.real - rightQuaternion.real,
                                                                                        leftComplex.imag - rightQuaternion.imag0,
                                                                                        -rightQuaternion.imag1,
                                                                                        -rightQuaternion.imag2),
            (Quaternion, int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real - rightInt,
                                                                                leftQuaternion.imag0,
                                                                                leftQuaternion.imag1,
                                                                                leftQuaternion.imag2),
            (Quaternion, float): lambda leftQuaternion, rightFloat: Quaternion(leftQuaternion.real - rightFloat,
                                                                                    leftQuaternion.imag0,
                                                                                    leftQuaternion.imag1,
                                                                                    leftQuaternion.imag2),
            (Quaternion, complex): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real - rightComplex.real,
                                                                                        leftQuaternion.imag0 - rightComplex.imag,
                                                                                        leftQuaternion.imag1,
                                                                                        leftQuaternion.imag2),
            (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(leftQuaternion.real - rightQuaternion.real,
                                                                                              leftQuaternion.imag0 - rightQuaternion.imag0,
                                                                                              leftQuaternion.imag1 - rightQuaternion.imag1,
                                                                                              leftQuaternion.imag2 - rightQuaternion.imag2),
            (DataValueList, int): lambda leftData, rightInt: DataValueList([value - rightInt for value in leftData]),
            (DataValueList, float): lambda leftData, rightFloat: DataValueList([value - rightFloat for value in leftData]),
            (DataValueList, DataValueList): __dataValueListMinusDataValueList,
            (Vector, Vector): __vectorMinusVector,
            (Matrix, Matrix): __matrixMinusMatrix}


def doSubtraction(mathEntity1: Union[int, float, MathEntity],
                  mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    key = (type(mathEntity1), type(mathEntity2))
    operation = subtDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
