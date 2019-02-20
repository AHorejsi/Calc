from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


negDict = {Quaternion: lambda quaternion: Quaternion(-quaternion.real, -quaternion.imag0,
                                                     -quaternion.imag1, -quaternion.imag2),
           Vector: lambda vector: Vector([-value for value in vector]),
           Matrix: lambda matrix: Matrix.createMatrixFrom1DList([-value for value in matrix],
                                                                matrix.rowLength,
                                                                matrix.columnLength)}


def doNegation(mathEntity: MathEntity) -> Union[MathEntity, float]:
    """
    Computes the negation of the given mathematical entity.
    If the given mathematical entity cannot be negated, nan
    is returned

    :param mathEntity: The mathematical entity to be negated
    :return: The negation of the given mathematical entity if
        it can be negated. If it cannot be negated, nan is returned
    """

    operation = negDict.get(type(mathEntity))

    if operation is not None:
        return operation(mathEntity)
    else:
        return nan
