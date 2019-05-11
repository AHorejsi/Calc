import math
import cmath
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix
from calc.QuaternionFunction import expQuaternion, sqrtQuaternion, logQuaternion, log10Quaternion, signumQuaternion
from calc.MatrixFunction import expMatrix, logMatrix, sqrtMatrix, sinMatrix, cosMatrix, tanMatrix, sinhMatrix, \
                                coshMatrix, tanhMatrix, signumMatrix
from typing import Union


functionDictionary = {("exp", int): math.exp,
                      ("exp", float): math.exp,
                      ("exp", complex): cmath.exp,
                      ("exp", Quaternion): expQuaternion,
                      ("exp", Matrix): expMatrix,
                      ("log", int): math.log,
                      ("log", float): math.log,
                      ("log", complex): cmath.log,
                      ("log", Quaternion): logQuaternion,
                      ("log", Matrix): logMatrix,
                      ("log10", int): math.log10,
                      ("log10", float): math.log10,
                      ("log10", complex): cmath.log10,
                      ("log10", Quaternion): log10Quaternion,
                      ("sqrt", int): math.sqrt,
                      ("sqrt", float): math.sqrt,
                      ("sqrt", complex): cmath.sqrt,
                      ("sqrt", Quaternion): sqrtQuaternion,
                      ("sqrt", Matrix): sqrtMatrix,
                      ("sin", int): math.sin,
                      ("sin", float): math.sin,
                      ("sin", complex): cmath.sin,
                      ("sin", Matrix): sinMatrix,
                      ("cos", int): math.cos,
                      ("cos", float): math.cos,
                      ("cos", complex): cmath.cos,
                      ("cos", Matrix): cosMatrix,
                      ("tan", int): math.tan,
                      ("tan", float): math.tan,
                      ("tan", complex): cmath.tan,
                      ("tan", Matrix): tanMatrix,
                      ("sinh", int): math.sinh,
                      ("sinh", float): math.sinh,
                      ("sinh", complex): cmath.sinh,
                      ("sinh", Matrix): sinhMatrix,
                      ("cosh", int): math.cosh,
                      ("cosh", float): math.cosh,
                      ("cosh", complex): cmath.cosh,
                      ("cosh", Matrix): coshMatrix,
                      ("tanh", int): math.tanh,
                      ("tanh", float): math.tanh,
                      ("tanh", complex): cmath.tanh,
                      ("tanh", Matrix): tanhMatrix,
                      ("asin", int): math.asin,
                      ("asin", float): math.asin,
                      ("asin", complex): cmath.asin,
                      ("acos", int): math.acos,
                      ("acos", float): math.acos,
                      ("acos", complex): cmath.acos,
                      ("atan", int): math.atan,
                      ("atan", float): math.atan,
                      ("atan", complex): cmath.atan,
                      ("asinh", int): math.asinh,
                      ("asinh", float): math.asinh,
                      ("asinh", complex): cmath.asinh,
                      ("acosh", int): math.acosh,
                      ("acosh", float): math.acosh,
                      ("acosh", complex): cmath.acosh,
                      ("atanh", int): math.atanh,
                      ("atanh", float): math.atanh,
                      ("atanh", complex): cmath.atanh,
                      ("signum", int): lambda value: 1 if value > 0 else -1 if value < 0 else 0,
                      ("signum", float): lambda value: 1 if value > 0 else -1 if value < 0 else 0,
                      ("signum", complex): lambda value: 1 if value.real > 0 else (-1 if value.real < 0 else (1 if
                                                         value.imag > 0 else -1)),
                      ("signum", Quaternion): signumQuaternion,
                      ("signum", Matrix): signumMatrix}


