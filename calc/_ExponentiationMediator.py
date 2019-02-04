from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


def __realToPowerOfComplex(leftReal: Union[int, float], rightComplex: Complex) -> Complex:
    value1 = (leftReal ** 2) ** (rightComplex.real / 2)
    value2 = cos(log(leftReal))
    value3 = sin(log(leftReal))

    return Complex(value1 * value2, value1 * value3)


def __complexToPowerOfReal(leftComplex: Complex, rightReal: Union[int, float]) -> Complex:
    arg = atan(leftComplex.imag0 / leftComplex.real)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2)) ** (rightReal / 2)
    value2 = cos(rightReal * arg)
    value3 = sin(rightReal * arg)

    return Complex(value1 * value2, value1 * value3)


def __complexToPowerOfComplex(leftComplex: Complex, rightComplex: Complex) -> Complex:
    arg = atan(leftComplex.imag0 / leftComplex.real)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2))
    value2 = value1 ** (rightComplex.real / 2)
    value3 = e ** (-rightComplex.imag0 * arg)
    value4 = value2 * value3
    value5 = cos(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))
    value6 = sin(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))

    return Complex(value4 * value5, value4 * value6)


def __matrixToPowerOfInt(leftMatrix: Matrix, rightInt: int) -> Matrix:
    newMatrix = deepcopy(leftMatrix)

    for iteration in range(rightInt):
        newMatrix *= leftMatrix

    return newMatrix


def __matrixToPowerOfFloat(leftMatrix: Matrix, rightFloat: Union[int, float]) -> Matrix:
    if rightFloat.is_integer():
        return __matrixToPowerOfInt(leftMatrix, rightFloat)
    else:
        return __generalExponent(leftMatrix, rightFloat)


def __matrixToPowerOfMatrix(leftMatrix: Matrix, rightMatrix: Matrix) -> Matrix:
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
    key = (type(mathEntity1), type(mathEntity2))
    operation = expDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return nan
