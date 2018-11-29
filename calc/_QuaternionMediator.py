from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix


def _addition(leftQuaternion, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _quaternionPlusReal(leftQuaternion, rightOperand)


def _quaternionPlusReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real + rightReal,
                      leftQuaternion.imag0,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)
