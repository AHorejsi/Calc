from math import nan, floor
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


"""
Named functions
"""


def __generalPlus(leftEntity, rightEntity):
    return leftEntity + rightEntity


def __entityPlusReal(leftEntity, rightReal):
    leftEntity._real += rightReal


def __entityPlusComplex(leftEntity, rightComplex):
    leftEntity._real += rightComplex.real
    leftEntity._imag0 += rightComplex.imag0


def __quaternionPlusQuaternion(leftQuaternion, rightQuaternion):
    leftQuaternion._real += rightQuaternion.real
    leftQuaternion._imag0 += rightQuaternion.imag0
    leftQuaternion._imag1 += rightQuaternion.imag1
    leftQuaternion._imag2 += rightQuaternion.imag2


def __vectorPlusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be added together")

    for index in range(len(leftVector)):
        leftVector[index] += rightVector[index]


def __matrixPlusMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be added together")

    for rowIndex in range(leftMatrix.rowLength):
        for columnIndex in range(leftMatrix.columnLength):
            leftMatrix[(rowIndex, columnIndex)] += rightMatrix[(rowIndex, columnIndex)]


def __generalMinus(leftEntity, rightEntity):
    return leftEntity - rightEntity


def __entityMinusReal(leftEntity, rightReal):
    leftEntity._real -= rightReal


def __entityMinusComplex(leftEntity, rightComplex):
    leftEntity._real -= rightComplex.real
    leftEntity._imago -= rightComplex.imag0


def __quaternionMinusQuaternion(leftQuaternion, rightQuaternion):
    leftQuaternion._real -= rightQuaternion.real
    leftQuaternion._imag0 -= rightQuaternion.imag0
    leftQuaternion._imag1 -= rightQuaternion.imag1
    leftQuaternion._imag2 -= rightQuaternion.imag2


def __vectorMinusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be subtracted from each other")

    for index in range(len(leftVector)):
        leftVector[index] -= rightVector[index]


def __matrixMinusMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be subtracted from each other")

    for rowIndex in range(leftMatrix.rowLength):
        for columnIndex in range(leftMatrix.columnLength):
            leftMatrix[(rowIndex, columnIndex)] -= rightMatrix[(rowIndex, columnIndex)]


"""
Operation dictionaries
"""


addDict = {(Complex, int): __entityPlusReal,
           (Complex, float): __entityPlusReal,
           (Complex, Complex): __entityPlusComplex,
           (Complex, Quaternion): __generalPlus,
           (Quaternion, int): __entityPlusReal,
           (Quaternion, float): __entityPlusReal,
           (Quaternion, Complex): __entityPlusComplex,
           (Quaternion, Quaternion): __quaternionPlusQuaternion,
           (Vector, Vector): __vectorPlusVector,
           (Matrix, Matrix): __matrixPlusMatrix}

subtDict = {(Complex, int): __entityMinusReal,
            (Complex, float): __entityMinusReal,
            (Complex, Complex): __entityMinusComplex,
            (Complex, Quaternion): __generalPlus,
            (Quaternion, int): __entityMinusReal,
            (Quaternion, float): __entityMinusReal,
            (Quaternion, Complex): __entityMinusComplex,
            (Quaternion, Quaternion): __quaternionMinusQuaternion,
            (Vector, Vector): __vectorMinusVector,
            (Matrix, Matrix): __matrixMinusMatrix}

multDict = {}

divDict = {}

floorDivDict = {}

expDict = {}

mutationOperations = {(Complex, "+", Quaternion),
                      (Complex, "-", Quaternion)}


"""
Operation functions
"""


def doAddition(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    func = addDict.get(key)

    if func is not None:
        if (key[0], "+", key[1]) in mutationOperations:
            return False
        else:
            func(mathEntity1, mathEntity2)
            return True
    else:
        raise ArithmeticError("Invalid operation")


def doSubtraction(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    func = subtDict.get(key)

    if func is not None:
        if (key[0], "-", key[1]) in mutationOperations:
            return False
        else:
            func(mathEntity1, mathEntity2)
            return True
    else:
        raise ArithmeticError("Invalid operation")


def doMultiplication(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    func = multDict.get(key)

    if func is not None:
        if (key[0], "*", key[1]) in mutationOperations:
            return False
        else:
            func(mathEntity1, mathEntity2)
            return True
    else:
        raise ArithmeticError("Invalid operation")


def doDivision(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    func = divDict.get(key)

    if func is not None:
        if (key[0], "/", key[1]) in mutationOperations:
            return False
        else:
            func(mathEntity1, mathEntity2)
            return True
    else:
        raise ArithmeticError("Invalid operation")


def doFloorDivision(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    func = expDict.get(key)

    if func is not None:
        if (key[0], "//", key[1]) in mutationOperations:
            return False
        else:
            func(mathEntity1, mathEntity2)
            return True
    else:
        raise ArithmeticError("Invalid operation")


def doExponentiation(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    func = expDict.get(key)

    if func is not None:
        if (key[0], "**", key[1]) in mutationOperations:
            return False
        else:
            func(mathEntity1, mathEntity2)
            return True
    else:
        raise ArithmeticError("Invalid operation")
