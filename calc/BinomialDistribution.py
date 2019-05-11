from __future__ import annotations
from math import sqrt


class BinomialDistribution:
    """
    Represents a binomial distribution. A binomial distribution consists of a given number of trials and a probability
    of success for each trial
    """

    def __init__(self, numberOfTrials: int, success: float):
        """
        Constructs a binomial distribution with the given number of trials and the given probability of success

        :param numberOfTrials: The number of trials
        :param success: The probability of success
        """

        if numberOfTrials < 1:
            raise ArithmeticError("The number of trials must be positive")
        if success < 0 or success > 1:
            raise ArithmeticError("The probability of success must be between 0 and 1")

        self.__numberOfTrials = numberOfTrials
        self.__success = success

    @property
    def numberOfTrials(self) -> int:
        """
        Returns the number of trials

        :return: The number of trials
        """

        return self.__numberOfTrials

    @property
    def success(self) -> float:
        """
        Returns the probability of success

        :return: The probability of success
        """

        return self.__success

    @property
    def failure(self) -> float:
        """
        Returns the probability of failure

        :return: The probability of failure
        """

        return 1 - self.__success

    def mean(self) -> float:
        """
        Computes the mean of this binomial distribution

        :return: The mean of this binomial distribution
        """

        return self.__numberOfTrials * self.__success

    def variance(self) -> float:
        """
        Computes the variance of this binomial distribution

        :return: The variance of this binomial distribution
        """

        return self.mean() * self.failure

    def standardDeviation(self) -> float:
        """
        Computes the standard deviation of this binomial distribution

        :return: The standard deviation of this binomial distribution
        """

        return sqrt(self.variance())

    def __eq__(self, distribution: BinomialDistribution) -> bool:
        """
        Checks if both binomial distributions have the same number of trials and the same probability of success

        :param distribution: Another binomial distribution
        :return: True if both binomial distributions are equal, False otherwise
        """

        return self.__numberOfTrials == distribution.__numberOfTrials and self.__success == distribution.__success

    def __ne__(self, distribution: BinomialDistribution) -> bool:
        """
        Checks if both binomial distributions have a different number of trials or a different probability of success

        :param distribution: Another binomial distribution
        :return: True if both binomial distributions are not equal, False otherwise
        """

        return not (self == distribution)

    def __str__(self) -> str:
        """
        Returns a string representation of this binomial distribution

        :return: A string representation of this binomial distribution
        """

        return "(# of trials: " + str(self.__numberOfTrials) + \
               "), (success: " + str(self.__success) + \
               "), (failure: " + str(self.failure) + ")"

    def __repr__(self) -> str:
        """
        Returns a string representation of this binomial distribution for the Python shell

        :return: A string representation of this binomial distribution for the Python shell
        """

        return str(self)
