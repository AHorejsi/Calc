from __future__ import annotations
from typing import Union, List, Tuple, Iterator
from calc.MathFunction import sqrtMath
from calc.Quaternion import Quaternion


class ProbabilityDistribution:
	def __init__(self, data: List[Tuple[Union[int, float, complex, Quaternion], float]]):
		self.__data = data
		
	def __len__(self) -> int:
		return len(self.__data)
		
	def __getitem__(self, index: int) -> Tuple[Union[int, float, complex, Quaternion], float]:
		return self.__data[index]
		
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
		
	def __iter__(self) -> Iterator[Tuple[Union[int, float, complex, Quaternion], float]]:
		return iter(self.__data)
		
	def __eq__(self, distribution: ProbabilityDistribution) -> bool:
		if len(self) != len(distribution):
			return False
			
		for (leftEntry, rightEntry) in zip(self, distribution):
			if leftEntry != rightEntry:
				return False
				
		return True
		
	def __ne__(self, distribution: ProbabilityDistribution) -> bool:
		return not (self == distribution)
		
	def __str__(self) -> str:
		return str(self.__data)
		
	def __repr__(self) -> str:
		return str(self)
