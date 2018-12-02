from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix
from math import sin, cos, acos


def _addition(leftQuaternion, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _quaternionPlusReal(leftQuaternion, rightOperand)
    elif typeOfOperand is Complex:
        return _quaternionPlusComplex(leftQuaternion, rightOperand)
    elif typeOfOperand is Quaternion:
        return _quaternionPlusQuaternion(leftQuaternion, rightOperand)


def _quaternionPlusReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real + rightReal,
                      leftQuaternion.imag0,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def _quaternionPlusComplex(leftQuaternion, rightComplex):
    from calc._ComplexMediator import _complexPlusComplex

    return _complexPlusComplex(rightComplex, leftQuaternion)


def _quaternionPlusQuaternion(leftQuaternion, rightQuaternion):
    return Quaternion(leftQuaternion.real + rightQuaternion.real,
                      leftQuaternion.imag0 + rightQuaternion.imag0,
                      leftQuaternion.imag1 + rightQuaternion.imag1,
                      leftQuaternion.imag2 + rightQuaternion.imag2)


def _subtraction(leftQuaternion, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _quaternionMinusReal(leftQuaternion, rightOperand)
    elif typeOfOperand is Complex:
        return _quaternionMinusComplex(leftQuaternion, rightOperand)
    elif typeOfOperand is Quaternion:
        return _quaternionMinusQuaternion(leftQuaternion, rightOperand)


def _quaternionMinusReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real - rightReal,
                      leftQuaternion.imag0,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def _quaternionMinusComplex(leftQuaternion, rightComplex):
    return Quaternion(leftQuaternion.real - rightComplex.real,
                      leftQuaternion.imag0 - rightComplex.imag0,
                      leftQuaternion.imag1,
                      leftQuaternion.imag2)


def _quaternionMinusQuaternion(leftQuaternion, rightQuaternion):
    return Quaternion(leftQuaternion.real - rightQuaternion.real,
                      leftQuaternion.imag0 - rightQuaternion.imag0,
                      leftQuaternion.imag1 - rightQuaternion.imag1,
                      leftQuaternion.imag2 - rightQuaternion.imag2)


def _multiplication(leftQuaternion, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _quaternionTimesReal(leftQuaternion, rightOperand)
    elif typeOfOperand is Complex:
        return _quaternionTimesComplex(leftQuaternion, rightOperand)
    elif typeOfOperand is Quaternion:
        return _quaternionTimesQuaternion(leftQuaternion, rightOperand)
    elif typeOfOperand is Matrix:
        return _quaternionTimesMatrix(leftQuaternion, rightOperand)


def _quaternionTimesReal(leftQuaternion, rightReal):
    return Quaternion(leftQuaternion.real * rightReal,
                      leftQuaternion.imag0 * rightReal,
                      leftQuaternion.imag1 * rightReal,
                      leftQuaternion.imag2 * rightReal)


def _quaternionTimesComplex(leftQuaternion, rightComplex):
    return Quaternion(leftQuaternion.real * rightComplex.real - leftQuaternion.imag0 * rightComplex.imag0,
                      leftQuaternion.real * rightComplex.imag0 + leftQuaternion.imag0 * rightComplex.real,
                      leftQuaternion.imag1 * rightComplex.real + leftQuaternion.imag2 * rightComplex.imag0,
                      -leftQuaternion.imag1 * rightComplex.imag0 + leftQuaternion.imag2 * rightComplex.real)


def _quaternionTimesQuaternion(leftQuaternion, rightQuaternion):
    return Quaternion(leftQuaternion.real * rightQuaternion.real - leftQuaternion.imag * rightQuaternion.imag -
                      leftQuaternion.imag1 * rightQuaternion.imag1 - leftQuaternion.imag2 * rightQuaternion.imag2,
                      leftQuaternion.real * rightQuaternion.imag + leftQuaternion.imag * rightQuaternion.real -
                      leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1,
                      leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag * rightQuaternion.imag2 +
                      leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag,
                      leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag * rightQuaternion.imag1 +
                      leftQuaternion.imag1 * rightQuaternion.imag + leftQuaternion.imag2 * rightQuaternion.real)


def _quaternionTimesMatrix(leftQuaternion, rightMatrix):
    from calc._MatrixMediator import _matrixTimesScalar

    return _matrixTimesScalar(rightMatrix, leftQuaternion)


def _division(leftQuaternion, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _quaternionDividedByReal(leftQuaternion, rightOperand)
    elif typeOfOperand is Complex:
        return _quaternionDividedByComplex(leftQuaternion, rightOperand)
    elif typeOfOperand is Quaternion:
        return _quaternionDividedByQuaternion(leftQuaternion, rightOperand)


def _quaternionDividedByReal(leftQuaternion, rightReal):
    return _quaternionTimesReal(leftQuaternion, 1 / rightReal)


def _quaternionDividedByComplex(leftQuaternion, rightComplex):
    conjugateOfRightComplex = rightComplex.conjugate()
    numerator = _quaternionTimesComplex(leftQuaternion, conjugateOfRightComplex)
    denominator = rightComplex * conjugateOfRightComplex
    result = _quaternionDividedByReal(numerator, denominator.real)

    return result


def _quaternionDividedByQuaternion(leftQuaternion, rightQuaternion):
    absoluteValueOfLeft = abs(rightQuaternion)

    realOfResult = leftQuaternion.real * rightQuaternion.real + leftQuaternion.imag * rightQuaternion.imag + \
                   leftQuaternion.imag1 * rightQuaternion.imag1 + leftQuaternion.imag2 * rightQuaternion.imag2
    imagOfResult = leftQuaternion.real * rightQuaternion.imag - leftQuaternion.imag * rightQuaternion.real - \
                   leftQuaternion.imag1 * rightQuaternion.imag2 + leftQuaternion.imag2 * rightQuaternion.imag1
    imag1OfResult = leftQuaternion.real * rightQuaternion.imag1 + leftQuaternion.imag * rightQuaternion.imag2 - \
                    leftQuaternion.imag1 * rightQuaternion.real - leftQuaternion.imag2 * rightQuaternion.imag
    imag2OfResult = leftQuaternion.real * rightQuaternion.imag2 - leftQuaternion.imag * rightQuaternion.imag1 + \
                    leftQuaternion.imag1 * rightQuaternion.imag - leftQuaternion.imag2 * rightQuaternion.real

    return Quaternion(realOfResult / absoluteValueOfLeft,
                      imagOfResult / absoluteValueOfLeft,
                      imag1OfResult / absoluteValueOfLeft,
                      imag2OfResult / absoluteValueOfLeft)


def _equality(leftQuaternion, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _quaternionEqualsReal(leftQuaternion, rightOperand)
    elif typeOfOperand is Complex:
        return _quaternionEqualsComplex(leftQuaternion, rightOperand)
    elif typeOfOperand is Quaternion:
        return _quaternionEqualsQuaternion(leftQuaternion, rightOperand)


def _quaternionEqualsReal(leftQuaternion, rightReal):
    return leftQuaternion.real == rightReal and \
           leftQuaternion.imag0 == 0 and \
           leftQuaternion.imag1 == 0 and \
           leftQuaternion.imag2 == 0


def _quaternionEqualsComplex(leftQuaternion, rightComplex):
    return leftQuaternion.real == rightComplex.real and \
           leftQuaternion.imag0 == rightComplex.imag0 and \
           leftQuaternion.imag1 == 0 and \
           leftQuaternion.imag2 == 0


def _quaternionEqualsQuaternion(leftQuaternion, rightQuaternion):
    return leftQuaternion.real == rightQuaternion.real and \
           leftQuaternion.imag0 == rightQuaternion.imag0 and \
           leftQuaternion.imag1 == rightQuaternion.imag1 and \
           leftQuaternion.imag2 == rightQuaternion.imag2


def _exponent(leftQuaternion, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _quaternionToPowerOfReal(leftQuaternion, rightOperand)
    elif typeOfOperand is Complex:
        pass
    elif typeOfOperand is Quaternion:
        pass


def _quaternionToPowerOfReal(leftQuaternion, rightReal):
    vectorPart = leftQuaternion.scalarAndVectorParts()[1]
    unitVector = vectorPart.normalize()
    angle = acos(leftQuaternion.real / abs(leftQuaternion))
    value1 = abs(leftQuaternion) ** rightReal
    value2 = cos(rightReal * angle)
    value3 = unitVector * sin(rightReal * angle)

    return Quaternion(value1 * value2, value1 * value3[0], value1 * value3[1], value1 * value3[2])
