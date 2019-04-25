from __future__ import annotations
from typing import Tuple, List, Union, NoReturn, Iterator
from math import sqrt


class IrregularPolygon:
    """
    Instances of this class represent irregular polygons
    """

    def __init__(self, points: List[Tuple[float, float]]):
        """
        Creates an irregular polygon based on the given list
        of tuples. Each tuple should contain two real numbers
        and each tuple will serve as a single point for this
        irregular polygon. The order of the points does matter
        because the lines connecting the points are drawn in
        the order each point appears in the list

        :param points: A list of points describing this irregular
            polygon
        :raises ArithmeticError: Raised if less than 3 points are
            given
        """

        if len(points) < 3:
            raise ArithmeticError("There must be at least 3 points")

        self.__points = points

    @property
    def numberOfSides(self) -> int:
        """
        Returns the number of sides that this polygon has

        :return: The number of sides that this polygon has
        """

        return len(self)

    def __len__(self) -> int:
        """
        Returns the number of points that this polygon has

        :return: The number of points that this polygon has
        """

        return len(self.__points)

    def __getitem__(self, index: int) -> Tuple[float, float]:
        """
        Returns the point at the given index

        :param index: The index of the point to be
            returned
        :return: The point that is stored at the
            given index
        """

        return self.__points[index]

    def __setitem__(self, index: int, point: Tuple[float, float]) -> NoReturn:
        """
        Sets the point at the given index

        :param index: The index of the point
            to be changed
        :param point: The new point to be set
            at the given index
        :return: None
        """

        self.__points[index] = point

    @property
    def perimeter(self) -> Union[int, float]:
        """
        Computes the perimeter of this irregular polygon

        :return: The perimeter of this irregular polygon
        """

        perimeterValue = 0

        for index in range(len(self) - 1):
            perimeterValue += sqrt(((self[index][0] - self[index + 1][0]) ** 2) +
                                   ((self[index][1] - self[index + 1][1]) ** 2))

        perimeterValue += sqrt(((self[len(self) - 1][0] - self[0][0]) ** 2) +
                               ((self[len(self) - 1][1] - self[0][1]) ** 2))

        return perimeterValue

    @property
    def area(self) -> Union[int, float]:
        """
        Computes the area of this irregular polygon

        :return: The area of this irregular polygon
        """

        return abs(self.__leftRun() - self.__rightRun()) / 2

    def __leftRun(self) -> Union[int, float]:
        """
        Performs the left half of the shoelace
        algorithm

        :return: The left half of the shoelace
            algorithm
        """

        value = 0

        for index in range(len(self) - 1):
            value += self[index][0] * self[index + 1][1]

        value += self[len(self) - 1][0] * self[0][1]

        return value

    def __rightRun(self) -> Union[int, float]:
        """
        Performs the right half of the shoelace
        algorithm

        :return: The right half of the showlace
            algorithm
        """

        value = 0

        for index in range(len(self) - 1):
            value += self[index][1] * self[index + 1][0]

        value += self[len(self) - 1][1] * self[0][0]

        return value

    def __iter__(self) -> Iterator[Tuple[float, float]]:
        """
        Returns an iterator over the points of this irregular
        polygon

        :return: An iterator over the points of this irregular
            polygon
        """

        return iter(self.__points)

    def __eq__(self, other: IrregularPolygon) -> bool:
        """
        Checks if both irregular polygons have the same points
        in the same order

        :param other: The other irregular polygon being compared
            to this one
        :return: True if both irregular polygons have the same points
            in the same order, False otherwise
        """

        if self.numberOfSides != other.numberOfSides:
            return False

        for (point1, point2) in zip(self, other):
            if point1 != point2:
                return False

        return True

    def __ne__(self, other: IrregularPolygon) -> bool:
        """
        Checks if either irregular polygon has any points
        that are not equal to each other and in the same
        position

        :param other: The other irregular polygon being
            compared to this one
        :return: True if both irregular polygons do not
            have the same points in the same order, False
            otherwise
        """

        return not (self == other)
