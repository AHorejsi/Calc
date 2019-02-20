from __future__ import annotations
from typing import List, Iterator, Union
from copy import copy
from calc.MathEntity import MathEntity


class DataValueList(MathEntity):
    def __init__(self, dataValues: List[Union[int, float]]):
        self.__data = dataValues
        self.__sortedData = None # This value will be filled with a sorted list of the data values if a function that
                                 # requires the list be sorted is called

    def __len__(self):
        return len(self.__data)

    def mean(self) -> Union[int, float]:
        meanValue = 0

        for value in self:
            meanValue += value

        meanValue /= len(self)

        return meanValue

    def median(self) -> Union[int, float]:
        self.__sortedData = copy(self.__data)
        self.__sortedData.sort()
        mid = int(len(self) / 2)

        if len(self) % 2 == 0:
            return (self.__data[mid] + self.__data[mid + 1]) / 2
        else:
            return self.__data[mid]

    def mode(self) -> Union[int, float]:


    def __iter__(self) -> Iterator[Union[int, float]]:
        return iter(self.__data)
