from __future__ import annotations
from typing import Union
from math import pi


class Circle:
    """
    Instances of this class represent a circle. This class can
    be used to compute the geometric properties of a given circle
    """

    def __init__(self, radius: Union[int, float]):
        """
        Creates a circle with the given radius. The
        radius is the distance from the circle's
        center to its edge

        :param radius: The radius of this circle
        :raises ArithmeticError: Raised if the value for radius
            is not positive
        """

        if radius <= 0:
            raise ArithmeticError("Radius must be positive")

        self.__radius = radius

    @property
    def radius(self) -> Union[int, float]:
        """
        Returns the radius of this circle

        :return: The radius of this circle
        """

        return self.__radius

    @property
    def diameter(self) -> Union[int, float]:
        """
        Computes the diameter of this circle

        :return: The diameter of this circle
        """

        return 2 * self.__radius

    @property
    def perimeter(self) -> Union[int, float]:
        """
        Computes the perimeter of this circle

        :return: The perimeter of this circle
        """

        return pi * self.diameter

    @property
    def area(self) -> Union[int, float]:
        """
        Computes the area of this circle

        :return: The area of this circle
        """

        return pi * self.__radius * self.__radius

    def __eq__(self, other: Circle) -> bool:
        """
        Checks if the two given circles have the same radius

        :param other: The other circle being compared to this
            one
        :return: True if both circles have the same radius,
            False otherwise
        """

        return self.__radius == other.__radius

    def __ne__(self, other: Circle) -> bool:
        """
        Checks if the two given circles do not have the same radius

        :param other: The other circle being compared to this
            one
        :return: True if both circles do not have the same radius,
            False otherwise
        """

        return not (self == other)
