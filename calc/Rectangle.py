from __future__ import annotations
from typing import Union


class Rectangle:
    def __init__(self, length: Union[int, float], width: Union[int, float]):
        self.__length = length
        self.__width = width

    @property
    def length(self) -> Union[int, float]:
        """
        Returns the length of this rectangle

        :return: The length of this rectangle
        """

        return self.__length

    @property
    def width(self) -> Union[int, float]:
        """
        Returns the width of this rectangle

        :return: The width of this rectangle
        """

        return self.__width

    @property
    def perimeter(self) -> Union[int, float]:
        """
        Computes the perimeter of this rectangle

        :return: The perimeter of this rectangle
        """

        return self.__length + self.__length + self.__width + self.__width

    @property
    def area(self) -> Union[int, float]:
        """
        Computes the area of this rectangle

        :return: The area of this rectangle
        """

        return self.__length * self.__width

    def __eq__(self, other: Rectangle) -> bool:
        """
        Checks if this rectangle has the same length
        and width as another rectangle

        :param other: Another rectangle
        :return: True if both rectangles have the same
            length ans width, False otherwise
        """

        return self.__length == other.__length and self.__width == other.__width

    def __ne__(self, other: Rectangle) -> bool:
        """
        Checks if this rectangle has different length
        or width than another rectangle

        :param other: Another rectangle
        :return: True if the given rectangles have
            different lengths or widths, False otherwise
        """

        return not (self == other)
