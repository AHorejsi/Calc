from math import nan, floor
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


addDict = {(int, "+", int): lambda leftInt, rightInt: leftInt + rightInt,
           (int, "+", float): lambda leftInt, rightFloat: leftInt + rightFloat,
           (int, "+", Complex): lambda leftInt, rightComplex: Complex(leftInt + rightComplex.real,
                                                                      rightComplex.imag0),
           (int, "+", Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt + rightQuaternion.real,
                                                                               rightQuaternion.imag0,
                                                                               rightQuaternion.imag1,
                                                                               rightQuaternion.imag2),
           (float, "+", int): lambda leftFloat, rightInt: leftFloat + rightInt,
           (float, "+", float): lambda leftFloat, rightFloat: leftFloat + rightFloat,
           (float, "+", Complex): lambda leftFloat, rightComplex: Complex(leftFloat + rightComplex.real,
                                                                          rightComplex.imag0),
           (float, "+", Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat + rightQuaternion.real,
                                                                                   rightQuaternion.imag0,
                                                                                   rightQuaternion.imag1,
                                                                                   rightQuaternion.imag2),
           (Complex, "+", int): lambda leftComplex, rightInt: Complex(leftComplex.real + rightInt,
                                                                      leftComplex.imag0),
           (Complex, "+", float): lambda leftComplex, rightFloat: Complex(leftComplex.real + rightFloat,
                                                                          leftComplex.imag0),
           (Complex, "+", Complex): lambda leftComplex, rightComplex: Complex(leftComplex.real + rightComplex.real,
                                                                              leftComplex.imag0 + rightComplex.imag0),
           (Complex, "+", Quaternion): lambda leftComplex, rightQuaternion: Quaternion(leftComplex.real + rightQuaternion.real,
                                                                                       leftComplex.imag0 + rightQuaternion.imag0,
                                                                                       rightQuaternion.imag1,
                                                                                       rightQuaternion.imag2),
           (Quaternion, "+", int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real + rightInt,
                                                                               leftQuaternion.imag0,
                                                                               leftQuaternion.imag1,
                                                                               leftQuaternion.imag2),
           (Quaternion, "+", float): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real + rightComplex.real,
                                                                                     leftQuaternion.imag0 + rightComplex.imag0,
                                                                                     leftQuaternion.imag1,
                                                                                     leftQuaternion.imag2),
           (Quaternion, "+", Complex): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real + rightComplex.real,
                                                                                       leftQuaternion.imag0 + rightComplex.imag0,
                                                                                       leftQuaternion.imag1,
                                                                                       leftQuaternion.imag2),
           (Quaternion, "+", Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(leftQuaternion.real + rightQuaternion.real,
                                                                                             leftQuaternion.imag0 + rightQuaternion.imag0,
                                                                                             leftQuaternion.imag1 + rightQuaternion.imag1,
                                                                                             leftQuaternion.imag2 + rightQuaternion.imag2)}

