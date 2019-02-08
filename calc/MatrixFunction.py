from calc.Matrix import Matrix
from calc.Complex import Complex
from scipy.linalg import expm, logm, sinm, cosm, tanm, sinhm, coshm, tanhm, signm
import scipy


def _createScipyArray(matrix: Matrix) -> scipy.ndarray:
    """
    Places the elements of a given matrix into an
    ndarray

    :param matrix: The matrix whose elements will
        be placed into a an ndarray
    :return: An ndarray with the same dimensions
        and elements as the given matrix
    """

    table = []

    for rowIndex in range(matrix.rowLength):
        row = []

        for columnIndex in range(matrix.columnLength):
            row.append(matrix[(rowIndex, columnIndex)])

        table.append(row)

    return scipy.array(table)


def _replaceBuiltInComplex(scipyArray: scipy.ndarray, rowLength: int, columnLength: int) -> Matrix:
    """
    Places the elements of a given ndarray into a matrix

    :param scipyArray: The ndarray to have its elements placed
        into a matrix
    :param rowLength: The number of rows the ndarray has
    :param columnLength: The number of coumns the ndarray has
    :return: A matrix with the same dimensions and elements
        as the given ndarray
    """

    newTable = []

    for rowIndex in range(rowLength):
        for columnIndex in range(columnLength):
            if type(scipyArray[(rowIndex, columnIndex)]) is complex:
                com = Complex.fromBuiltInComplex(scipyArray[(rowIndex, columnIndex)])
                newTable.append(com)

    return Matrix.createMatrixFrom1DList(newTable, rowLength, columnLength)


def expMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the exponential of the given
    matrix

    :param matrix: The matrix whose exponential
        will be computed
    :return: The exponential of the given matrix
    """

    scipyArray = expm(_createScipyArray(matrix))
    return Matrix(scipyArray.tolist())


def logMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the logarithm of the given
    matrix

    :param matrix: The matrix whose logarithm
        will be computed
    :return: The logarithm of the given matrix
    """

    scipyArray = logm(_createScipyArray(matrix))
    return Matrix(scipyArray.tolist())


def sqrtMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the square root of the given matrix

    :param matrix: The matrix whose square root
        will be computed
    :return: The square root of the given matrix
    """

    return matrix ** 0.5


def sinMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the sine of the given matrix

    :param matrix: The matrix which will
        have the sine function applied to
        it
    :return: The sine of the given matrix
    """

    scipyArray = sinm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def cosMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the cosine of the given matrix

    :param matrix: The matrix which will
        have the cosine function applied to
        it
    :return: The cosine of the given matrix
    """

    scipyArray = cosm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def tanMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the tangent of the given matrix

    :param matrix: The matrix which will
        have the tangent function applied to
        it
    :return: The tangent of the given matrix
    """

    scipyArray = tanm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def sinhMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the hyperbolic sine of the given matrix

    :param matrix: The matrix which will
        have the hyperbolic sine function applied to
        it
    :return: The hyperbolic sine of the given matrix
    """

    scipyArray = sinhm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def coshMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the hyperbolic cosine of the given matrix

    :param matrix: The matrix which will
        have the hyperbolic cosine function applied to
        it
    :return: The hyperbolic cosine of the given matrix
    """

    scipyArray = coshm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def tanhMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the hyperbolic tangent of the given matrix

    :param matrix: The matrix which will
        have the hyperbolic tangent function applied to
        it
    :return: The hyperbolic tangent of the given matrix
    """

    scipyArray = tanhm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()))


def signumMatrix(matrix: Matrix) -> Matrix:
    """
    Computes the sign of the given matrix

    :param matrix: The matrix whose sign
        will be computed
    :return: The sign of the given matrix
    """

    scipyArray = signm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)
