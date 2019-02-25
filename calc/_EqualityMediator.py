from typing import Union
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __vectorEqualsVector(leftVector: Vector, rightVector: Vector) -> bool:
    """
    Checks if the two given vectors are mathematically equal. Two
    vectors are equal if they have the same values in the same
    positions

    :param leftVector: The vector on the left side of the equality
        operator
    :param rightVector: The vector on the right side of the equality
        operator
    :return: True if both given vectors are equal, False otherwise
    """

    if not leftVector.equalDimensions(rightVector):
        return False

    for (leftValue, rightValue) in zip(leftVector, rightVector):
        if leftValue != rightValue:
            return False

    return True


def __matrixEqualsMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> bool:
    """
    Checks if the two given matrices are mathematically equal. Two
    matrices are equal if they have the same values in the same
    positions

    :param leftMatrix: The matrix on the left side of the equality
        operator
    :param rightMatrix: The matrix on the right side of the equality
        operator
    :return: True if both matrices are equal, False otherwise
    """

    if not leftMatrix.equalDimensions(rightMatrix):
        return False

    for (leftValue, rightValue) in zip(leftMatrix, rightMatrix):
        if leftValue != rightValue:
            return False

    return True


eqDict = {(int, Quaternion): lambda leftInt, rightQuaternion: leftInt == rightQuaternion.real and
                                                                    rightQuaternion.imag0 == 0 and
                                                                    rightQuaternion.imag1 == 0 and
                                                                    rightQuaternion.imag2 == 0,
          (float, Quaternion): lambda leftFloat, rightQuaternion: leftFloat == rightQuaternion.real and
                                                                        rightQuaternion.imag0 == 0 and
                                                                        rightQuaternion.imag1 == 0 and
                                                                        rightQuaternion.imag2 == 0,
          (complex, Quaternion): lambda leftComplex, rightQuaternion: leftComplex.real == rightQuaternion.real and
                                                                      leftComplex.imag == rightQuaternion.imag0 and
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
          (Quaternion, complex): lambda leftQuaternion, rightComplex: leftQuaternion.real == rightComplex.real and
                                                                            leftQuaternion.imag0 == rightComplex.imag and
                                                                            leftQuaternion.imag1 == 0 and
                                                                            leftQuaternion.imag2 == 0,
          (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: leftQuaternion.real == rightQuaternion.real and
                                                                            leftQuaternion.imag0 == rightQuaternion.imag0 and
                                                                            leftQuaternion.imag1 == rightQuaternion.imag1 and
                                                                            leftQuaternion.imag2 == rightQuaternion.imag2,
          (NumberList, NumberList): __numberListEqualsNumberList,
          (Vector, Vector): __vectorEqualsVector,
          (Matrix, Matrix): __matrixEqualsMatrix}


def doEquality(mathEntity1: Union[int, float, MathEntity],
               mathEntity2: Union[int, float, MathEntity]) -> bool:
    """
    Checks if the two mathematical entities are mathematically
    equal

    :param mathEntity1: The mathematical entity on the left side
        of the equality operator
    :param mathEntity2: The mathematical entity on the right side
        of the equality operator
    :return: True if the two given mathematical entities are equal,
        False otherwise
    """

    key = (type(mathEntity1), type(mathEntity2))
    operation = eqDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return False