subtDict = {(int, "-", int): lambda leftInt, rightInt: leftInt - rightInt,
            (int, "-", float): lambda leftInt, rightFloat: leftInt - rightFloat,
            (int, "-", Complex): lambda leftInt, rightComplex: Complex(leftInt - rightComplex.real,
                                                                       -rightComplex.imag0),
            (int, "-", Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt - rightQuaternion.real,
                                                                                -rightQuaternion.imag0,
                                                                                -rightQuaternion.imag1,
                                                                                -rightQuaternion.imag2),
            (float, "-", int): lambda leftFloat, rightInt: leftFloat - rightInt,
            (float, "-", float): lambda leftFloat, rightFloat: leftFloat - rightFloat,
            (float, "-", Complex): lambda leftFloat, rightComplex: Complex(leftFloat - rightComplex.real,
                                                                           -rightComplex.imag0),
            (float, "-", Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat - rightQuaternion.real,
                                                                                    -rightQuaternion.imag0,
                                                                                    -rightQuaternion.imag1,
                                                                                    -rightQuaternion.imag2),
            (Complex, "-", int): lambda leftComplex, rightInt: Complex(leftComplex.real - rightInt,
                                                                       leftComplex.imag0),
            (Complex, "-", float): lambda leftComplex, rightFloat: Complex(leftComplex.real - rightFloat,
                                                                           leftComplex.imag0),
            (Complex, "-", Complex): lambda leftComplex, rightComplex: Complex(leftComplex.real - rightComplex.real,
                                                                               leftComplex.imag0 - rightComplex.imag0),
            (Complex, "-", Quaternion): lambda leftComplex, rightQuaternion: Quaternion(leftComplex.real - rightQuaternion.real,
                                                                                        leftComplex.imag0 - rightQuaternion.imag0,
                                                                                        -rightQuaternion.imag1,
                                                                                        -rightQuaternion.imag2),
            (Quaternion, "-", int): lambda leftQuaternion, rightInt: Quaternion(leftQuaternion.real - rightInt,
                                                                                leftQuaternion.imag0,
                                                                                leftQuaternion.imag1,
                                                                                leftQuaternion.imag2),
            (Quaternion, "-", float): lambda leftQuaternion, rightFloat: Quaternion(leftQuaternion.real - rightFloat,
                                                                                    leftQuaternion.imag0,
                                                                                    leftQuaternion.imag1,
                                                                                    leftQuaternion.imag2),
            (Quaternion, "-", Complex): lambda leftQuaternion, rightComplex: Quaternion(leftQuaternion.real - rightComplex.real,
                                                                                        leftQuaternion.imag0 - rightComplex.imag0,
                                                                                        leftQuaternion.imag1,
                                                                                        leftQuaternion.imag2),
            (Quaternion, "-", Quaternion): lambda leftQuaternion, rightQuaternion: Quaternion(leftQuaternion.real - rightQuaternion.real,
                                                                                              leftQuaternion.imag0 - rightQuaternion.imag0,
                                                                                              leftQuaternion.imag1 - rightQuaternion.imag1,
                                                                                              leftQuaternion.imag2 - rightQuaternion.imag2)}

multDict = {(int, "*", int): lambda leftInt, rightInt: leftInt * rightInt,
            (int, "*", float): lambda leftInt, rightFloat: leftInt * rightFloat,
            (int, "*", Complex): lambda leftInt, rightComplex: Complex(leftInt * rightComplex.real,
                                                                       leftInt * rightComplex.imag0),
            (int, "*", Quaternion): lambda leftInt, rightQuaternion: Quaternion(leftInt * rightQuaternion.real,
                                                                                leftInt * rightQuaternion.imag0,
                                                                                leftInt * rightQuaternion.imag1,
                                                                                leftInt * rightQuaternion.imag2),
            (float, "*", int): lambda leftFloat, rightInt: leftFloat * rightInt,
            (float, "*", float): lambda leftFloat, rightFloat: leftFloat * rightFloat,
            (float, "*", Complex): lambda leftInt, rightComplex: Complex(leftInt * rightComplex.real,
                                                                         leftInt * rightComplex.imag0),
            (float, "*", Quaternion): lambda leftFloat, rightQuaternion: Quaternion(leftFloat * rightQuaternion.real,
                                                                                    leftFloat * rightQuaternion.imag0,
                                                                                    leftFloat * rightQuaternion.imag1,
                                                                                    leftFloat * rightQuaternion.imag2)}

divDict = {(int, "/", int): lambda leftInt, rightInt: leftInt / rightInt,
           (int, "/", float): lambda leftInt, rightFloat: leftInt / rightFloat,
           (float, "/", int): lambda leftFloat, rightInt: leftFloat / rightInt,
           (float, "/", float): lambda leftFloat, rightFloat: leftFloat / rightFloat}

negDict = {("-", int): lambda int: -int,
           ("-", float): lambda float: -float,
           ("-", Complex): lambda complex: Complex(-complex.real, -complex.imag0),
           ("-", Quaternion): lambda quaternion: Quaternion(-quaternion.real, -quaternion.imag0,
                                                            -quaternion.imag1, -quaternion.imag2),
           ("-", Vector): lambda vector: Vector([-value for value in vector]),
           ("-", Matrix): lambda matrix: Matrix([-value for value in matrix])}

