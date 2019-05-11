from __future__ import annotations
from typing import Union, List, Tuple, Iterator, NoReturn
from sys import float_info
from calc.MathFunction import sqrtMath
from calc.Quaternion import Quaternion


class ProbabilityDistribution:
    """
    Represents a probability distribution. While a data value can be a int, float, complex or Quaternion, not all
    functions will not work if a given ProbabilityDistribution contains a complex and/or a Quaternion
    """

    def __init__(self, data: List[Tuple[Union[int, float, complex, Quaternion], float]]):
        """
        Constructs the probability distribution with the given data.
        The data should be a list of tuples whose first value is any numeric value and whose second value
        is a number between 0 and 1.  The sum of each tuples second value should sum up to 1. The first element of each
        tuple is a data value. The second element of each tuple is the probability of getting that value

        :param data: A list of tuples with each tuple having two values. The first value is any numeric value.
            The second value is a number between 0 and 1. The sum of all second values in each tuple should add up to 1
        """

        self.__data = data
        self.__sortedData = None

    def __sort(self) -> NoReturn:
        """
        Checks if the data is sorted. If it is not, the data is sorted. Otherwise, this method
        does nothing

        :return: None
        """

        if self.__sortedData is None:
            self.__sortedData = sorted(self.__data, key=lambda entry: entry[0])

    def __len__(self) -> int:
        """
        Returns the number of items in this probability distribution

        :return: The number of items in this probability distribution
        """

        return len(self.__data)

    def getItem(self, index: int) -> Tuple[Union[int, float, complex, Quaternion], float]:
        """
        Returns the value and its probability at the given index

        :param index: The index of the item to be obtained
        :return: The value and its corresponding probability that is at the given index
        :raises IndexError: Raised if the index is outside the bounds of the list of values
        """

        if index < 0 or index >= len(self):
            raise IndexError("index out of bounds")

        return self.__data[index]

    def getSortedItem(self, index: int) -> Tuple[Union[int, float], float]:
        """
        Returns the value and its probability at the given sorted position. This method should be used to find
        the nth largest element

        :param index: The index of the sorted position of the element to be obtained
        :return: The value and its corresponding probability at the given sorted position
        """

        if index < 0 or index >= len(self):
            raise IndexError("index out of bounds")

        self.__sort()
        return self.__sortedData[index]

    def min(self) -> Union[int, float]:
        """
        Searches for the minimum value

        :return: The minimum value
        :raises TypeError: Raised if any data value is a complex or a Quaternion
        """

        if self.__sortedData is not None:
            return self.__sortedData[0]
        else:
            minValue = float_info.max

            for (value, probability) in self:
                if value < minValue:
                    minValue = value

            return minValue

    def max(self) -> Union[int, float]:
        """
        Searches for the maximum value

        :return: The maximum value
        :raises TypeError: Raised if any data value is a complex or a Quaternion
        """

        if self.__sortedData is not None:
            return self.__sortedData[len(self) - 1]
        else:
            maxValue = float_info.min

            for (value, probability) in self:
                if value > maxValue:
                    maxValue = value

            return maxValue

    def mean(self) -> Union[int, float, complex, Quaternion]:
        """
        Computes the mean of this probability distribution

        :return: The mean of this probability distribution
        """

        meanValue = 0

        for (value, probability) in self:
            meanValue += value * probability

        return meanValue

    def median(self) -> Union[int, float]:
        """
        Searches for the median of this probability distribution

        :return: The median of this probability distribution
        :raises TypeError: Raised if any data value is a complex or a Quaternion
        """

        self.__sort()
        mid = len(self) // 2

        if len(self) % 2 == 0:
            return (self.__sortedData[mid][0] + self.__sortedData[mid + 1][0]) / 2
        else:
            return self.__sortedData[mid + 1][0]

    def mode(self) -> List[int, float, complex, Quaternion]:
        """
        Computes the mode of this probability distribution

        :return: The mode of this probability distribution
        """

        modes = []

        try:
            self.__sort()

            countOfMode = 1
            index = 0

            while index < len(self):
                current = self.__sortedData[index]
                countOfCurrent = 0

                while current[0] == self.__sortedData[index][0]:
                    countOfCurrent += 1
                    index += 1

                    if index >= len(self):
                        break

                if countOfCurrent == countOfMode and countOfMode != 1:
                    modes.append(current[0])
                elif countOfCurrent > countOfMode:
                    countOfMode = countOfCurrent

                    modes.clear()
                    modes.append(current[0])
        except TypeError:
            counts = {}

            for (value, probability) in self:
                if value in counts:
                    counts[value] += 1
                else:
                    counts[value] = 1

            countOfMode = None

            for (value, count) in counts.items():
                if count > countOfMode:
                    modes.clear()
                    modes.append(value)

                    countOfMode = count
                elif count == countOfMode and count != -1:
                    modes.append(value)

        return modes

    def midrange(self) -> Union[int, float]:
        """
        Computes the midrange of this probability distribution

        :return: The midrange of this probability distribution
        :raises TypeError: Raised if any data value is a complex or a Quaternion
        """

        self.__sort()

        return (self.__sortedData[len(self) - 1][0] + self.__sortedData[0][0]) / 2

    def range(self) -> Union[int, float]:
        """
        Computes the range of this probability distribution

        :return: The range of this probability distribution
        :raises TypeError: Raised if any data value is a complex or a Quaternion
        """

        self.__sort()

        return self.__sortedData[len(self) - 1][0] - self.__sortedData[0][0]

    def variance(self) -> Union[int, float, complex, Quaternion]:
        """
        Computes the variance of this probability distribution

        :return: The variance of this probability distribution
        """

        varianceValue = 0

        for (value, probability) in self:
            varianceValue += value * value * probability

        varianceValue -= self.mean() ** 2

        return varianceValue

    def standardDeviation(self) -> Union[int, float, complex, Quaternion]:
        """
        Computes the standard deviation of this probability distribution

        :return: The standard deviation of this probability distribution
        """

        return sqrtMath(self.variance())

    def __iter__(self) -> Iterator[Tuple[Union[int, float, complex, Quaternion], float]]:
        """
        Returns an iterator over the values and their corresponding probabilities

        :return: An iterator over the values and their corresponding probabilities
        """

        return iter(self.__data)

    def __hash__(self) -> int:
        """
        Computes a hash code for this probability distribution

        :return: A hash code for this probability distribution
        """

        MODIFIER = 31
        hashCode = 0

        for entry in self:
            hashCode += MODIFIER * hash(entry)

        return hashCode

    def __eq__(self, distribution: ProbabilityDistribution) -> bool:
        """
        Checks if this probability distribution contains the same values and if those values have the same
        probabilities

        :param distribution: Another probability distribution
        :return: True if both probability distributions are equal, False otherwise
        """

        if len(self) != len(distribution):
            return False

        for (leftEntry, rightEntry) in zip(self, distribution):
            if leftEntry != rightEntry:
                return False

        return True

    def __ne__(self, distribution: ProbabilityDistribution) -> bool:
        """
        Checks if this probability distribution does not contain the same values and/or if those values have the
        different probabilities

        :param distribution: Another probability distribution
        :return: True if both probability distributions are not equal, False otherwise
        """

        return not (self == distribution)

    def __str__(self) -> str:
        """
        Returns a string representation of this probability distribution

        :return: A string representation of this probability distribution
        """

        return str(self.__data)

    def __repr__(self) -> str:
        """
        Returns a string representation of this probability distribution for the Python shell

        :return: A string representation of this probability distribution for the Python shell
        """

        return str(self)
