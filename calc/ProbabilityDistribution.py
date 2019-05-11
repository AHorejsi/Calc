from __future__ import annotations
from typing import Union, List, Tuple, Iterator, NoReturn
from sys import float_info
from calc.MathFunction import sqrtMath
from calc.Quaternion import Quaternion


class ProbabilityDistribution:
    def __init__(self, data: List[Tuple[Union[int, float, complex, Quaternion], float]]):
        self.__data = data
        self.__sortedData = None

    def __sort(self) -> NoReturn:
        if self.__sortedData is None:
            self.__sortedData = sorted(self.__data, key=lambda entry: entry[0])

    def __len__(self) -> int:
        return len(self.__data)

    def getItem(self, index: int) -> Tuple[Union[int, float, complex, Quaternion], float]:
        if index < 0 or index >= len(self):
            raise IndexError("index out of bounds")

        return self.__data[index]

    def getSortedItem(self, index: int) -> Tuple[Union[int, float], float]:
        if index < 0 or index >= len(self):
            raise IndexError("index out of bounds")

        self.__sort()
        return self.__sortedData[index]

    def min(self) -> Tuple[Union[int, float], float]:
        minValue = float_info.max

        for (value, _) in self:
            if value < minValue:
                minValue = value

        return minValue

    def max(self) -> Tuple[Union[int, float], float]:
        maxValue = float_info.min

        for (value, _) in self:
            if value > maxValue:
                maxValue = value

        return maxValue

    def mean(self) -> Union[int, float, complex, Quaternion]:
        meanValue = 0

        for (value, probability) in self:
            meanValue += value * probability

        return meanValue

    def median(self) -> Union[int, float]:
        self.__sort()
        mid = len(self) // 2

        if len(self) % 2 == 0:
            return (self.__sortedData[mid][0] + self.__sortedData[mid + 1][0]) / 2
        else:
            return self.__sortedData[mid + 1][0]

    def mode(self) -> List[int, float, complex, Quaternion]:
        modes = []

        try:
            self.__sort()

            countOfMode = 1
            index = 0

            while index < len(self):
                current = self.__sortedData[index]
                countOfCurrent = 0

                while current[0] == self.__sortedData[index][0]:
                    countOfCurrent += 1
                    index += 1

                    if index >= len(self):
                        break

                if countOfCurrent == countOfMode and countOfMode != 1:
                    modes.append(current[0])
                elif countOfCurrent > countOfMode:
                    countOfMode = countOfCurrent

                    modes.clear()
                    modes.append(current[0])
        except TypeError:
            counts = {}

            for (value, probability) in self:
                if value in counts:
                    counts[value] += 1
                else:
                    counts[value] = 1

            countOfMode = None

            for (value, count) in counts.items():
                if count > countOfMode:
                    modes.clear()
                    modes.append(value)

                    countOfMode = count
                elif count == countOfMode and count != -1:
                    modes.append(value)

        return modes

    def midrange(self) -> Union[int, float]:
        self.__sort()

        return (self.__sortedData[len(self) - 1][0] + self.__sortedData[0][0]) / 2

    def range(self) -> Union[int, float]:
        self.__sort()

        return self.__sortedData[len(self) - 1][0] - self.__sortedData[0][0]

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

    def __hash__(self) -> int:
        MODIFIER = 31
        hashCode = 0

        for entry in self:
            hashCode += MODIFIER * hash(entry)

        return hashCode

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
