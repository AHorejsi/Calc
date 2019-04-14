from typing import Union
from math import nan
from copy import deepcopy
from itertools import zip_longest
from calc.entities.MathEntity import MathEntity
from calc.entities.Quaternion import Quaternion
from calc.stats.NumberList import NumberList
from calc.entities.Matrix import Matrix


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


def __generalExponent(leftEntity: Union[int, float, complex, Quaternion, Matrix],
                      rightEntity: Union[int, float, complex, Quaternion, Matrix]) -> Union[MathEntity, float]:
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
           (int, NumberList): lambda leftInt, rightList: NumberList([leftInt ** value for value in rightList]),
           (int, Matrix): __generalExponent,
           (float, Quaternion): __generalExponent,
           (float, NumberList): lambda leftFloat, rightList: NumberList([leftFloat ** value for value in rightList]),
           (float, Matrix): __generalExponent,
           (complex, Quaternion): __generalExponent,
           (complex, NumberList): lambda leftComplex, rightList: NumberList([leftComplex ** value for value in rightList]),
           (Quaternion, int): __generalExponent,
           (Quaternion, float): __generalExponent,
           (Quaternion, complex): __generalExponent,
           (Quaternion, Quaternion): __generalExponent,
           (Quaternion, NumberList): lambda leftQuaternion, rightList: NumberList([leftQuaternion ** value for value in rightList]),
           (NumberList, int): lambda leftList, rightInt: NumberList([value ** rightInt for value in leftList]),
           (NumberList, float): lambda leftList, rightFloat: NumberList([value ** rightFloat for value in leftList]),
           (NumberList, complex): lambda leftList, rightComplex: NumberList([value ** rightComplex for value in leftList]),
           (NumberList, Quaternion): lambda leftList, rightQuaternion: NumberList([value ** rightQuaternion for value in leftList]),
           (NumberList, NumberList): lambda leftList, rightList: NumberList([leftValue ** rightValue
                                                                             for (leftValue, rightValue)
                                                                             in zip_longest(leftList, rightList, fillvalue=0)]),
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