eqDict = {(int, "==", int): lambda leftInt, rightInt: leftInt == rightInt,
          (int, "==", float): lambda leftInt, rightFloat: leftInt == rightFloat,
          (int, "==", Complex): lambda leftInt, rightComplex: leftInt == rightComplex.real and
                                                              rightComplex.imag0 == 0,
          (int, "==", Quaternion): lambda leftInt, rightQuaternion: leftInt == rightQuaternion.real and
                                                                    rightQuaternion.imag0 == 0 and
                                                                    rightQuaternion.imag1 == 0 and
                                                                    rightQuaternion.imag2 == 0,
          (float, "==", int): lambda leftFloat, rightInt: leftFloat == rightInt,
          (float, "==", float): lambda leftFloat, rightFloat: leftFloat == rightFloat,
          (float, "==", Complex): lambda leftFloat, rightComplex: leftFloat == rightComplex.real and
                                                                  rightComplex.imag0 == 0,
          (float, "==", Quaternion): lambda leftFloat, rightQuaternion: leftFloat == rightQuaternion.real and
                                                                        rightQuaternion.imag0 == 0 and
                                                                        rightQuaternion.imag1 == 0 and
                                                                        rightQuaternion.imag2 == 0,
          (Complex, "==", int): lambda leftComplex, rightInt: leftComplex.real == rightInt and
                                                              leftComplex.imag0 == 0,
          (Complex, "==", float): lambda leftComplex, rightFloat: leftComplex.real == rightFloat and
                                                                  leftComplex.imag0 == 0,
          (Complex, "==", Complex): lambda leftComplex, rightComplex: leftComplex.real == rightComplex.real and
                                                                      leftComplex.imag0 == rightComplex.imag0,
          (Complex, "==", Quaternion): lambda leftComplex, rightQuaternion: leftComplex.real == rightQuaternion.real and
                                                                            leftComplex.imag0 == rightQuaternion.imag0 and
                                                                            leftComplex.imag1 == 0 and
                                                                            leftComplex.imag2 == 0,
          (Quaternion, "==", int): lambda leftQuaternion, rightInt: leftQuaternion.real == rightInt and
                                                                    leftQuaternion.imag0 == 0 and
                                                                    leftQuaternion.imag1 == 0 and
                                                                    leftQuaternion.imag2 == 0,
          (Quaternion, "==", float): lambda leftQuaternion, rightFloat: leftQuaternion.real == rightFloat and
                                                                        leftQuaternion.imag0 == 0 and
                                                                        leftQuaternion.imag1 == 0 and
                                                                        leftQuaternion.imag2 == 0,
          (Quaternion, "==", Complex): lambda leftQuaternion, rightComplex: leftQuaternion.real == rightComplex.real and
                                                                            leftQuaternion.imag0 == rightComplex.imag0 and
                                                                            leftQuaternion.imag1 == 0 and
                                                                            leftQuaternion.imag2 == 0,
          (Quaternion, "==", Quaternion): lambda leftQuaternion, rightQuaternion: leftQuaternion.real == rightQuaternion.real and
                                                                                  leftQuaternion.imag0 == rightQuaternion.imag0 and
                                                                                  leftQuaternion.imag1 == rightQuaternion.imag1 and
                                                                                  leftQuaternion.imag2 == rightQuaternion.imag2,
          (bool, "==", bool): lambda leftBool, rightBool: leftBool == rightBool}


def doAddition(mathEntity1, mathEntity2):
    key = (type(mathEntity1), "+", type(mathEntity2))
    operation = addDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doSubtraction(mathEntity1, mathEntity2):
    key = (type(mathEntity1), "-", type(mathEntity2))
    operation = subtDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doMultiplication(mathEntity1, mathEntity2):
    key = (type(mathEntity1), "*", type(mathEntity2))
    operation = multDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan


def doDivision(mathEntity1, mathEntity2):
    key = (type(mathEntity1), "/", type(mathEntity2))
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
    key = ("-", type(mathEntity))
    operation = negDict.get(key)

    if operation is not None:
        return operation(mathEntity)
    else:
        return nan


def doExponentiation(mathEntity1, mathEntity2):
    from calc.MathFunction import exp, log

    return exp(log(mathEntity1) * mathEntity2)


def doEquality(mathEntity1, mathEntity2):
    key = (type(mathEntity1), "==", mathEntity2)
    operation = eqDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
