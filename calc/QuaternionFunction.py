import math
from calc.Quaternion import Quaternion


def expQuaternion(quaternion):
    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)
    magnitudeOfVectorPart = abs(vectorPart)

    return (math.e ** quaternion.real) * (math.cos(magnitudeOfVectorPart) + vectorPart.normalize() * math.sin(magnitudeOfVectorPart))


def sqrtQuaternion(quaternion):
    return quaternion ** 0.5


def logQuaternion(quaternion, base=math.e):
    vectorPart = Quaternion(0, quaternion.imag0, quaternion.imag1, quaternion.imag2)

    return math.log(abs(quaternion), base) * (vectorPart / abs(vectorPart)) * math.acos(quaternion.real / abs(quaternion))


def log10Quaternion(quaternion):
    return logQuaternion(quaternion, 10)


def floorQuaternion(quaternion):
    return math.floor(quaternion)


def ceilQuaternion(quaternion):
    return math.ceil(quaternion)
