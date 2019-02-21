from __future__ import annotations
from typing import List, Union, Optional, Iterator
from bisect import bisect_left
from math import ceil
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.MathFunction import sqrtMath


class DataValueList(MathEntity):
    def __init__(self, values: List[Union[int, float, complex, Quaternion]]):
        self.__data = values
        self.__sorted = sorted(values)

    def __len__(self) -> int:
        return len(self.__data)

    def equalDimensions(self, dataValueList: DataValueList) -> bool:
        return len(self) == len(dataValueList)

    def __getitem__(self, index: int) -> Union[int, float, complex, Quaternion]:
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        return self.__data[index]

    def mean(self) -> Optional[Union[int, float, complex, Quaternion]]:
        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            return sum(self.__data) / len(self)

    def median(self) -> Optional[Union[int, float, complex, Quaternion]]:
        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            mid = round(len(self) / 2)

            if len(self) & 1 == 0:
                return (self.__sorted[mid] + self.__sorted[mid + 1]) / 2
            else:
                return self.__sorted[mid]

    def mode(self) -> DataValueList:
        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            currentModes = []
            countOfMode = 1
            currentValue = None
            countOfCurrent = 1

            for value in self.__sorted:
                if value == currentValue:
                    countOfCurrent += 1
                else:
                    countOfCurrent = 1
                    currentValue = value

                if countOfCurrent == countOfMode:
                    currentModes.append(currentValue)
                elif countOfCurrent > countOfMode:
                    currentModes.clear()
                    currentModes.append(currentValue)
                    countOfMode = countOfCurrent

            return DataValueList(currentModes)

    def midrange(self) -> Union[int, float, complex, Quaternion]:
        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            return (self.__sorted[0] + self.__sorted[len(self) - 1]) / 2

    def range(self) -> Union[int, float, complex, Quaternion]:
        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            return self.__sorted[len(self) - 1] - self.__sorted[0]

    def variance(self) -> Union[int, float, complex, Quaternion]:
        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            meanValue = self.mean()
            variance = 0

            for value in self:
                variance += (value - meanValue) ** 2

            variance /= len(self)

            return variance

    def standardDeviation(self) -> Union[int, float, complex, Quaternion]:
        return sqrtMath(self.variance())

    def percentileOf(self, element) -> Union[int, float]:
        if len(self) == 0:
            return 1
        else:
            sortedPosition = bisect_left(self.__sorted, element)

            return round((sortedPosition / len(self)) * 100)

    def percentileIn(self, percentile):
        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            position = (percentile * len(self)) / 100

            if position.is_integer():
                position = int(position)

                return (self.__sorted[position] + self.__sorted[position + 1]) / 2
            else:
                position = ceil(position)

                return self.__sorted[position]

    def __iter__(self) -> Iterator[Union[int, float, complex, Quaternion]]:
        return iter(self.__data)

    def sorted(self) -> DataValueList:
        return DataValueList(self.__sorted)

    def __str__(self) -> str:
        rep = "["

        for index in range(len(self)):
            if index != len(self) - 1:
                rep += str(self[index]) + ", "
            else:
                rep += "]"

        return rep
