from typing import Union
from math import nan, e, log, sin, cos, atan
from copy import deepcopy
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix


def __realToPowerOfComplex(leftReal: Union[int, float], rightComplex: Complex) -> Complex:
    """
    Takes the given real number to the power of the given
    complex number

    :param leftReal: The real number on the left side of
        the exponentiation sign
    :param rightComplex: The complex number on the right
        side of the exponentiation sign
    :return: The result of taking the given real number
        to the power of the given complex number
    """

    value1 = (leftReal ** 2) ** (rightComplex.real / 2)
    value2 = cos(log(leftReal))
    value3 = sin(log(leftReal))

    return Complex(value1 * value2, value1 * value3)


def __complexToPowerOfReal(leftComplex: Complex, rightReal: Union[int, float]) -> Complex:
    """
    Takes the given complex number to the power of the given real
    number

    :param leftComplex: The complex number on the left side of the
        exponentiation sign
    :param rightReal: The real number on the right side of the
        exponentiation sign
    :return: The result of taking the given complex number to the
        power of the given real number
    """

    arg = atan(leftComplex.imag0 / leftComplex.real)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2)) ** (rightReal / 2)
    value2 = cos(rightReal * arg)
    value3 = sin(rightReal * arg)

    return Complex(value1 * value2, value1 * value3)


def __complexToPowerOfComplex(leftComplex: Complex, rightComplex: Complex) -> Complex:
    """
    Takes the first given complex number to the power of the second
    given complex number

    :param leftComplex: The complex number on the left side of the
        exponentiation sign
    :param rightComplex: The complex number on the right side of the
        exponentiation sign
    :return: The result of taking the first given complex number to
        the power of the second given complex number
    """

    arg = atan(leftComplex.imag0 / leftComplex.real)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2))
    value2 = value1 ** (rightComplex.real / 2)
    value3 = e ** (-rightComplex.imag0 * arg)
    value4 = value2 * value3
    value5 = cos(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))
    value6 = sin(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))

    return Complex(value4 * value5, value4 * value6)


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


def __matrixToPowerOfFloat(leftMatrix: Matrix, rightFloat: Union[int, float]) -> Matrix:
    """
    Takes the given matrix to the power of the given float

    :param leftMatrix: The matrix on the left side of the
        exponentiation sign
    :param rightFloat: The float on the right side of the
        exponentiation sign
    :return: The result of taking the given matrix to the
        power of the given float
    """

    if rightFloat.is_integer() and rightFloat > 0:
        return __matrixToPowerOfInt(leftMatrix, rightFloat)
    else:
        return __generalExponent(leftMatrix, rightFloat)


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
        for rowIndex in range(leftMatrix.rowLength):
            for columnIndex in range(leftMatrix.columnLength):
                if type(result[(rowIndex, columnIndex)]) is complex:
                    com = Complex.fromBuiltInComplex(result[(rowIndex, columnIndex)])
                    newTable.append(com)

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


expDict = {(int, Complex): __realToPowerOfComplex,
           (int, Quaternion): __generalExponent,
           (int, Matrix): __generalExponent,
           (float, Complex): __realToPowerOfComplex,
           (float, Quaternion): __generalExponent,
           (float, Matrix): __generalExponent,
           (Complex, int): __complexToPowerOfReal,
           (Complex, float): __complexToPowerOfReal,
           (Complex, Complex): __complexToPowerOfComplex,
           (Complex, Quaternion): __generalExponent,
           (Quaternion, int): __generalExponent,
           (Quaternion, float): __generalExponent,
           (Quaternion, Complex): __generalExponent,
           (Quaternion, Quaternion): __generalExponent,
           (Matrix, int): __matrixToPowerOfInt,
           (Matrix, float): __matrixToPowerOfFloat,
           (Matrix, Complex): __generalExponent,
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
