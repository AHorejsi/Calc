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

        if numberOfSides < 2:
            raise ArithmeticError("The number of sides must be greater than 2")
        if lengthOfSides <= 0:
            raise ArithmeticError("The length of each side must be positive")

        self.__numberOfSides = numberOfSides
        self.__lengthOfSides = lengthOfSides

    @property
    def numberOfSides(self) -> int:
        """
        Returns the number of sides that this regular polygon has

        :return: The number of sides that this regular polygon has
        """

        return self.__numberOfSides

    @property
    def lengthOfSides(self) -> float:
        """
        Return the length of this regular polygon's sides

        :return: The length of this regular polygon's sides
        """

        return self.__lengthOfSides

    @property
    def perimeter(self) -> Union[int, float]:
        """
        Computes the perimeter of this polygon

        :return: The perimeter of this polygon
        """

        return self.__numberOfSides * self.__lengthOfSides

    @property
    def area(self) -> Union[int, float]:
        """
        Computes the area of this polygon

        :return: The area of this polygon
        """

        return (self.__lengthOfSides * self.__lengthOfSides * self.__numberOfSides) / \
               (4 * tan(pi / self.__numberOfSides))

    @property
    def apothem(self) -> Union[int, float]:
        """
        Computes the length of the apothem of this regular polygon

        :return: The length of the apothem of this regular polygon
        """

        return self.__lengthOfSides / (2 * tan(pi / self.__numberOfSides))

    @property
    def circumradius(self) -> Union[int, float]:
        """
        Computes the length of the circumradius of this regular polygon

        :return: The length of the circumradius of this regular polygon
        """

        return self.__lengthOfSides / (2 * sin(pi / self.__numberOfSides))

    @property
    def sumOfInteriorAngles(self) -> Union[int, float]:
        """
        Computes the sum of the interior angles of this regular polygon

        :return: The sum of the interior angles of this regular polygon
        """

        return (self.__numberOfSides - 2) * pi

    @property
    def interiorAngles(self) -> Union[int, float]:
        """
        Computes the interior angles of this regular polygon

        :return: The interior angles of this regular polygon
        """

        return self.sumOfInteriorAngles / self.__numberOfSides

    def __eq__(self, other: RegularPolygon) -> bool:
        """
        Checks if the two given regular polygons have the same number
        of sides and the sides are of the same length

        :param other: The other regular polygon being compared to this
            one
        :return: True if both regular polygon are equal, False otherwise
        """

        return self.__numberOfSides == other.__numberOfSides and self.__lengthOfSides == other.__lengthOfSides

    def __ne__(self, other: RegularPolygon) -> bool:
        """
        Checks if the two given regular polygons do not have the same
        number of sides and/or do not have the same side lengths

        :param other: The other regular polygon being compared to this
            one
        :return: True if both regular polygon are not equal, False otherwise
        """

        return not (self == other)
