from __future__ import annotations
from typing import Union
from math import pi, sin, tan


class RegularPolygon:
    def __init__(self, numberOfSides: int, lengthOfSides: float):
        self.numberOfSides = numberOfSides
        self.lengthOfSides = lengthOfSides

    @property
    def perimeter(self) -> Union[int, float]:
        return self.numberOfSides * self.lengthOfSides

    @property
    def area(self) -> Union[int, float]:
        return (self.lengthOfSides * self.lengthOfSides * self.numberOfSides) / (4 * tan(pi / self.numberOfSides))

    @property
    def apothem(self) -> Union[int, float]:
        return self.lengthOfSides / (2 * tan(pi / self.numberOfSides))

    @property
    def circumradius(self) -> Union[int, float]:
        return self.lengthOfSides / (2 * sin(pi / self.numberOfSides))

    @property
    def sumOfInteriorAngles(self) -> Union[int, float]:
        return (self.numberOfSides - 2) * pi

    @property
    def interiorAngles(self) -> Union[int, float]:
        return self.sumOfInteriorAngles / self.numberOfSides

    def __eq__(self, other: RegularPolygon) -> bool:
        return self.numberOfSides == other.numberOfSides and self.lengthOfSides == other.lengthOfSides

    def __ne__(self, other: RegularPolygon) -> bool:
        return not (self == other)
