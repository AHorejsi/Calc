from __future__ import annotations
from typing import Union, Tuple, Iterator
from calc.MathFunction import sqrtMath


class QuadraticEquation:
	def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
		if a == 0:
			raise ArithmeticError("Leading coefficient cannot be zero")
	
		self.__a = a
		self.__b = b
		self.__c = c
		
	@property
	def a(self) -> Union[int, float]:
		return self.__a
		
	@property
	def b(self) -> Union[int, float]:
		return self.__b
		
	@property
	def c(self) -> Union[int, float]:
		return self.__c
		
	@property
	def vertex(self) -> Tuple[Union[int, float]]:
		xValue = -self.__b / (2 * self.__a)
		yValue = (self.__a * xValue ** 2) + (self.__b * xValue) + self.__c
		
		return (xValue, yValue)
		
	@property
	def discriminant(self) -> Union[int, float]:
		return (self.__b ** 2) - (4 * self.__a * self.__c)
		
	@property
	def xValue(self) -> Union[Union[int, float], Tuple[Union[int, float, complex]]]:
		discriminant = self.discriminant
		
		if discriminant == 0:
			return (-self.__b + sqrtMath(discriminant)) / (2 * self.__a)
		else:
			value1 = (-self.__b + sqrtMath(discriminant)) / (2 * self.__a)
			value2 = (-self.__b - sqrtMath(discriminant)) / (2 * self.__a)
			
			return (value1, value2)
			
	def __iter__(self) -> Iterator[Union[int, float]]:
		return iter([self.__a, self.__b, self.__c])
		
	def __eq__(self, quadEqn: QuadraticEquation) -> bool:
		return self.__a == quadEqn.__a and self.__b == quadEqn.__b and self.__c == quadEqn.__c
		
	def __ne__(self, quadEqn: QuadraticEquation) -> bool:
		return not (self == quadEqn)
		
	def __str__(self) -> str:
		strRep = QuadraticEquation.__coefficient(self.__a, "x^2") + \
				 QuadraticEquation.__coefficient(self.__b, "x") + \
				 QuadraticEquation.__coefficient(self.__c, "")
				 
		return strRep
	
	@staticmethod
	def __coefficient(value: Union[int, float], var: str) -> str:
		if value == 0:
			return "+0" + var
		elif value < 0:
			return "-" + str(abs(value)) + var
		else:
			return "+" + str(value) + var
	
	def __repr__(self) -> str:
		return str(self)
