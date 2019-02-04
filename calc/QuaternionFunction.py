from __future__ import annotations
import math
from calc.Quaternion import Quaternion
from typing import Union


def expQuaternion(quaternion: Quaternion) -> Quaternion:
    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)
    magnitudeOfVectorPart = abs(vectorPart)

    return (math.e ** quaternion.real) * (math.cos(magnitudeOfVectorPart) + vectorPart.normalize() * math.sin(magnitudeOfVectorPart))


def sqrtQuaternion(quaternion: Quaternion) -> Quaternion:
    return quaternion ** 0.5


def logQuaternion(quaternion: Quaternion, base: Union[int, float]=math.e) -> Quaternion:
    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)

    return math.log(abs(quaternion), base) * (vectorPart / abs(vectorPart)) * math.acos(quaternion.real / abs(quaternion))


def log10Quaternion(quaternion: Quaternion) -> Quaternion:
    return logQuaternion(quaternion, 10)


def floorQuaternion(quaternion: Quaternion) -> Quaternion:
    return quaternion.__floor__()


def ceilQuaternion(quaternion: Quaternion) -> Quaternion:
    return quaternion.__ceil__()
