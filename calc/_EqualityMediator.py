from typing import Union
from math import nan
from calc.MathEntity import MathEntity
from calc.Complex import Complex
from calc.Quaternion import Quaternion
from calc.Vector import Vector
from calc.Matrix import Matrix


eqDict = {(int, Complex): lambda leftInt, rightComplex: leftInt == rightComplex.real and
                                                              rightComplex.imag0 == 0,
          (int, Quaternion): lambda leftInt, rightQuaternion: leftInt == rightQuaternion.real and
                                                                    rightQuaternion.imag0 == 0 and
                                                                    rightQuaternion.imag1 == 0 and
                                                                    rightQuaternion.imag2 == 0,
          (float, Complex): lambda leftFloat, rightComplex: leftFloat == rightComplex.real and
                                                                  rightComplex.imag0 == 0,
          (float, Quaternion): lambda leftFloat, rightQuaternion: leftFloat == rightQuaternion.real and
                                                                        rightQuaternion.imag0 == 0 and
                                                                        rightQuaternion.imag1 == 0 and
                                                                        rightQuaternion.imag2 == 0,
          (Complex, int): lambda leftComplex, rightInt: leftComplex.real == rightInt and
                                                              leftComplex.imag0 == 0,
          (Complex, float): lambda leftComplex, rightFloat: leftComplex.real == rightFloat and
                                                                  leftComplex.imag0 == 0,
          (Complex, Complex): lambda leftComplex, rightComplex: leftComplex.real == rightComplex.real and
                                                                      leftComplex.imag0 == rightComplex.imag0,
          (Complex, Quaternion): lambda leftComplex, rightQuaternion: leftComplex.real == rightQuaternion.real and
                                                                            leftComplex.imag0 == rightQuaternion.imag0 and
                                                                            leftComplex.imag1 == 0 and
                                                                            leftComplex.imag2 == 0,
          (Quaternion, int): lambda leftQuaternion, rightInt: leftQuaternion.real == rightInt and
                                                                    leftQuaternion.imag0 == 0 and
                                                                    leftQuaternion.imag1 == 0 and
                                                                    leftQuaternion.imag2 == 0,
          (Quaternion, float): lambda leftQuaternion, rightFloat: leftQuaternion.real == rightFloat and
                                                                        leftQuaternion.imag0 == 0 and
                                                                        leftQuaternion.imag1 == 0 and
                                                                        leftQuaternion.imag2 == 0,
          (Quaternion, Complex): lambda leftQuaternion, rightComplex: leftQuaternion.real == rightComplex.real and
                                                                            leftQuaternion.imag0 == rightComplex.imag0 and
                                                                            leftQuaternion.imag1 == 0 and
                                                                            leftQuaternion.imag2 == 0,
          (Quaternion, Quaternion): lambda leftQuaternion, rightQuaternion: leftQuaternion.real == rightQuaternion.real and
                                                                                  leftQuaternion.imag0 == rightQuaternion.imag0 and
                                                                                  leftQuaternion.imag1 == rightQuaternion.imag1 and
                                                                                  leftQuaternion.imag2 == rightQuaternion.imag2}


def doEquality(mathEntity1: Union[int, float, MathEntity],
               mathEntity2: Union[int, float, MathEntity]) -> bool:
    key = (type(mathEntity1), type(mathEntity2))
    operation = eqDict.get(key)

    if operation is not None:
        return operation(mathEntity1, mathEntity2)
    else:
        return False
