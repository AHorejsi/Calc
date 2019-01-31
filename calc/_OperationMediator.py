from math import e, nan, sin, cos, atan, log, floor
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __vectorPlusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be added together")

    point = []

    for (leftValue, rightValue) in zip(leftVector, rightVector):
        point.append(leftValue + rightValue)

    return Vector(point)


def __matrixPlusMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be added together")

    table = []

    for (leftValue, rightValue) in zip(leftMatrix, rightMatrix):
        table.append(leftValue + rightValue)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def __vectorMinusVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        raise ArithmeticError("Vectors must be of equal dimensions to be subtracted from each other")

    point = []

    for (leftValue, rightValue) in zip(leftVector, rightVector):
        point.append(leftValue - rightValue)

    return Vector(point)


def __matrixMinusMatrix(leftMatrix, rightMatrix):
    if not leftMatrix.equalDimensions(rightMatrix):
        raise ArithmeticError("Matrices must be of equal dimensions to be subtracted from each other")

    table = []

    for (leftValue, rightValue) in zip(leftMatrix, rightMatrix):
        table.append(leftValue - rightValue)

    return Matrix(table, leftMatrix.rowLength, leftMatrix.columnLength)


def __realDividedByComplex(leftReal, rightComplex):
    conj = rightComplex.conjugate()

    return (leftReal * conj) / (rightComplex * conj).real


def __realDividedByQuaternion(leftReal, rightQuaternion):
    absoluteValueOfRight = abs(rightQuaternion)

    return Quaternion((leftReal * rightQuaternion.real) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag0) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag1) / absoluteValueOfRight,
                      (-leftReal * rightQuaternion.imag2) / absoluteValueOfRight)


def __complexDividedByComplex(leftComplex, rightComplex):
    conj = rightComplex.conjugate()
    numerator = leftComplex * conj
    denominator = (rightComplex * conj).real

    return Complex(numerator.real / denominator, numerator.imag0 / denominator)


def __complexDividedByQuaternion(leftComplex, rightQuaternion):
    absoluteValueOfRight = abs(rightQuaternion)

    realOfResult = leftComplex.real * rightQuaternion.real + leftComplex.imag0 * rightQuaternion.imag0
    imagOfResult = leftComplex.imag0 * rightQuaternion.real - leftComplex.real * rightQuaternion.imag0
    imag1OfResult = -leftComplex.real * rightQuaternion.imag1 - leftComplex.imag0 * rightQuaternion.imag2
    imag2OfResult = leftComplex.imag0 * rightQuaternion.imag1 - leftComplex.real * rightQuaternion.imag2

    return Quaternion(realOfResult / absoluteValueOfRight,
                      imagOfResult / absoluteValueOfRight,
                      imag1OfResult / absoluteValueOfRight,
                      imag2OfResult / absoluteValueOfRight)


def __realToPowerOfComplex(leftReal, rightComplex):
    value1 = (leftReal ** 2) ** (rightComplex.real / 2)
    value2 = cos(log(leftReal))
    value3 = sin(log(leftReal))

    return Complex(value1 * value2, value1 * value3)


def __complexToPowerOfReal(leftComplex, rightReal):
    arg = atan(leftComplex.imag0 / leftComplex.real)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2)) ** (rightReal / 2)
    value2 = cos(rightReal * arg)
    value3 = sin(rightReal * arg)

    return Complex(value1 * value2, value1 * value3)


def __complexToPowerOfComplex(leftComplex, rightComplex):
    arg = atan(leftComplex.imag0 / leftComplex.real)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2))
    value2 = value1 ** (rightComplex.real / 2)
    value3 = e ** (-rightComplex.imag0 * arg)
    value4 = value2 * value3
    value5 = cos(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))
    value6 = sin(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))

    return Complex(value4 * value5, value4 * value6)


def __generalExponent(leftEntity, rightEntity):
    from calc.MathFunction import expMath, logMath

    return expMath(logMath(leftEntity) * rightEntity)


