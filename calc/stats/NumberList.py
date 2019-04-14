from __future__ import annotations
from typing import Union, List, Iterator, NoReturn
from calc.entities.MathEntity import MathEntity
from calc.entities.Quaternion import Quaternion
from calc.functions.MathFunction import sqrtMath


class NumberList(MathEntity):
    def __init__(self, data: List[Union[int, float, complex, Quaternion]]):
        """
        Uses the given list of values to represent a
        list of numbers

        :param data: The list of values to be contained
            in this list of numbers
        """

        self.__data = data

    def __len__(self) -> int:
        """
        Returns the number of elements in this number list

        :return: The number of elements in this number list
        """

        return len(self.__data)

    def __getitem__(self, index: int) -> Union[int, float, complex, Quaternion]:
        """
        Returns the element at the given index

        :param index: The index of the element
            to be returned
        :return: The number at the given index
        :raises IndexError: Raised if the given
            index is outside of the bounds of this
            list
        """

        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        return self.__data[index]

    def __setitem__(self, index: int, value: Union[int, float, complex, Quaternion]) -> NoReturn:
        """
        Changes the value at the given index

        :param index: The index of the element
            to be changed
        :param value: The new value to be placed
            into this list
        :return: None
        :raises IndexError: Raised if the given
            index is outside the bounds of this
            list
        """

        if index < 0 or index >= len(self):
            raise IndexError("Invalid index")

        self.__data[index] = value

    def mean(self) -> Union[int, float, complex, Quaternion]:
        """
        Returns the mean of this list of numbers

        :return: The mean of this list of numbers
        """

        return sum(self) / len(self)

    def median(self) -> Union[int, float]:
        """
        Returns the median of thsi list of numbers

        :return: The median of this list of numbers
        :raises AttributeError: Raised if this list
            contains either complex number or
            quaternions
        """

        sortedData = sorted(self.__data)
        mid = round(len(self) / 2)

        if len(self) % 2 == 0:
            return (sortedData[mid] + sortedData[mid + 1]) / 2
        else:
            return sortedData[mid]

    def mode(self) -> List[Union[int, float, complex, Quaternion]]:
        """
        Returns the mode of this list of numbers

        :return: The mode of this list of numbers
        """

        counts = {}

        for value in self:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1

        modes = []
        countOfModes = -1

        for (value, count) in counts.items():
            if count > countOfModes:
                modes.clear()
                modes.append(value)
                countOfModes = count
            elif count == countOfModes and count != -1:
                modes.append(value)

        return modes

    def midrange(self) -> Union[int, float]:
        """
        Returns the midrange of this list of numbers

        :return: The midrange of this list of numbers
        :raises AttributeError: Raised if this list
            contains complex numbers or quaternions
        """

        sortedData = sorted(self.__data)

        return (sortedData[0] + sortedData[len(self) - 1]) / 2

    def range(self) -> Union[int, float]:
        """
        Returns the range of this list of numbers

        :return: The range of this list of numbers
        :raises AttributeError: Raised if this list
            contains complex numbers or quaternions
        """

        sortedData = sorted(self.__data)

        return sortedData[len(self) - 1] - sortedData[0]

    def variance(self) -> Union[int, float, complex, Quaternion]:
        """
        Returns the variance of this list of numbers

        :return: The variance of this list of numbers
        """

        meanValue = self.mean()
        result = 0

        for value in self:
            result += (value - meanValue) ** 2

        result /= len(self) - 1

        return result

    def standardDeviation(self) -> Union[int, float, complex, Quaternion]:
        """
        Returns the standard deviation of this list of numbers

        :return: The standard deviation of this list of numbers
        """

        return sqrtMath(self.variance())

    def __iter__(self) -> Iterator[Union[int, float, complex, Quaternion]]:
        """
        Returns an iterator over the elements of this list of
        numbers

        :return: An iterator over the elements of this list of
            numbers
        """

        return iter(self.__data)

    def __hash__(self) -> int:
        """
        Computes a hash code for this list of numbers

        :return: A hash code for this list of numbers
        """

        hashCode = 0
        MODIFIER = 31

        for value in self:
            hashCode += MODIFIER * hash(value)

        return hashCode

    def __str__(self) -> str:
        """
        Returns a string representation of this list
        of numbers

        :return: A string representation of this list
            of numbers
        """

        rep = "{"

        for index in range(len(self)):
            rep += str(self[index])

            if index == len(self) - 1:
                rep += "}"
            else:
                rep += ", "

        return rep
