from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix
from calc.ComplexFunction import expComplex, logComplex, log10Complex, sqrtComplex, sinComplex, cosComplex, \
                                 tanComplex, sinhComplex, coshComplex, tanhComplex, asinComplex, acosComplex, \
                                 atanComplex, asinhComplex, acoshComplex, atanhComplex, ceilComplex, floorComplex, \
                                 signumComplex
from calc.QuaternionFunction import expQuaternion, sqrtQuaternion, logQuaternion, log10Quaternion, ceilQuaternion, \
                                    floorQuaternion
from calc.MatrixFunction import expMatrix, logMatrix, sqrtMatrix, sinMatrix, cosMatrix, tanMatrix, sinhMatrix, \
                                coshMatrix, tanhMatrix, signumMatrix, floorMatrix, ceilMatrix
from calc.MathFunction import expMath, logMath, log10Math, sqrtMath, sinMath, cosMath, tanMath, sinhMath, coshMath, \
                              tanhMath, asinMath, acosMath, atanMath, asinhMath, acoshMath, atanhMath, floorMath, \
                              ceilMath
from calc.MathConstant import PI, EULER, POSITIVE_INFINITY, NEGATIVE_INFINITY, NOT_A_NUMBER, IMAG_0, IMAG_1, IMAG_2

x0 = 6
x1 = 10.527
x2 = Complex(6.152, -9.057)
x3 = Quaternion(-0.953, 5.109, -44.313, 9.011)
x4 = Vector([-9.412, 100.091, -89.341])
x5 = Matrix([[5.127, 6.724, 7.552],
             [0.008, -6.423, -90.196],
             [-88.444, 9.312, 2.809]])
x6 = Matrix([[Complex(9.423, 0.312), Complex(-0.413, 5.441), Complex(90.135, -1.111)],
             [Complex(81.745, -15.609), Complex(91.135, -0.133), Complex(10.011, -19.198)],
             [Complex(5.246, 6.515), Complex(-7.777, 8.888), Complex(-19.023, -11.673)]])
x7 = Matrix([[Quaternion(7.814, -0.944, 6.126, 5.142), Quaternion(8.159, 10.523, -9.111, 70.001), Quaternion(99.412, 1.132, -8.412, 7.119)],
             [Quaternion(17.643, -9.412, 66.111, -10.199), Quaternion(-1.147, 61.109, 55.151, -78.143), Quaternion(0.999, -1.443, 72.086, 7.098)],
             [Quaternion(-3.319, 0.145, 9.005, -53.001), Quaternion(700.832, -15.415, 88.888, 111.876), Quaternion(9.109, 66.909, -54.489, 10.998)]])

values = [x0, x1, x2, x3, x4, x5, x6, x7]

for val1 in values:
    for val2 in values:
        try:
            result = val1 + val2

            if result is NOT_A_NUMBER:
                print(str(type(val1)) + " + " + str(type(val2)) + " is not working")
            else:
                print(str(type(val1)) + " + " + str(type(val2)) + " is working")
        except Exception:
            print(str(type(val1)) + " + " + str(type(val2)) + " is not possible")

        try:
            result = val1 - val2

            if result is NOT_A_NUMBER:
                print(str(type(val1)) + " - " + str(type(val2)) + " is not working")
            else:
                print(str(type(val1)) + " - " + str(type(val2)) + " is working")
        except Exception:
            print(str(type(val1)) + " - " + str(type(val2)) + " is not possible")

        try:
            result = val1 * val2

            if result is NOT_A_NUMBER:
                print(str(type(val1)) + " * " + str(type(val2)) + " is not working")
            else:
                print(str(type(val1)) + " * " + str(type(val2)) + " is working")
        except Exception:
            print(str(type(val1)) + " * " + str(type(val2)) + " is not possible")

        try:
            result = val1 / val2

            if result is NOT_A_NUMBER:
                print(str(type(val1)) + " / " + str(type(val2)) + " is not working")
            else:
                print(str(type(val1)) + " / " + str(type(val2)) + " is working")
        except Exception:
            print(str(type(val1)) + " / " + str(type(val2)) + " is not possible")

        try:
            result = val1 // val2

            if result is NOT_A_NUMBER:
                print(str(type(val1)) + " // " + str(type(val2)) + " is not working")
            else:
                print(str(type(val1)) + " // " + str(type(val2)) + " is working")
        except Exception:
            print(str(type(val1)) + " // " + str(type(val2)) + " is not possible")

        try:
            result = val1 ** val2

            if result is NOT_A_NUMBER:
                print(str(type(val1)) + " ** " + str(type(val2)) + " is not working")
            else:
                print(str(type(val1)) + " ** " + str(type(val2)) + " is working")
        except Exception:
            print(str(type(val1)) + " ** " + str(type(val2)) + " is not possible")

        print("\n\n\n")