addDict = {(int, int): lambda leftInt, rightInt: leftInt + rightInt,
           (int, float): lambda leftInt, rightFloat: leftInt + rightFloat,
           (int, Complex): lambda leftInt, rightComplex: Complex(leftInt + rightComplex.real,
                                                                      rightComplex.imag0),
           (int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt + rightQuaternion.real,
                                                                               rightQuaternion.imag0,
                                                                               rightQuaternion.imag1,
                                                                               rightQuaternion.imag2),
           (float, int): lambda leftFloat, rightInt: leftFloat + rightInt,
           (float, float): lambda leftFloat, rightFloat: leftFloat + rightFloat,
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
           (Quaternion, float): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real + rightComplex.real,
                                                                                     leftQuaternion.imag0 + rightComplex.imag0,
                                                                                     leftQuaternion.imag1,
                                                                                     leftQuaternion.imag2),
           (Quaternion, Complex): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real + rightComplex.real,
                                                                                       leftQuaternion.imag0 + rightComplex.imag0,
                                                                                       leftQuaternion.imag1,
                                                                                       leftQuaternion.imag2),
           (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(leftQuaternion.real + rightQuaternion.real,
                                                                                             leftQuaternion.imag0 + rightQuaternion.imag0,
                                                                                             leftQuaternion.imag1 + rightQuaternion.imag1,
                                                                                             leftQuaternion.imag2 + rightQuaternion.imag2),
           (Vector, Vector): __vectorPlusVector,
           (Matrix, Matrix): __matrixPlusMatrix}

