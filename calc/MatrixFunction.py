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
    scipyArray = sinm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def cosMatrix(matrix: Matrix) -> Matrix:
    scipyArray = cosm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def tanMatrix(matrix: Matrix) -> Matrix:
    scipyArray = tanm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def sinhMatrix(matrix: Matrix) -> Matrix:
    scipyArray = sinhm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def coshMatrix(matrix: Matrix) -> Matrix:
    scipyArray = coshm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def tanhMatrix(matrix: Matrix) -> Matrix:
    scipyArray = tanhm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def signumMatrix(matrix: Matrix) -> Matrix:
    scipyArray = signm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)
