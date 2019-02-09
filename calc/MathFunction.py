from math import nan, exp, log, log10, sqrt, sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, asinh, acosh, atanh
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix
from calc.ComplexFunction import expComplex, logComplex, log10Complex, sqrtComplex, sinComplex, cosComplex, \
                                 tanComplex, sinhComplex, coshComplex, tanhComplex, asinComplex, acosComplex, \
                                 atanComplex, asinhComplex, acoshComplex, atanhComplex, signumComplex
from calc.QuaternionFunction import expQuaternion, sqrtQuaternion, logQuaternion, log10Quaternion, signumQuaternion
from calc.MatrixFunction import expMatrix, logMatrix, sqrtMatrix, sinMatrix, cosMatrix, tanMatrix, sinhMatrix, \
                                coshMatrix, tanhMatrix, signumMatrix
from typing import Union


functionDictionary = {("exp", int): exp,
                      ("exp", float): exp,
                      ("exp", Complex): expComplex,
                      ("exp", Quaternion): expQuaternion,
                      ("exp", Matrix): expMatrix,
                      ("log", int): log,
                      ("log", float): log,
                      ("log", Complex): logComplex,
                      ("log", Quaternion): logQuaternion,
                      ("log", Matrix): logMatrix,
                      ("log10", int): log10,
                      ("log10", float): log10,
                      ("log10", Complex): log10Complex,
                      ("log10", Quaternion): log10Quaternion,
                      ("sqrt", int): sqrt,
                      ("sqrt", float): sqrt,
                      ("sqrt", Complex): sqrtComplex,
                      ("sqrt", Quaternion): sqrtQuaternion,
                      ("sqrt", Matrix): sqrtMatrix,
                      ("sin", int): sin,
                      ("sin", float): sin,
                      ("sin", Complex): sinComplex,
                      ("sin", Matrix): sinMatrix,
                      ("cos", int): cos,
                      ("cos", float): cos,
                      ("cos", Complex): cosComplex,
                      ("cos", Matrix): cosMatrix,
                      ("tan", int): tan,
                      ("tan", float): tan,
                      ("tan", Complex): tanComplex,
                      ("tan", Matrix): tanMatrix,
                      ("sinh", int): sinh,
                      ("sinh", float): sinh,
                      ("sinh", Complex): sinhComplex,
                      ("sinh", Matrix): sinhMatrix,
                      ("cosh", int): cosh,
                      ("cosh", float): cosh,
                      ("cosh", Complex): coshComplex,
                      ("cosh", Matrix): coshMatrix,
                      ("tanh", int): tanh,
                      ("tanh", float): tanh,
                      ("tanh", Complex): tanhComplex,
                      ("tanh", Matrix): tanhMatrix,
                      ("asin", int): asin,
                      ("asin", float): asin,
                      ("asin", Complex): asinComplex,
                      ("acos", int): acos,
                      ("acos", float): acos,
                      ("acos", Complex): acosComplex,
                      ("atan", int): atan,
                      ("atan", float): atan,
                      ("atan", Complex): atanComplex,
                      ("asinh", int): asinh,
                      ("asinh", float): asinh,
                      ("asinh", Complex): asinhComplex,
                      ("acosh", int): acosh,
                      ("acosh", float): acosh,
                      ("acosh", Complex): acoshComplex,
                      ("atanh", int): atanh,
                      ("atanh", float): atanh,
                      ("atanh", Complex): atanhComplex,
                      ("signum", int): lambda value: 1 if value > 0 else -1 if value < 0 else 0,
                      ("signum", float): lambda value: 1 if value > 0 else -1 if value < 0 else 0,
                      ("signum", Complex): signumComplex,
                      ("signum", Quaternion): signumQuaternion,
                      ("signum", Matrix): signumMatrix}


def expMath(mathEntity: Union[int, float, Complex, Quaternion, Matrix]) -> Union[int, float, Complex, Quaternion, Matrix]:
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
        return nan


def logMath(mathEntity: Union[int, float, Complex, Quaternion, Matrix]) -> Union[int, float, Complex, Quaternion, Matrix]:
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
        return nan


def log10Math(mathEntity: Union[int, float, Complex, Quaternion, Matrix]) -> Union[int, float, Complex, Quaternion, Matrix]:
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
        return nan


def sqrtMath(mathEntity: Union[int, float, Complex, Quaternion, Matrix]) -> Union[int, float, Complex, Quaternion, Matrix]:
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
        return func(mathEntity)
    else:
        return nan


def sinMath(mathEntity: Union[int, float, Complex, Matrix]) -> Union[int, float, Complex, Matrix]:
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
        return nan


def cosMath(mathEntity: Union[int, float, Complex, Matrix]) -> Union[int, float, Complex, Matrix]:
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
        return nan


def tanMath(mathEntity: Union[int, float, Complex, Matrix]) -> Union[int, float, Complex, Matrix]:
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
        return nan


def sinhMath(mathEntity: Union[int, float, Complex, Matrix]) -> Union[int, float, Complex, Matrix]:
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
        return nan


def coshMath(mathEntity: Union[int, float, Complex, Matrix]) -> Union[int, float, Complex, Matrix]:
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
        return nan


def tanhMath(mathEntity: Union[int, float, Complex, Matrix]) -> Union[int, float, Complex, Matrix]:
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
        return nan


def asinMath(mathEntity: Union[int, float, Complex]) -> Union[int, float, Complex]:
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
        return nan


def acosMath(mathEntity: Union[int, float, Complex]) -> Union[int, float, Complex]:
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
        return nan


def atanMath(mathEntity: Union[int, float, Complex]) -> Union[int, float, Complex]:
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
        return nan


def asinhMath(mathEntity: Union[int, float, Complex]) -> Union[int, float, Complex]:
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
        return nan


def acoshMath(mathEntity: Union[int, float, Complex]) -> Union[int, float, Complex]:
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
        return nan


def atanhMath(mathEntity: Union[int, float, Complex]) -> Union[int, float, Complex]:
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
        return nan


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
        return nan
