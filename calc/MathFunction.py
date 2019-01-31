from math import nan, exp, log, log10, sqrt, sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, \
                 asinh, acosh, atanh, floor, ceil
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Matrix import Matrix
from calc.ComplexFunction import expComplex, logComplex, log10Complex, sqrtComplex, sinComplex, cosComplex, \
    tanComplex, sinhComplex, coshComplex, tanhComplex, asinComplex, acosComplex, \
    atanComplex, asinhComplex, acoshComplex, atanhComplex, signumComplex
from calc.QuaternionFunction import expQuaternion, sqrtQuaternion, logQuaternion, log10Quaternion
from calc.MatrixFunction import expMatrix, logMatrix, sqrtMatrix, sinMatrix, cosMatrix, tanMatrix, sinhMatrix, \
    coshMatrix, tanhMatrix, signumMatrix


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
                      ("signum", Matrix): signumMatrix}


def expMath(mathEntity):
    key = ("exp", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def logMath(mathEntity):
    key = ("log", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def log10Math(mathEntity):
    key = ("log10", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def sqrtMath(mathEntity):
    key = ("sqrt", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def sinMath(mathEntity):
    key = ("sin", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def cosMath(mathEntity):
    key = ("cos", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def tanMath(mathEntity):
    key = ("tan", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def sinhMath(mathEntity):
    key = ("sinh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def coshMath(mathEntity):
    key = ("cosh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def tanhMath(mathEntity):
    key = ("tanh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def asinMath(mathEntity):
    key = ("asin", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def acosMath(mathEntity):
    key = ("acos", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def atanMath(mathEntity):
    key = ("atan", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def asinhMath(mathEntity):
    key = ("asinh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def acoshMath(mathEntity):
    key = ("acosh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def atanhMath(mathEntity):
    key = ("atanh", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def signumMath(mathEntity):
    key = ("signum", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return nan


def floorMath(mathEntity):
    return floor(mathEntity)


def ceilMath(mathEntity):
    return ceil(mathEntity)
