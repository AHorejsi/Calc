from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


"""
Named functions
"""


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


def __complexTimesReal(leftComplex, rightReal):
    leftComplex._real *= rightReal
    leftComplex._imag0 *= rightReal


def __complexTimesComplex(leftComplex, rightComplex):
    leftComplex._real = leftComplex.real * rightComplex.real - leftComplex.imag0 * rightComplex.imag0
    leftComplex._imag0 = leftComplex.real * rightComplex.imag0 + leftComplex.imag0 * rightComplex.real


def __quaternionTimesReal(leftQuaternion, rightReal):
    leftQuaternion._real *= rightReal
    leftQuaternion._imag0 *= rightReal
    leftQuaternion._imag1 *= rightReal
    leftQuaternion._imag2 *= rightReal


def __quaternionTimesComplex(leftQuaternion, rightComplex):
    leftQuaternion._real = leftQuaternion.real * rightComplex.real - leftQuaternion.imag0 * rightComplex.imag0
    leftQuaternion._imag0 = leftQuaternion.real * rightComplex.imag0 + leftQuaternion.imag0 * rightComplex.real
    leftQuaternion._imag1 = leftQuaternion.imag1 * rightComplex.real + leftQuaternion.imag2 * rightComplex.imag0
    leftQuaternion._imag2 = -leftQuaternion.imag1 * rightComplex.imag0 + leftQuaternion.imag2 * rightComplex.real


def __quaternionTimesQuaternion(leftQuaternion, rightQuaternion):
    leftQuaternion._real = leftQuaternion.real * rightQuaternion.real - leftQuaternion.imag0 * rightQuaternion.imag0 - \
                           leftQuaternion.imag1 * rightQuaternion.imag1 - leftQuaternion.imag2 * rightQuaternion.imag2
    leftQuaternion._imag0 = leftQuaternion.real * rightQuaternion.imag0 + leftQuaternion.imag0 * rightQuaternion.real - \
                            leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1
    leftQuaternion._imag1 = leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag0 * rightQuaternion.imag2 + \
                            leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag0
    leftQuaternion._imag2 = leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag0 * rightQuaternion.imag1 + \
                            leftQuaternion.imag1 * rightQuaternion.imag0 + leftQuaternion.imag2 * rightQuaternion.real


def __vectorTimesReal(leftVector, rightReal):
    for index in range(len(leftVector)):
        leftVector[index] *= rightReal


def __matrixTimesScalar(leftMatrix, rightScalar):
    for rowIndex in range(leftMatrix.rowLength):
        for columnIndex in range(leftMatrix.columnLength):
            leftMatrix[(rowIndex, columnIndex)] *= rightScalar


"""
Operation dictionaries
"""


addDict = {(Complex, int): __entityPlusReal,
           (Complex, float): __entityPlusReal,
           (Complex, Complex): __entityPlusComplex,
           (Quaternion, int): __entityPlusReal,
           (Quaternion, float): __entityPlusReal,
           (Quaternion, Complex): __entityPlusComplex,
           (Quaternion, Quaternion): __quaternionPlusQuaternion,
           (Vector, Vector): __vectorPlusVector,
           (Matrix, Matrix): __matrixPlusMatrix}

subtDict = {(Complex, int): __entityMinusReal,
            (Complex, float): __entityMinusReal,
            (Complex, Complex): __entityMinusComplex,
            (Quaternion, int): __entityMinusReal,
            (Quaternion, float): __entityMinusReal,
            (Quaternion, Complex): __entityMinusComplex,
            (Quaternion, Quaternion): __quaternionMinusQuaternion,
            (Vector, Vector): __vectorMinusVector,
            (Matrix, Matrix): __matrixMinusMatrix}

multDict = {(Complex, int): __complexTimesReal,
            (Complex, float): __complexTimesReal,
            (Complex, Complex): __complexTimesComplex,
            (Complex, Matrix): lambda leftComplex, rightMatrix: __matrixTimesScalar(rightMatrix, leftComplex),
            (Quaternion, int): __quaternionTimesReal,
            (Quaternion, float): __quaternionTimesReal,
            (Quaternion, Complex): __quaternionTimesComplex,
            (Quaternion, Quaternion): __quaternionTimesQuaternion,
            (Quaternion, Matrix): lambda leftComplex, rightMatrix: __matrixTimesScalar(rightMatrix, leftComplex),
            (Vector, int): __vectorTimesReal,
            (Vector, float): __vectorTimesReal,
            (Matrix, int): __matrixTimesScalar,
            (Matrix, float): __matrixTimesScalar,
            (Matrix, Complex): __matrixTimesScalar,
            (Matrix, Quaternion): __matrixTimesScalar}

divDict = {}

floorDivDict = {}

expDict = {}

mutationOperations = {(Complex, "+", Quaternion),
                      (Complex, "-", Quaternion),
                      (Complex, "*", Quaternion),
                      (Complex, "*", Matrix),
                      (Quaternion, "*", Matrix)}


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
