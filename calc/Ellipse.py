from __future__ import annotations
from typing import Union
from math import pi, sqrt


class Ellipse:
    def __init__(self, verticalAxis: Union[int, float], horizontalAxis: Union[int, float]):
        """
        Creates an ellipse with the distances along the vertical and
        horizontal axes

        :param verticalAxis: The length along the vertical axis
        :param horizontalAxis: The length along the horizontal axis
        :raises ArithmeticError: Raised if either parameter is not
            positive
        """

        if verticalAxis <= 0 or horizontalAxis <= 0:
            raise ArithmeticError("The length along both axes must be positive")

        self.__verticalAxis = verticalAxis
        self.__horizontalAxis = horizontalAxis

    @property
    def verticalAxis(self) -> Union[int, float]:
        """
        Returns the length along the vertical axis

        :return: The length along the vertical axis
        """

        return self.__verticalAxis

    @property
    def horizontalAxis(self) -> Union[int, float]:
        """
        Returns the length along the horizontal axis

        :return: The length along the horizontal axis
        """

        return self.__horizontalAxis

    @property
    def majorAxis(self) -> Union[int, float]:
        """
        Computes the length of the major axis

        :return: The length of the major axis
        """

        return max(self.__verticalAxis, self.__horizontalAxis)

    @property
    def minorAxis(self) -> Union[int, float]:
        """
        Computes the length of the minor axis

        :return: The length of the minor axis
        """

        return min(self.__verticalAxis, self.__horizontalAxis)

    @property
    def semimajorAxis(self) -> Union[int, float]:
        """
        Computes the length of the semimajor axis

        :return: The length of the semimajor axis
        """

        return self.majorAxis / 2

    @property
    def semiminorAxis(self) -> Union[int, float]:
        """
        Computes the length of the semiminor axis

        :return: The length of the semiminor axis
        """

        return self.minorAxis / 2

    @property
    def perimeter(self) -> Union[int, float]:
        """
        Computes the perimeter of this ellipse

        :return: The perimeter of this ellipse
        """

        semimajor = self.semimajorAxis
        semiminor = self.semiminorAxis
        hValue = ((semimajor - semiminor) ** 2) / ((semimajor + semiminor) ** 2)

        return pi * (semimajor * semiminor) * (1 + ((3 * hValue) / (10 + sqrt(4 - 3 * hValue))))

    @property
    def area(self) -> Union[int, float]:
        """
        Computes the area of this ellipse

        :return: The area of this ellipse
        """

        return pi * self.__verticalAxis * self.__horizontalAxis

    @property
    def eccentricity(self) -> Union[int, float]:
        """
        Computes the eccentricity of this ellipse

        :return: The eccentricity on this ellipse
        """

        return sqrt((self.semimajorAxis ** 2) - (self.semiminorAxis ** 2)) / self.semimajorAxis

    def __eq__(self, other: Ellipse) -> bool:
        """
        Checks if both given ellipses have the same lengths along
        each of their respective axes

        :param other: The other ellipse being compared to this one
        :return: True if both ellipses have the same lengths along
            both of their respective axes, False otherwise
        """

        return self.__verticalAxis == other.__verticalAxis and self.__horizontalAxis == other.__horizontalAxis

    def __ne__(self, other: Ellipse) -> bool:
        """
        Checks if both given ellipses do not have the same lengths
        along either of their respective axes

        :param other: The other ellipse being compared to this one
        :return: True if both ellipses do not have the same lengths
            along both of their respective axes, False otherwise
        """

        return not (self == other)
