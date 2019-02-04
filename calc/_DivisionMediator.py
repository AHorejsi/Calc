from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __realDividedByComplex(leftReal: Union[int, float], rightComplex: Complex) -> Complex:
    conj = rightComplex.conjugate()

    return (leftReal * conj) / (rightComplex * conj).real


def __realDividedByQuaternion(leftReal: Union[int, float], rightQuaternion: Quaternion) -> Quaternion:
    absoluteValueOfRight = abs(rightQuaternion)

    return Quaternion((leftReal * rightQuaternion.real) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag0) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag1) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag2) / absoluteValueOfRight)


def __complexDividedByComplex(leftComplex: Complex, rightComplex: Complex) -> Complex:
    conj = rightComplex.conjugate()
    numerator = leftComplex * conj
    denominator = (rightComplex * conj).real

    return numerator / denominator


def __complexDividedByQuaternion(leftComplex: Complex, rightQuaternion: Quaternion) -> Quaternion:
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
    conjugateOfRightComplex = rightComplex.conjugate()
    numerator = leftQuaternion * conjugateOfRightComplex
    denominator = rightComplex * conjugateOfRightComplex
    result = numerator / denominator.real

    return result


def __quaternionDividedByQuaternion(leftQuaternion: Quaternion, rightQuaternion: Quaternion) -> Quaternion:
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
    key = (type(mathEntity1), type(mathEntity2))
    operation = divDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doFloorDivision(mathEntity1: Union[int, float, MathEntity],
                    mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    trueDiv = doDivision(mathEntity1, mathEntity2)

    if (trueDiv is not None) and (trueDiv is not nan):
        return trueDiv.__floor__()
    else:
        return nan