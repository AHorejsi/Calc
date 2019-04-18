from __future__ import annotations
from typing import Union, Tuple


class QuadraticEquation:
	def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
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
