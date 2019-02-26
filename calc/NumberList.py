from __future__ import annotations
from typing import List, Union, Iterator, NoReturn
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion


class NumberList(MathEntity):
    def __init__(self, data: List[Union[int, float, complex, Quaternion]]):
        self.__data = data

    def __len__(self) -> int:
        return len(self.__data)

    def __getitem__(self, index: int) -> Union[int, float]:
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        return self.__data[index]

    def __setitem__(self, index: int, value: Union[int, float, complex, Quaternion]) -> NoReturn:
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        self.__data[index] = value

    def mean(self) -> Union[int, float, complex, Quaternion]:
        return sum(self) / len(self)

    def median(self) -> Union[int, float]:
        sortedData = sorted(self.__data)
        mid = round(len(self) / 2)

        if len(self) % 2 == 0:
            return (sortedData[mid] + sortedData[mid + 1]) / 2
        else:
            return sortedData[mid]

    def __iter__(self) -> Iterator[Union[int, float]]:
        return iter(self.__data)

    def __str__(self) -> str:
        rep = "{"

        for index in range(len(self)):
            rep += self[index]

            if index == len(self) - 1:
                rep += "}"
            else:
                rep += ", "

        return rep
