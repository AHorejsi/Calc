from calc.Vector import Vector
from calc.Matrix import Matrix


def _division(leftVector, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _vectorDividedByReal(leftVector, rightOperand)

    raise ArithmeticError("(Vector + " + _typeName(typeOfOperand) + ") is not possible")


def _vectorDividedByReal(leftVector, rightReal):
    return _vectorTimesReal(leftVector, 1 / rightReal)


def _equality(leftVector, rightOperand):
    typeOfOperand = type(rightOperand)

    if typeOfOperand is Vector:
        return _vectorEqualsVector(leftVector, rightOperand)

    return False


def _vectorEqualsVector(leftVector, rightVector):
    if not leftVector.equalDimensions(rightVector):
        return False

    for leftValue, rightValue in zip(leftVector, rightVector):
        if leftValue != rightValue:
            return False

    return True