def expMath(mathEntity: Union[int, float, complex, Quaternion, Matrix]) -> Union[int, float, complex, Quaternion, Matrix]:
    """
    Computes the exponential of the given mathematical entity if it has one.
    If it is does not have an exponential, nan is returned

    :param mathEntity: The mathematical entity whose exponential will be
        computed
    :return: The exponential of the given mathematical entity if it has
        one. If it does not have an exponential, nan is returned
    """

    key = ("exp", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def logMath(mathEntity: Union[int, float, complex, Quaternion, Matrix]) -> Union[int, float, complex, Quaternion, Matrix]:
    """
    Computes the logarithm of the given mathematical entity if it has one.
    If it does not have a logarithm, nan is returned

    :param mathEntity: The mathematical entity whose logarithm will be
        computed
    :return: The logarithm of the given mathematical entity if it has one.
        If it does not have a logarithm, nan is returned
    """

    key = ("log", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def log10Math(mathEntity: Union[int, float, complex, Quaternion, Matrix]) -> Union[int, float, complex, Quaternion, Matrix]:
    """
    Computes the logarithm of the given mathematical entity if it has one
    with a base of 10. If it does not have a logarithm, nan is returned

    :param mathEntity: The mathematical entity whose logarithm with a base
        of 10 will be computed
    :return: The logarithm of the given mathematical entity with a base of 10
        if it has one. If it does not have a logarithm, nan is returned
    """

    key = ("log10", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def sqrtMath(mathEntity: Union[int, float, complex, Quaternion, Matrix]) -> Union[int, float, complex, Quaternion, Matrix]:
    """
    Computes the square root of the given mathematical entity if it has one.
    If it does not have a square root, nan is returned

    :param mathEntity: The mathematical entity whose square root will be
        computed
    :return: The square root of the given mathematical entity if it has one.
        If it does not have a square root, nan is returned
    """

    key = ("sqrt", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        if type(mathEntity) == int or type(mathEntity) == float:
            if mathEntity < 0:
                func = cmath.sqrt

        return func(mathEntity)
    else:
        return math.nan


def sinMath(mathEntity: Union[int, float, complex, Matrix]) -> Union[int, float, complex, Matrix]:
    """
    Computes the sine of the given mathematical entity if it has one. If it does
    not have a sine, nan is returned

    :param mathEntity: The mathematical entity whose sine will be computed
    :return: The sine of the given mathematical entity if it has one. If it
        does not have a sine, nan is returned
    """

    key = ("sin", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def cosMath(mathEntity: Union[int, float, complex, Matrix]) -> Union[int, float, complex, Matrix]:
    """
    Computes the cosine of the given mathematical entity if it has one. If it does
    not have a cosine, nan is returned

    :param mathEntity: The mathematical entity whose cosine will be computed
    :return: The cosine of the given mathematical entity if it has one. If it
        does not have a cosine, nan is returned
    """

    key = ("cos", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def tanMath(mathEntity: Union[int, float, complex, Matrix]) -> Union[int, float, complex, Matrix]:
    """
    Computes the tangent of the given mathematical entity if it has one. If it does
    not have a tangent, nan is returned

    :param mathEntity: The mathematical entity whose tangent will be computed
    :return: The tangent of the given mathematical entity if it has one. If it
        does not have a tangent, nan is returned
    """

    key = ("tan", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def sinhMath(mathEntity: Union[int, float, complex, Matrix]) -> Union[int, float, complex, Matrix]:
    """
    Computes the hyperbolic sine of the given mathematical entity if it has one. If it does
    not have a hyperbolic sine, nan is returned

    :param mathEntity: The mathematical entity whose hyperbolic sine will be computed
    :return: The hyperbolic sine of the given mathematical entity if it has one. If it
        does not have a hyperbolic sine, nan is returned
    """

    key = ("sinh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def coshMath(mathEntity: Union[int, float, complex, Matrix]) -> Union[int, float, complex, Matrix]:
    """
    Computes the hyperbolic cosine of the given mathematical entity if it has one. If it does
    not have a hyperbolic cosine, nan is returned

    :param mathEntity: The mathematical entity whose hyperbolic cosine will be computed
    :return: The hyperbolic cosine of the given mathematical entity if it has one. If it
        does not have a hyperbolic cosine, nan is returned
    """

    key = ("cosh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def tanhMath(mathEntity: Union[int, float, complex, Matrix]) -> Union[int, float, complex, Matrix]:
    """
    Computes the hyperbolic tangent of the given mathematical entity if it has one. If it does
    not have a hyperbolic tangent, nan is returned

    :param mathEntity: The mathematical entity whose hyperbolic tangent will be computed
    :return: The hyperbolic tangent of the given mathematical entity if it has one. If it
        does not have a hyperbolic tangent, nan is returned
    """

    key = ("tanh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def asinMath(mathEntity: Union[int, float, complex]) -> Union[int, float, complex]:
    """
    Computes the arcsine of the given mathematical entity if it has one. If it does
    not have an arcsine, nan is returned

    :param mathEntity: The mathematical entity whose arcsine will be computed
    :return: The arcsine of the given mathematical entity if it has one. If it
        does not have a arcsine, nan is returned
    """

    key = ("asin", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def acosMath(mathEntity: Union[int, float, complex]) -> Union[int, float, complex]:
    """
    Computes the arccosine of the given mathematical entity if it has one. If it does
    not have an arccosine, nan is returned

    :param mathEntity: The mathematical entity whose arccosine will be computed
    :return: The arccosine of the given mathematical entity if it has one. If it
        does not have an arccosine, nan is returned
    """

    key = ("acos", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def atanMath(mathEntity: Union[int, float, complex]) -> Union[int, float, complex]:
    """
    Computes the arctangent of the given mathematical entity if it has one. If it does
    not have an arctangent, nan is returned

    :param mathEntity: The mathematical entity whose arctangent will be computed
    :return: The arctangent of the given mathematical entity if it has one. If it
        does not have an arctangent, nan is returned
    """

    key = ("atan", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def asinhMath(mathEntity: Union[int, float, complex]) -> Union[int, float, complex]:
    """
    Computes the hyperbolic arcsine of the given mathematical entity if it has one. If it
    does not have a hyperbolic arcsine, nan is returned

    :param mathEntity: The mathematical entity whose hyperbolic arcsine will be computed
    :return: The hyperbolic arcsine of the given mathematical entity if it has one. If it
        does not have a hyperbolic arcsine, nan is returned
    """

    key = ("asinh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def acoshMath(mathEntity: Union[int, float, complex]) -> Union[int, float, complex]:
    """
    Computes the hyperbolic arccosine of the given mathematical entity if it has one. If it
    does not have a hyperbolic arccosine, nan is returned

    :param mathEntity: The mathematical entity whose hyperbolic arccosine will be computed
    :return: The hyperbolic arccosine of the given mathematical entity if it has one. If it
        does not have a hyperbolic arccosine, nan is returned
    """

    key = ("acosh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def atanhMath(mathEntity: Union[int, float, complex]) -> Union[int, float, complex]:
    """
    Computes the hyperbolic arctangent of the given mathematical entity if it has one. If it
    does not have a hyperbolic arctangent, nan is returned

    :param mathEntity: The mathematical entity whose hyperbolic arctangent will be computed
    :return: The hyperbolic arctangent of the given mathematical entity if it has one. If it
        does not have a hyperbolic arctangent, nan is returned
    """

    key = ("atanh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def signumMath(mathEntity: MathEntity) -> Union[MathEntity, float]:
    """
    Computes the sign of the given mathematical entity

    :param mathEntity: The mathematical entity whose sign will be computed
    :return: The sign of the given mathematical entity
    """

    key = ("signum", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return math.nan


def chooseMath(total: int, amountToTake: int) -> int:
    return math.factorial(total) // (math.factorial(amountToTake) * math.factorial(total - amountToTake))


def chooseRepeatMath(total: int, amountToTake: int) -> int:
    return chooseMath(total + amountToTake - 1, amountToTake)


def permutationMath(total: int, amountToTake: int) -> int:
    return math.factorial(total) // math.factorial(total - amountToTake)