subtDict = {(int, int): lambda leftInt, rightInt: leftInt - rightInt,
            (int, float): lambda leftInt, rightFloat: leftInt - rightFloat,
            (int, Complex): lambda leftInt, rightComplex: Complex(leftInt - rightComplex.real,
                                                                       -rightComplex.imag0),
            (int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt - rightQuaternion.real,
                                                                                -rightQuaternion.imag0,
                                                                                -rightQuaternion.imag1,
                                                                                -rightQuaternion.imag2),
            (float, int): lambda leftFloat, rightInt: leftFloat - rightInt,
            (float, float): lambda leftFloat, rightFloat: leftFloat - rightFloat,
            (float, Complex): lambda leftFloat, rightComplex: Complex(leftFloat - rightComplex.real,
                                                                           -rightComplex.imag0),
            (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat - rightQuaternion.real,
                                                                                    -rightQuaternion.imag0,
                                                                                    -rightQuaternion.imag1,
                                                                                    -rightQuaternion.imag2),
            (Complex, int): lambda leftComplex, rightInt: Complex(leftComplex.real - rightInt,
                                                                       leftComplex.imag0),
            (Complex, float): lambda leftComplex, rightFloat: Complex(leftComplex.real - rightFloat,
                                                                           leftComplex.imag0),
            (Complex, Complex): lambda leftComplex, rightComplex: Complex(leftComplex.real - rightComplex.real,
                                                                               leftComplex.imag0 - rightComplex.imag0),
            (Complex, Quaternion): lambda leftComplex, rightQuaternion: Quaternion(leftComplex.real - rightQuaternion.real,
                                                                                        leftComplex.imag0 - rightQuaternion.imag0,
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
            (Quaternion, Complex): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real - rightComplex.real,
                                                                                        leftQuaternion.imag0 - rightComplex.imag0,
                                                                                        leftQuaternion.imag1,
                                                                                        leftQuaternion.imag2),
            (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(leftQuaternion.real - rightQuaternion.real,
                                                                                              leftQuaternion.imag0 - rightQuaternion.imag0,
                                                                                              leftQuaternion.imag1 - rightQuaternion.imag1,
                                                                                              leftQuaternion.imag2 - rightQuaternion.imag2),
            (Vector, Vector): __vectorMinusVector,
            (Matrix, Matrix): __matrixMinusMatrix}

multDict = {(int, int): lambda leftInt, rightInt: leftInt * rightInt,
            (int, float): lambda leftInt, rightFloat: leftInt * rightFloat,
            (int, Complex): lambda leftInt, rightComplex: Complex(leftInt * rightComplex.real,
                                                                       leftInt * rightComplex.imag0),
            (int, Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt * rightQuaternion.real,
                                                                                leftInt * rightQuaternion.imag0,
                                                                                leftInt * rightQuaternion.imag1,
                                                                                leftInt * rightQuaternion.imag2),
            (float, int): lambda leftFloat, rightInt: leftFloat * rightInt,
            (float, float): lambda leftFloat, rightFloat: leftFloat * rightFloat,
            (float, Complex): lambda leftInt, rightComplex: Complex(leftInt * rightComplex.real,
                                                                         leftInt * rightComplex.imag0),
            (float, Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat * rightQuaternion.real,
                                                                                    leftFloat * rightQuaternion.imag0,
                                                                                    leftFloat * rightQuaternion.imag1,
                                                                                    leftFloat * rightQuaternion.imag2),
            (Complex, int): lambda leftComplex, rightInt: Complex(leftComplex.real * rightInt,
                                                                  leftComplex.imag0 * rightInt),
            (Complex, float): lambda leftComplex, rightFloat: Complex(leftComplex.real * rightFloat,
                                                                      leftComplex.imag0 * rightFloat),
            (Complex, Complex): lambda leftComplex, rightComplex: Complex(
                   leftComplex.real * rightComplex.real - leftComplex.imag0 * rightComplex.imag0,
                   leftComplex.real * rightComplex.imag0 + leftComplex.imag0 * rightComplex.real),
            (Complex, Quaternion): lambda leftComplex, rightQuaternion: Quaternion(
                      leftComplex.real * rightQuaternion.real - leftComplex.imag0 * rightQuaternion.imag0,
                      leftComplex.real * rightQuaternion.imag0 + rightQuaternion.real * leftComplex.imag0,
                      leftComplex.real * rightQuaternion.imag1 - leftComplex.imag0 * rightQuaternion.imag2,
                      leftComplex.real * rightQuaternion.imag2 + leftComplex.imag0 * rightQuaternion.imag1),
            (Complex, Matrix): lambda leftComplex, rightMatrix: Matrix([leftComplex * value for value in rightMatrix],
                                                                       rightMatrix.rowLength,
                                                                       rightMatrix.columnLength)}

divDict = {(int, int): lambda leftInt, rightInt: leftInt / rightInt,
           (int, float): lambda leftInt, rightFloat: leftInt / rightFloat,
           (int, Complex): __realDividedByComplex,
           (int, Quaternion): __realDividedByQuaternion,
           (float, int): lambda leftFloat, rightInt: leftFloat / rightInt,
           (float, float): lambda leftFloat, rightFloat: leftFloat / rightFloat,
           (float, Complex): __realDividedByComplex,
           (float, Quaternion): __realDividedByQuaternion,
           (Complex, int): lambda leftComplex, rightInt: Complex(leftComplex.real / rightInt,
                                                                 leftComplex.imag0 / rightInt),
           (Complex, float): lambda leftComplex, rightInt: Complex(leftComplex.real / rightInt,
                                                                 leftComplex.imag0 / rightInt),
           (Complex, Complex): __complexDividedByComplex,
           (Complex, Quaternion): __complexDividedByQuaternion}

negDict = {int: lambda int: -int,
           float: lambda float: -float,
           Complex: lambda complex: Complex(-complex.real, -complex.imag0),
           Quaternion: lambda quaternion: Quaternion(-quaternion.real, -quaternion.imag0,
                                                            -quaternion.imag1, -quaternion.imag2),
           Vector: lambda vector: Vector([-value for value in vector]),
           Matrix: lambda matrix: Matrix([-value for value in matrix])}

expDict = {(int, int): lambda leftInt, rightInt: leftInt ** rightInt,
           (int, float): lambda leftInt, rightFloat: leftInt ** rightFloat,
           (int, Complex): __realToPowerOfComplex,
           (int, Quaternion): __generalExponent,
           (float, int): lambda leftFloat, rightInt: leftFloat ** rightInt,
           (float, float): lambda leftFloat, rightFloat: leftFloat ** rightFloat,
           (float, Complex): __realToPowerOfComplex,
           (float, Quaternion): __generalExponent,
           (Complex, int): __complexToPowerOfReal,
           (Complex, float): __complexToPowerOfReal,
           (Complex, Complex): __complexToPowerOfComplex,
           (Complex, Quaternion): __generalExponent,
           (Quaternion, int): __generalExponent,
           (Quaternion, float): __generalExponent,
           (Quaternion, Complex): __generalExponent,
           (Quaternion, Quaternion): __generalExponent}

eqDict = {(int, int): lambda leftInt, rightInt: leftInt == rightInt,
          (int, float): lambda leftInt, rightFloat: leftInt == rightFloat,
          (int, Complex): lambda leftInt, rightComplex: leftInt == rightComplex.real and
                                                              rightComplex.imag0 == 0,
          (int, Quaternion): lambda leftInt, rightQuaternion: leftInt == rightQuaternion.real and
                                                                    rightQuaternion.imag0 == 0 and
                                                                    rightQuaternion.imag1 == 0 and
                                                                    rightQuaternion.imag2 == 0,
          (float, int): lambda leftFloat, rightInt: leftFloat == rightInt,
          (float, float): lambda leftFloat, rightFloat: leftFloat == rightFloat,
          (float, Complex): lambda leftFloat, rightComplex: leftFloat == rightComplex.real and
                                                                  rightComplex.imag0 == 0,
          (float, Quaternion): lambda leftFloat, rightQuaternion: leftFloat == rightQuaternion.real and
                                                                        rightQuaternion.imag0 == 0 and
                                                                        rightQuaternion.imag1 == 0 and
                                                                        rightQuaternion.imag2 == 0,
          (Complex, int): lambda leftComplex, rightInt: leftComplex.real == rightInt and
                                                              leftComplex.imag0 == 0,
          (Complex, float): lambda leftComplex, rightFloat: leftComplex.real == rightFloat and
                                                                  leftComplex.imag0 == 0,
          (Complex, Complex): lambda leftComplex, rightComplex: leftComplex.real == rightComplex.real and
                                                                      leftComplex.imag0 == rightComplex.imag0,
          (Complex, Quaternion): lambda leftComplex, rightQuaternion: leftComplex.real == rightQuaternion.real and
                                                                            leftComplex.imag0 == rightQuaternion.imag0 and
                                                                            leftComplex.imag1 == 0 and
                                                                            leftComplex.imag2 == 0,
          (Quaternion, int): lambda leftQuaternion, rightInt: leftQuaternion.real == rightInt and
                                                                    leftQuaternion.imag0 == 0 and
                                                                    leftQuaternion.imag1 == 0 and
                                                                    leftQuaternion.imag2 == 0,
          (Quaternion, float): lambda leftQuaternion, rightFloat: leftQuaternion.real == rightFloat and
                                                                        leftQuaternion.imag0 == 0 and
                                                                        leftQuaternion.imag1 == 0 and
                                                                        leftQuaternion.imag2 == 0,
          (Quaternion, Complex): lambda leftQuaternion, rightComplex: leftQuaternion.real == rightComplex.real and
                                                                            leftQuaternion.imag0 == rightComplex.imag0 and
                                                                            leftQuaternion.imag1 == 0 and
                                                                            leftQuaternion.imag2 == 0,
          (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: leftQuaternion.real == rightQuaternion.real and
                                                                                  leftQuaternion.imag0 == rightQuaternion.imag0 and
                                                                                  leftQuaternion.imag1 == rightQuaternion.imag1 and
                                                                                  leftQuaternion.imag2 == rightQuaternion.imag2,
          (bool, bool): lambda leftBool, rightBool: leftBool == rightBool}


def doAddition(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    operation = addDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doSubtraction(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    operation = subtDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doMultiplication(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    operation = multDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doDivision(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    operation = divDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doFloorDivision(mathEntity1, mathEntity2):
    trueDiv = doDivision(mathEntity1, mathEntity2)

    if (trueDiv is not None) and (trueDiv is not nan):
        return floor(trueDiv)
    else:
        return nan


def doNegation(mathEntity):
    operation = negDict.get(type(mathEntity))

    if operation is not None:
        return operation(mathEntity)
    else:
        return nan


def doExponentiation(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    operation = expDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doEquality(mathEntity1, mathEntity2):
    key = (type(mathEntity1), type(mathEntity2))
    operation = eqDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
