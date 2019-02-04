from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


negDict = {Complex: lambda complex: Complex(-complex.real, -complex.imag0),
           Quaternion: lambda quaternion: Quaternion(-quaternion.real, -quaternion.imag0,
                                                     -quaternion.imag1, -quaternion.imag2),
           Vector: lambda vector: Vector([-value for value in vector]),
           Matrix: lambda matrix: Matrix.createMatrixFrom1DList([-value for value in matrix],
                                                                matrix.rowLength,
                                                                matrix.columnLength)}


def doNegation(mathEntity: MathEntity) -> Union[MathEntity, float]:
    operation = negDict.get(type(mathEntity))

    if operation is not None:
        return operation(mathEntity)
    else:
        return nan
