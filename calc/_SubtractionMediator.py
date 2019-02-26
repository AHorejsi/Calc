from typing import Union
from math import nan
from itertools import zip_longest
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.NumberList import NumberList
from calc.Vector import Vector
from calc.Matrix import Matrix


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
            (int, NumberList): lambda leftInt, rightList: NumberList([leftInt - value for value in rightList]),
            (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat - rightQuaternion.real,
                                                                                    -rightQuaternion.imag0,
                                                                                    -rightQuaternion.imag1,
                                                                                    -rightQuaternion.imag2),
            (float, NumberList): lambda leftFloat, rightList: NumberList([leftFloat - value for value in rightList]),
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
            (NumberList, int): lambda leftList, rightInt: NumberList([value - rightInt for value in leftList]),
            (NumberList, float): lambda leftList, rightFloat: NumberList([value - rightFloat for value in leftList]),
            (NumberList, NumberList): lambda leftList, rightList: NumberList([leftValue - rightValue
                                                                              for (leftValue, rightValue)
                                                                              in zip_longest(leftList, rightList, fillvalue=0)]),
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
