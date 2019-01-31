from math import e, pi, inf, nan, exp, log, log10, sqrt, sin, floor, ceil
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix
from calc.ComplexFunction import expComplex, logComplex, log10Complex, sqrtComplex, sinComplex, cosComplex, \
    tanComplex, sinhComplex, coshComplex, tanhComplex, asinComplex, acosComplex, \
    atanComplex, asinhComplex, acoshComplex, atanhComplex, signumComplex
from calc.QuaternionFunction import expQuaternion, sqrtQuaternion, logQuaternion, log10Quaternion
from calc.MatrixFunction import expMatrix, logMatrix, sqrtMatrix, sinMatrix, cosMatrix, tanMatrix, sinhMatrix, \
    coshMatrix, tanhMatrix


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
                      ("floor", int): floor,
                      ("floor", float): floor,
                      ("floor", Complex): floor,
                      ("floor", Quaternion): floor,
                      ("floor", Vector): floor,
                      ("floor", Matrix): floor,
                      ("ceil", int): ceil,
                      ("ceil", float): ceil,
                      ("ceil", Complex): ceil,
                      ("ceil", Quaternion): ceil,
                      ("ceil", Vector): ceil,
                      ("ceil", Matrix): ceil,
                      ("sin", int): sin,
                      ("sin", float): sin,
                      ("sin", Complex): sinComplex,
                      ("sin", Matrix): sinMatrix,}
E = e
PI = pi
IMAG_0 = Complex(0, 1)
IMAG_1 = Quaternion(0, 0, 1, 0)
IMAG_2 = Quaternion(0, 0, 0, 1)
POSITIVE_INFINITY = inf
NEGATIVE_INFINITY = -inf
NOT_A_NUMBER = nan


def expMath(mathEntity):
    key = ("exp", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return NOT_A_NUMBER


def logMath(mathEntity):
    key = ("log", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return NOT_A_NUMBER


def log10Math(mathEntity):
    key = ("log10", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return NOT_A_NUMBER


def sqrtMath(mathEntity):
    key = ("sqrt", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return NOT_A_NUMBER


def sinMath(mathEntity):
    key = ("sin", type(mathEntity))
    func = functionDictionary.get(key)

    if func is not None:
        return func(mathEntity)
    else:
        return NOT_A_NUMBER
