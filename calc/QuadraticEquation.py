from __future__ import annotations
from typing import Union, Tuple, Iterator
from calc.MathFunction import sqrtMath


class QuadraticEquation:
	"""
	Instances of this class represent quadratic equations.
	Quadratic equations are of the form (a * x ** 2) + (b * x) + c = 0, where
	a, b and c are real numbers
	"""

	def __init__(self, leadingCoefficient: Union[int, float], secondCoefficient: Union[int, float], constant: Union[int, float]):
		"""
		Constructs a quadratic equation with the given coefficients
		
		:param leadingCoefficient: The value of the leading coefficent. 
			This value cannot be set to zero
		:param secondCoefficient: The value of the second coefficient
		:param constant: The value of the constant variable
		"""
	
		if leadingCoefficient == 0:
			raise ArithmeticError("Leading coefficient cannot be zero")
	
		self.__leadingCoefficient = leadingCoefficient
		self.__secondCoefficient = secondCoefficient
		self.__constant = constant
		
	@property
	def leadingCoefficient(self) -> Union[int, float]:
		"""
		Returns the value of the leading coefficient
		
		:return: The leading coefficent of this
			quadratic equation
		"""
	
		return self.__leadingCoefficient
		
	@property
	def secondCoefficient(self) -> Union[int, float]:
		"""
		Returns the value of the second coefficent
		
		:return: The second coefficent of this
			quadratic equation
		"""
	
		return self.__secondCoefficient
		
	@property
	def constant(self) -> Union[int, float]:
		"""
		Returns the value of the constant variable
			
		:return: The constant variable of this
			quadratic equation
		"""
	
		return self.__constant
		
	@property
	def vertex(self) -> Tuple[Union[int, float]]:
		"""
		Computes the vertex of this quadratic equation
		
		:return: The vertex of this quadratic equation
		"""
	
		xValue = -self.__secondCoefficient / (2 * self.__leadingCoefficient)
		yValue = (self.__leadingCoefficient * xValue ** 2) + (self.__secondCoefficient * xValue) + self.__constant
		
		return (xValue, yValue)
		
	@property
	def discriminant(self) -> Union[int, float]:
		"""
		Computes the discriminant of this quadratic equation
		
		:return: The discriminant of this quadratic equation
		"""
	
		return (self.__secondCoefficient ** 2) - (4 * self.__leadingCoefficient * self.__constant)
		
	@property
	def xValue(self) -> Union[Union[int, float], Tuple[Union[int, float, complex]]]:
		"""
		Computes the value(s) of this quadratic equation. If the
		discriminant of this quadratic equation is positive, two
		real numbers are returned. If negative, two complex numbers
		are returned. If zero, one real number is returned
		
		:return: The value(s) of this quadratic equation
		"""
	
		discriminant = self.discriminant
		
		if discriminant == 0:
			return (-self.__secondCoefficient + sqrtMath(discriminant)) / (2 * self.__leadingCoefficient)
		else:
			value1 = (-self.__secondCoefficient + sqrtMath(discriminant)) / (2 * self.__leadingCoefficient)
			value2 = (-self.__secondCoefficient - sqrtMath(discriminant)) / (2 * self.__leadingCoefficient)
			
			return (value1, value2)
			
	def __iter__(self) -> Iterator[Union[int, float]]:
		"""
		Returns an iterator over the coefficients of this
		quadratic equation
		
		:return: An iterator over the coefficients of this
			quadratic equation
		"""
	
		return iter([self.__leadingCoefficient, self.__secondCoefficient, self.__constant])
		
	def __eq__(self, quadEqn: QuadraticEquation) -> bool:
		"""
		Checks if this quadratic equation has the same coefficients
		as the given quadratic equation
		
		:return: True if both quadratic equations have the same
			coefficients, False otherwise
		"""
	
		return self.__leadingCoefficient == quadEqn.__leadingCoefficient and \
		self.__secondCoefficient == quadEqn.__secondCoefficient and \
		self.__constant == quadEqn.__constant
		
	def __ne__(self, quadEqn: QuadraticEquation) -> bool:
		"""
		Checks if this quadratic equation does not share the same
		coefficients as the given quadratic equation
		
		:return: True if the given quadratic equations do not share
			the same coefficients, False otherwise
		"""
	
		return not (self == quadEqn)
		
	def __str__(self) -> str:
		"""
		Returns a string representation of this quadratic equation
		
		:return: A string representation of this quadratic equation
		"""
	
		strRep = QuadraticEquation.__coefficient(self.__leadingCoefficient, "x^2") + \
				 QuadraticEquation.__coefficient(self.__secondCoefficient, "x") + \
				 QuadraticEquation.__coefficient(self.__constant, "")
				 
		return strRep
	
	@staticmethod
	def __coefficient(value: Union[int, float], var: str) -> str:
		"""
		Computes the string representation for the given coefficient
		
		:return: The string representation for the given coefficient
		"""
	
		if value == 0:
			return "+0" + var
		elif value < 0:
			return "-" + str(abs(value)) + var
		else:
			return "+" + str(value) + var
	
	def __repr__(self) -> str:
		"""
		Returns a string representation of this quadratic equation
		for the Python shell
		
		:return: A string representation of this quadratic equation
			for the Python shell
		"""
	
		return str(self)
