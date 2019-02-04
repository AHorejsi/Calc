from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __vectorPlusVector(leftVector: Vector, rightVector: Vector) -> Vector:
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be added together")

    point = []

    for (leftValue, rightValue) in zip(leftVector, rightVector):
        point.append(leftValue + rightValue)

    return Vector(point)


def __matrixPlusMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> Matrix:
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be added together")

    table = []

    for (leftValue, rightValue) in zip(leftMatrix, rightMatrix):
        table.append(leftValue + rightValue)

    return Matrix.createMatrixFrom1DList(table, leftMatrix.rowLength, leftMatrix.columnLength)


addDict = {(int, Complex): lambda leftInt, rightComplex: Complex(leftInt + rightComplex.real,
                                                                      rightComplex.imag0),
           (int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt + rightQuaternion.real,
                                                                               rightQuaternion.imag0,
                                                                               rightQuaternion.imag1,
                                                                               rightQuaternion.imag2),
           (float, Complex): lambda leftFloat, rightComplex: Complex(leftFloat + rightComplex.real,
                                                                          rightComplex.imag0),
           (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat + rightQuaternion.real,
                                                                                   rightQuaternion.imag0,
                                                                                   rightQuaternion.imag1,
                                                                                   rightQuaternion.imag2),
           (Complex, int): lambda leftComplex, rightInt: Complex(leftComplex.real + rightInt,
                                                                      leftComplex.imag0),
           (Complex, float): lambda leftComplex, rightFloat: Complex(leftComplex.real + rightFloat,
                                                                          leftComplex.imag0),
           (Complex, Complex): lambda leftComplex, rightComplex: Complex(leftComplex.real + rightComplex.real,
                                                                              leftComplex.imag0 + rightComplex.imag0),
           (Complex, Quaternion): lambda leftComplex, rightQuaternion: Quaternion(leftComplex.real + rightQuaternion.real,
                                                                                  leftComplex.imag0 + rightQuaternion.imag0,
                                                                                  rightQuaternion.imag1,
                                                                                  rightQuaternion.imag2),
           (Quaternion, int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real + rightInt,
                                                                               leftQuaternion.imag0,
                                                                               leftQuaternion.imag1,
                                                                               leftQuaternion.imag2),
           (Quaternion, float): lambda leftQuaternion, rightFloat: Quaternion(leftQuaternion.real + rightFloat,
                                                                                     leftQuaternion.imag0,
                                                                                     leftQuaternion.imag1,
                                                                                     leftQuaternion.imag2),
           (Quaternion, Complex): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real + rightComplex.real,
                                                                                  leftQuaternion.imag0 + rightComplex.imag0,
                                                                                  leftQuaternion.imag1,
                                                                                  leftQuaternion.imag2),
           (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(
               leftQuaternion.real + rightQuaternion.real,
               leftQuaternion.imag0 + rightQuaternion.imag0,
               leftQuaternion.imag1 + rightQuaternion.imag1,
               leftQuaternion.imag2 + rightQuaternion.imag2),
           (Vector, Vector): __vectorPlusVector,
           (Matrix, Matrix): __matrixPlusMatrix}


def doAddition(mathEntity1: Union[int, float, MathEntity],
               mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    key = (type(mathEntity1), type(mathEntity2))
    operation = addDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
