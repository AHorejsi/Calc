from __future__ import annotations
from typing import Union
from math import pi


class Circle:
    def __init__(self, radius: Union[int, float]):
        self.__radius = radius

    @property
    def radius(self) -> Union[int, float]:
        return self.__radius

    @property
    def diameter(self) -> Union[int, float]:
        return 2 * self.__radius

    @property
    def perimeter(self) -> Union[int, float]:
        return pi * self.diameter

    @property
    def area(self) -> Union[int, float]:
        return pi * self.__radius * self.__radius
