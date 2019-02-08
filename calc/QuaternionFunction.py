from __future__ import annotations
import math
from calc.Quaternion import Quaternion
from typing import Union


def signumQuaternion(quaternion: Quaternion) -> int:
    if quaternion.real > 0:
        return 1
    elif quaternion.real < 0:
        return -1
    else:
        if quaternion.imag0 > 0:
            return 1
        elif quaternion.imag0 < 0:
            return -1
        else:
            if quaternion.imag1 > 0:
                return 1
            elif quaternion.imag1 < 0:
                return -1
            else:
                if quaternion.imag2 > 0:
                    return 1
                elif quaternion.imag2 < 0:
                    return -1
                else:
                    return 0


def expQuaternion(quaternion: Quaternion) -> Quaternion:
    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)
    magnitudeOfVectorPart = abs(vectorPart)

    return (math.e ** quaternion.real) * \
           (math.cos(magnitudeOfVectorPart) + vectorPart.normalize() * math.sin(magnitudeOfVectorPart))


def sqrtQuaternion(quaternion: Quaternion) -> Quaternion:
    return quaternion ** 0.5


def logQuaternion(quaternion: Quaternion, base: Union[int, float]=math.e) -> Quaternion:
    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)

    return math.log(abs(quaternion), base) * \
           (vectorPart / abs(vectorPart)) * math.acos(quaternion.real / abs(quaternion))


def log10Quaternion(quaternion: Quaternion) -> Quaternion:
    return logQuaternion(quaternion, 10)
