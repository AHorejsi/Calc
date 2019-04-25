from __future__ import annotations
from typing import Union
from math import pi, sin, tan


class RegularPolygon:
    """
    Instances of this class represent regular polygons. A regular
    polygon is a polygon whose sides are all of the same length and
    all of its interior angles are equal
    """

    def __init__(self, numberOfSides: int, lengthOfSides: float):
        """
        Creates a regular polygon with the given number of sides
        with each side being the given length

        :param numberOfSides: The number of sides this polygon will have
        :param lengthOfSides: The length of the sides of this polygon
        """

        self.numberOfSides = numberOfSides
        self.lengthOfSides = lengthOfSides

    @property
    def perimeter(self) -> Union[int, float]:
        """
        Computes the perimeter of this polygon

        :return: The perimeter of this polygon
        """

        return self.numberOfSides * self.lengthOfSides

    @property
    def area(self) -> Union[int, float]:
        """
        Computes the area of this polygon

        :return: The area of this polygon
        """

        return (self.lengthOfSides * self.lengthOfSides * self.numberOfSides) / (4 * tan(pi / self.numberOfSides))

    @property
    def apothem(self) -> Union[int, float]:
        """
        Computes the length of the apothem of this regular polygon

        :return: The length of the apothem of this regular polygon
        """

        return self.lengthOfSides / (2 * tan(pi / self.numberOfSides))

    @property
    def circumradius(self) -> Union[int, float]:
        """
        Computes the length of the circumradius of this regular polygon

        :return: The length of the circumradius of this regular polygon
        """

        return self.lengthOfSides / (2 * sin(pi / self.numberOfSides))

    @property
    def sumOfInteriorAngles(self) -> Union[int, float]:
        """
        Computes the sum of the interior angles of this regular polygon

        :return: The sum of the interior angles of this regular polygon
        """

        return (self.numberOfSides - 2) * pi

    @property
    def interiorAngles(self) -> Union[int, float]:
        """
        Computes the interior angles of this regular polygon

        :return: The interior angles of this regular polygon
        """

        return self.sumOfInteriorAngles / self.numberOfSides

    def __eq__(self, other: RegularPolygon) -> bool:
        """
        Checks if the two given regular polygons have the same number
        of sides and the sides are of the same length

        :param other: The other regular polygon being compared to this
            one
        :return: True if both regular polygon are equal, False otherwise
        """

        return self.numberOfSides == other.numberOfSides and self.lengthOfSides == other.lengthOfSides

    def __ne__(self, other: RegularPolygon) -> bool:
        """
        Checks if the two given regular polygons do not have the same
        number of sides and/or do not have the same side lengths

        :param other: The other regular polygon being compared to this
            one
        :return: True if both regular polygon are not equal, False otherwise
        """

        return not (self == other)
