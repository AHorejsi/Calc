import math
from typing import Union
from calc.Quaternion import Quaternion


def signumQuaternion(quaternion: Quaternion) -> int:
    """
    Computes the sign of this quaternion

    :param quaternion: The quaternion whose
        sign will be computed
    :return: The sign of the given quaternion
    """

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
    """
    Returns the exponential of this quaternion

    :param quaternion: The quaternion whose
        exponential will be computed
    :return: The exponential of the given
        quaternion
    """

    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)
    magnitudeOfVectorPart = abs(vectorPart)

    return (math.e ** quaternion.real) * \
           (math.cos(magnitudeOfVectorPart) + vectorPart.normalize() * math.sin(magnitudeOfVectorPart))


def sqrtQuaternion(quaternion: Quaternion) -> Quaternion:
    """
    Computes the square root of the given quaternion

    :param quaternion: The quaternion whose square
        root will be computed
    :return: The square root of the given quaternion
    """

    return quaternion ** 0.5


def logQuaternion(quaternion: Quaternion, base: Union[int, float]=math.e) -> Quaternion:
    """
    Computes the logarithm of the given quaternion with
    given base

    :param quaternion: The quaternion that the logarithm
        will be applied to
    :param base: The base of the logarithm of the being
        computed
    :return: The logarithm of the given quaternion with
        the given base
    """

    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)

    return math.log(abs(quaternion), base) * \
           (vectorPart / abs(vectorPart)) * math.acos(quaternion.real / abs(quaternion))


def log10Quaternion(quaternion: Quaternion) -> Quaternion:
    """
    Computes the logarithm of the given quaternion
    with a base of 10

    :param quaternion: The quaternion that the
        logarithm with a base 10 will be applied to
    :return: The logarithm of the given quaternion
        with a base of 10
    """

    return logQuaternion(quaternion, 10)
