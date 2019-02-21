from __future__ import annotations
from typing import List, Union, Optional, Iterator
from bisect import bisect_left
from math import ceil
from copy import copy
from calc.MathEntity import MathEntity
from calc.Quaternion import Quaternion
from calc.MathFunction import sqrtMath


class DataValueList(MathEntity):
    """
    Instances of this class represent lists of data values
    that can be used for statistical calculations
    """

    def __init__(self, values: List[Union[int, float, complex, Quaternion]]):
        """
        Makes the given list of data values a representation
        of statistical information

        :param values: The list of values to represent
            statistical information
        """

        if DataValueList.__isSorted(values):
            self.__data = values
            self.__sorted = values
        else:
            self.__data = values
            self.__sorted = sorted(values)

    @staticmethod
    def __isSorted(values: List[Union[int, float, complex, Quaternion]]) -> bool:
        """
        Checks if the given list is sorted

        :param values: The list to be checked
            for if it is sorted
        :return: True if the given list is sorted,
            False otherwise
        """

        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                return False

        return True

    def __len__(self) -> int:
        """
        Returns the number of values contained in
        this data value list

        :return: The number of values contained in
            this data value list
        """

        return len(self.__data)

    def equalDimensions(self, dataValueList: DataValueList) -> bool:
        """
        Checks if the two given data value lists have the same number
        of elements

        :param dataValueList: The data value list whose size is to be
            compared with this one
        :return: True if the two given data value lists have the same
            number of elements, False otherwise
        """

        return len(self) == len(dataValueList)

    def __getitem__(self, index: int) -> Union[int, float, complex, Quaternion]:
        """
        Returns the elements at the given index

        :param index: The index of the element to
            be returned
        :return: The element at the given index
        :raises IndexError: Raised if the given index
            is outside the bounds of this data value
            list
        """

        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        return self.__data[index]

    def mean(self) -> Optional[Union[int, float, complex, Quaternion]]:
        """
        Returns the mean of this data value list

        :return: The mean of this data value list
        :raises ArithmeticError: Raised if this list
            is empty
        """

        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            return sum(self.__data) / len(self)

    def median(self) -> Optional[Union[int, float, complex, Quaternion]]:
        """
        Returns the median of this data value list

        :return: The median of this data value list
        :raises ArithmeticError: Raised if this list
            is empty
        """

        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            mid = round(len(self) / 2)

            if len(self) & 1 == 0:
                return (self.__sorted[mid] + self.__sorted[mid + 1]) / 2
            else:
                return self.__sorted[mid]

    def mode(self) -> DataValueList:
        """
        Returns the mode of this data value list

        :return: The mode of this data value list
        :raises ArithmeticError: Raised if this
            list is empty
        """

        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            currentModes = []
            countOfMode = 1
            currentValue = None
            countOfCurrent = 1

            for value in self.__sorted:
                if value == currentValue:
                    countOfCurrent += 1
                else:
                    countOfCurrent = 1
                    currentValue = value

                if countOfCurrent == countOfMode:
                    currentModes.append(currentValue)
                elif countOfCurrent > countOfMode:
                    currentModes.clear()
                    currentModes.append(currentValue)
                    countOfMode = countOfCurrent

            return DataValueList(currentModes)

    def midrange(self) -> Union[int, float, complex, Quaternion]:
        """
        Returns the midrange of this data value list

        :return: The midrange of this data value list
        :raises ArithmeticError: Raised if this list
            is empty
        """

        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            return (self.__sorted[0] + self.__sorted[len(self) - 1]) / 2

    def range(self) -> Union[int, float, complex, Quaternion]:
        """
        Returns the range of this data value list

        :return: The range of this data value list
        :raises ArithmeticError:
        """

        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            return self.__sorted[len(self) - 1] - self.__sorted[0]

    def variance(self) -> Union[int, float, complex, Quaternion]:
        """
        Returns the variance of this data value list

        :return: The variance of this data value list
        :raises ArithmeticError: Raised if this list
            is empty
        """

        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            meanValue = self.mean()
            variance = 0

            for value in self:
                variance += (value - meanValue) ** 2

            variance /= len(self) - 1

            return variance

    def standardDeviation(self) -> Union[int, float, complex, Quaternion]:
        """
        Returns the standard deviation of this data value list

        :return: The standard deviation of this data value list
        :raises ArithmeticError: Raised if this list is empty
        """

        return sqrtMath(self.variance())

    def percentileOf(self, value) -> Union[int, float]:
        """
        Computes the percentile of the given value

        :param value: The value whose percentile in
            this data value list will be computed
        :return: The percentile of the given value
        """

        if len(self) == 0:
            return 1
        else:
            sortedPosition = bisect_left(self.__sorted, value)

            return round((sortedPosition / len(self)) * 100)

    def percentileIn(self, percentile):
        """
        Computes the value that would fall into the
        given percentile

        :param percentile: The percentile of the value
            to be computed
        :return: The value that falls into the given
            percentile
        :raises ArithmeticError: Raised if this list
            is empty
        """

        if len(self) == 0:
            raise ArithmeticError("List is empty")
        else:
            position = (percentile * len(self)) / 100

            if position.is_integer():
                position = int(position)

                return (self.__sorted[position] + self.__sorted[position + 1]) / 2
            else:
                position = ceil(position)

                return self.__sorted[position]

    def __copy__(self) -> DataValueList:
        """
        Creates a shallow copy of this data value list

        :return: A shallow copy of this data value list
        """

        return DataValueList(self.__data)

    def __deepcopy__(self, memodict: dict={}) -> DataValueList:
        """
        Creates a deep copy of this data value list

        :param memodict: N/A
        :return: A deep copy of this data value list
        """

        return DataValueList(copy(self.__data))

    def __iter__(self) -> Iterator[Union[int, float, complex, Quaternion]]:
        """
        Returns an iterator over the elements of this data value list

        :return: An iterator over the elements of this data value list
        """

        return iter(self.__data)

    def sorted(self) -> DataValueList:
        """
        Returns a version of this data value list
        that has its elements sorted

        :return: A sorted version of this data value
            list
        """

        return DataValueList(self.__sorted)

    def __str__(self) -> str:
        """
        Returns a string representation of this data
        value list

        :return: A string representation of this data
            value list
        """

        rep = "["

        for index in range(len(self)):
            if index != len(self) - 1:
                rep += str(self[index]) + ", "
            else:
                rep += "]"

        return rep
