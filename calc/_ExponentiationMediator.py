from typing import Union
from math import nan, e, log, sin, cos, atan
from copy import deepcopy
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix


def __matrixToPowerOfInt(leftMatrix: Matrix, rightInt: int) -> Matrix:
    """
    Takes the given matrix to the power of the given integer

    :param leftMatrix: The matrix on the left side of the
        exponentiation sign
    :param rightInt: The integer on the right side of the
        exponentiation sign
    :return: The result of taking the given matrix to the
        power of the given integer
    """

    if rightInt > 0:
        newMatrix = deepcopy(leftMatrix)

        for iteration in range(rightInt):
            newMatrix *= leftMatrix

        return newMatrix
    else:
        return __generalExponent(leftMatrix, rightInt)


def __matrixToPowerOfMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> Matrix:
    """
    Takes the first given matrix to the power of the second
    given matrix

    :param leftMatrix: The matrix on the left side of the
        exponentiation sign
    :param rightMatrix: The matrix on the right side of the
        exponentiation sign
    :return: The result of taking the first given matrix to
        the power of the second given matrix
    """

    result = __generalExponent(leftMatrix, rightMatrix)
    newTable = []

    if type(result) is Matrix:
        return Matrix.createMatrixFrom1DList(newTable, leftMatrix.rowLength, leftMatrix.columnLength)
    else:
        return result


def __generalExponent(leftEntity: Union[int, float, Complex, Quaternion, Matrix],
                      rightEntity: Union[int, float, Complex, Quaternion, Matrix]) -> Union[MathEntity, float]:
    """
    Takes the first given mathematical entity to the power of
    the second mathematical entity

    :param leftEntity: The mathematical entity on the left side
        of the exponentiation sign
    :param rightEntity: The mathematical entity on the right side
        of the exponentiation sign
    :return: The result of taking the first given mathematical
        entity to the power of the second mathematical entity
    """

    from calc.MathFunction import expMath, logMath

    try:
        return expMath(logMath(leftEntity) * rightEntity)
    except ValueError:
        return nan
    except AttributeError:
        return nan
    except TypeError:
        return nan


expDict = {(int, Quaternion): __generalExponent,
           (int, Matrix): __generalExponent,
           (float, Quaternion): __generalExponent,
           (float, Matrix): __generalExponent,
           (complex, Quaternion): __generalExponent,
           (Quaternion, int): __generalExponent,
           (Quaternion, float): __generalExponent,
           (Quaternion, complex): __generalExponent,
           (Quaternion, Quaternion): __generalExponent,
           (Matrix, int): __matrixToPowerOfInt,
           (Matrix, float): __generalExponent,
           (Matrix, complex): __generalExponent,
           (Matrix, Quaternion): __generalExponent,
           (Matrix, Matrix): __matrixToPowerOfMatrix}


def doExponentiation(mathEntity1: Union[int, float, MathEntity],
                     mathEntity2: Union[int, float, MathEntity]) -> Union[MathEntity, float]:
    """
    Takes the first given mathematical entity to the power of
    the second mathematical entity. If such an operation is
    not possible, nan is returned

    :param mathEntity1: The mathematical entity on the left side
        of the exponentiation sign
    :param mathEntity2: The mathematical entity on the right side
        of the exponentiation sign
    :return: The result of taking the first given mathematical
        entity to the power of the second mathematical entity.
        If such an operation cannot be performed, nan is
        returned
    """

    key = (type(mathEntity1), type(mathEntity2))
    operation = expDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
