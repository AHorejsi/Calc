from __future__ import annotations
from typing import Union, List, Tuple, Iterator
from calc.MathFunction import sqrtMath


class ProbabilityDistribution:
	def __init__(self, data: List[Tuple[Union[int, float, complex, Quaternion], float]]):
		self.__data = data
		
	def mean(self) -> Union[int, float, complex, Quaternion]:
		meanValue = 0
		
		for (value, probability) in self:
			meanValue += value * probability
			
		return meanValue
		
	def variance(self) -> Union[int, float, complex, Quaternion]:
		varianceValue = 0
		
		for (value, probability) in self:
			varianceValue += value * value * probability
			
		varianceValue -= self.mean() ** 2
		
		return varianceValue
		
	def standardDeviation(self) -> Union[int, float, complex, Quaternion]:
		return sqrtMath(self.variance())
		
	def __iter__(self) -> Iterator[Union[int, float]]:
		return iter(self.__data)
		
	def __str__(self) -> str:
		return str(self.__data)
		
	def __repr__(self) -> str:
		return str(self)
