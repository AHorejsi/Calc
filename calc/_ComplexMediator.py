from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix
from math import sin, cos, atan, e
from calc.MathFunction import log, exp


def _addition(leftComplex, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _complexPlusReal(leftComplex, rightOperand)
    elif typeOfOperand is Complex:
        return _complexPlusComplex(leftComplex, rightOperand)
    elif typeOfOperand is Quaternion:
        return _complexPlusQuaternion(leftComplex, rightOperand)


def _complexPlusReal(leftComplex, rightReal):
    return Complex(leftComplex.real + rightReal, leftComplex.imag0)


def _complexPlusComplex(leftComplex, rightComplex):
    return Complex(leftComplex.real + rightComplex.real, leftComplex.imag0 + rightComplex.imag0)


def _complexPlusQuaternion(leftComplex, rightQuaternion):
    return Quaternion(leftComplex.real + rightQuaternion.real,
                      leftComplex.imag0 + rightQuaternion.imag0,
                      rightQuaternion.imag1,
                      rightQuaternion.imag2)


def _subtraction(leftComplex, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _complexMinusReal(leftComplex, rightOperand)
    elif typeOfOperand is Complex:
        return _complexMinusComplex(leftComplex, rightOperand)
    elif typeOfOperand is Quaternion:
        return _complexMinusQuaternion(leftComplex, rightOperand)


def _complexMinusReal(leftComplex, rightReal):
    return Complex(leftComplex.real - rightReal, leftComplex.imag0)


def _complexMinusComplex(leftComplex, rightComplex):
    return Complex(leftComplex.real - rightComplex.real, leftComplex.imag0 - rightComplex.imag0)


def _complexMinusQuaternion(leftComplex, rightQuaternion):
    return Quaternion(leftComplex.real - rightQuaternion.real,
                      leftComplex.imag0 - rightQuaternion.imag0,
                      -rightQuaternion.imag1,
                      -rightQuaternion.imag2)


def _multiplication(leftComplex, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _complexTimesReal(leftComplex, rightOperand)
    elif typeOfOperand is Complex:
        return _complexTimesComplex(leftComplex, rightOperand)
    elif typeOfOperand is Quaternion:
        return _complexTimesQuaternion(leftComplex, rightOperand)
    elif typeOfOperand is Matrix:
        return _complexTimesMatrix(leftComplex, rightOperand)


def _complexTimesReal(leftComplex, rightReal):
    return Complex(leftComplex.real * rightReal, leftComplex.imag0 * rightReal)


def _complexTimesComplex(leftComplex, rightComplex):
    return Complex(leftComplex.real * rightComplex.real - leftComplex.imag0 * rightComplex.imag0,
                   leftComplex.real * rightComplex.imag0 + leftComplex.imag0 * rightComplex.real)


def _complexTimesQuaternion(leftComplex, rightQuaternion):
    return Quaternion(leftComplex.real * rightQuaternion.real - leftComplex.imag0 * rightQuaternion.imag0,
                      leftComplex.real * rightQuaternion.imag0 + rightQuaternion.real * leftComplex.imag0,
                      leftComplex.real * rightQuaternion.imag1 - leftComplex.imag0 * rightQuaternion.imag2,
                      leftComplex.real * rightQuaternion.imag2 + leftComplex.imag0 * rightQuaternion.imag1)


def _complexTimesMatrix(leftComplex, rightMatrix):
    from calc._MatrixMediator import _matrixTimesScalar

    return _matrixTimesScalar(rightMatrix, leftComplex)


def _division(leftComplex, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _complexDividedByReal(leftComplex, rightOperand)
    elif typeOfOperand is Complex:
        return _complexDividedByComplex(leftComplex, rightOperand)
    elif typeOfOperand is Quaternion:
        return _complexDividedByQuaternion(leftComplex, rightOperand)


def _complexDividedByReal(leftComplex, rightReal):
    return _complexTimesReal(leftComplex, 1 / rightReal)


def _complexDividedByComplex(leftComplex, rightComplex):
    conj = rightComplex.conjugate()
    numerator = _complexTimesComplex(leftComplex, conj)
    denominator = (rightComplex * conj).real

    return Complex(numerator.real / denominator, numerator.imag0 / denominator)


def _complexDividedByQuaternion(leftComplex, rightQuaternion):
    absoluteValueOfRight = abs(rightQuaternion)

    realOfResult = leftComplex.real * rightQuaternion.real + leftComplex.imag0 * rightQuaternion.imag0
    imagOfResult = leftComplex.imag0 * rightQuaternion.real - leftComplex.real * rightQuaternion.imag0
    imag1OfResult = -leftComplex.real * rightQuaternion.imag1 - leftComplex.imag0 * rightQuaternion.imag2
    imag2OfResult = leftComplex.imag0 * rightQuaternion.imag1 - leftComplex.real * rightQuaternion.imag2

    return Quaternion(realOfResult / absoluteValueOfRight,
                      imagOfResult / absoluteValueOfRight,
                      imag1OfResult / absoluteValueOfRight,
                      imag2OfResult / absoluteValueOfRight)


def _equality(leftComplex, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _complexEqualsReal(leftComplex, rightOperand)
    elif typeOfOperand is Complex:
        return _complexEqualsComplex(leftComplex, rightOperand)
    elif typeOfOperand is Quaternion:
        return _complexEqualsQuaternion(leftComplex, rightOperand)

    return False


def _complexEqualsReal(leftComplex, rightReal):
    return leftComplex.real == rightReal and leftComplex.imag0 == 0


def _complexEqualsComplex(leftComplex, rightComplex):
    return leftComplex.real == rightComplex.real and leftComplex.imag0 == rightComplex.imag0


def _complexEqualsQuaternion(leftComplex, rightQuaternion):
    return leftComplex.real == rightQuaternion.real and \
           leftComplex.imag0 == rightQuaternion.imag0 and \
           rightQuaternion.imag1 == 0 and \
           rightQuaternion.imag2 == 0


def _exponent(leftComplex, rightOperand):
    typeOfOperand = type(rightOperand)

    if (typeOfOperand is int) or (typeOfOperand is float):
        return _complexToPowerOfReal(leftComplex, rightOperand)
    elif typeOfOperand is Complex:
        return _complexToPowerOfComplex(leftComplex, rightOperand)
    elif typeOfOperand is Quaternion:
        return _complexToPowerOfQuaternion(leftComplex, rightOperand)


def _complexArgument(complex):
    return atan(complex.imag0 / complex.real)


def _complexToPowerOfReal(leftComplex, rightReal):
    arg = _complexArgument(leftComplex)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2)) ** (rightReal / 2)
    value2 = cos(rightReal * arg)
    value3 = sin(rightReal * arg)

    return Complex(value1 * value2, value1 * value3)


def _complexToPowerOfComplex(leftComplex, rightComplex):
    arg = _complexArgument(leftComplex)
    value1 = ((leftComplex.real ** 2) + (leftComplex.imag0 ** 2))
    value2 = value1 ** (rightComplex.real / 2)
    value3 = e ** (-rightComplex.imag0 * arg)
    value4 = value2 * value3
    value5 = cos(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))
    value6 = sin(rightComplex.real * arg + 0.5 * rightComplex.imag0 * log(value1))

    return Complex(value4 * value5, value4 * value6)


def _complexToPowerOfQuaternion(leftComplex, rightQuaternion):
    return exp(log(leftComplex) * rightQuaternion)
