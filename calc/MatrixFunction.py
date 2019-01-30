from calc.Matrix import Matrix
from calc.Complex import Complex
from scipy.linalg import expm, logm, sinm, cosm, tanm, sinhm, coshm, tanhm
import scipy


def _createScipyArray(matrix):
    table = []

    for rowIndex in range(matrix.rowLength):
        row = []

        for columnIndex in range(matrix.columnLength):
            row.append(matrix[(rowIndex, columnIndex)])

        table.append(row)

    return scipy.array(table)


def _replaceBuiltInComplex(scipyArray, rowLength, columnLength):
    newTable = []

    for rowIndex in range(rowLength):
        for columnIndex in range(columnLength):
            if type(scipyArray[(rowIndex, columnIndex)]) is complex:
                com = Complex.fromBuiltInComplex(scipyArray[(rowIndex, columnIndex)])
                newTable.append(com)

    return Matrix(newTable, rowLength, columnLength)


def expMatrix(matrix):
    scipyArray = expm(_createScipyArray(matrix))
    return Matrix(scipyArray.tolist())


def logMatrix(matrix):
    scipyArray = logm(_createScipyArray(matrix))
    return Matrix(scipyArray.tolist())


def sqrtMatrix(matrix):
    result = matrix ** 0.5


def sinMatrix(matrix):
    scipyArray = sinm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def cosMatrix(matrix):
    scipyArray = cosm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def tanMatrix(matrix):
    scipyArray = tanm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def sinhMatrix(matrix):
    scipyArray = sinhm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def coshMatrix(matrix):
    scipyArray = coshm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)


def tanhMatrix(matrix):
    scipyArray = tanhm(_createScipyArray(matrix))
    return _replaceBuiltInComplex(Matrix(scipyArray.tolist()), matrix.rowLength, matrix.columnLength)
