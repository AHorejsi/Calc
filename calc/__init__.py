from calc.MathEntity import MathEntity
from calc.Negatable import Negatable
from calc.Exponentable import Exponentable
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix
from calc.BaseConversion import intToBinary, intToHexadecimal, intToOctal, binaryToInt, hexadecimalToInt, octalToInt
from calc.MathFunction import pow, exp, sqrt, cbrt, log, log10, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, \
                              asinh, acosh, atanh, sec, csc, cot, asec, acsc, acot, sech, csch, coth, asech, acsch, \
                              acoth, ceil, floor, PI, E

x = Quaternion(9, 5, -2, 4)
y = Complex(7, 4.2)
print(x ** y)
