from calc.Matrix import Matrix
from calc.Complex import Complex
from scipy.linalg import expm, logm, sinm, cosm, tanm, sinhm, coshm, tanhm, signm
import scipy


def _createScipyArray(matrix: Matrix) -> scipy.ndarray:
    table = []

    for rowIndex in range(matrix.rowLength):
        row = []

        for columnIndex in range(matrix.columnLength):
            row.append(matrix[(rowIndex, columnIndex)])

        table.append(row)

    return scipy.array(table)


def _replaceBuiltInComplex(scipyArray: scipy.ndarray, rowLength: int, columnLength: int) -> Matrix:
    newTable = []

    for rowIndex in range(rowLength):
        for columnIndex in range(columnLength):
            if type(scipyArray[(rowIndex, columnIndex)]) is complex:
                com = Complex.fromBuiltInComplex(scipyArray[(rowIndex, columnIndex)])
                newTable.append(com)

    return Matrix.createMatrixFrom1DList(newTable, rowLength, columnLength)


def expMatrix(matrix: Matrix) -> Matrix:
    scipyArray = expm(_createScipyArray(matrix))
    return Matrix(scipyArray.tolist())


def logMatrix(matrix: Matrix) -> Matrix:
    scipyArray = logm(_createScipyArray(matrix))
    return Matrix(scipyArray.tolist())


def sqrtMatrix(matrix: Matrix) -> Matrix:
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
