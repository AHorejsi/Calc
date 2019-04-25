from __future__ import annotations
from math import sqrt


class BinomialDistribution:
    def __init__(self, numberOfTrials: int, success: float):
        if numberOfTrials < 1:
            raise ArithmeticError("The number of trials must be positive")

        if success < 0 or success > 1:
            raise ArithmeticError("The probability of success must be between 0 and 1")

        self.__numberOfTrials = numberOfTrials
        self.__success = success

    @property
    def numberOfTrials(self) -> int:
        return self.__numberOfTrials

    @property
    def success(self) -> float:
        return self.__success

    @property
    def failure(self) -> float:
        return 1 - self.__success

    def mean(self) -> float:
        return self.__numberOfTrials * self.__success

    def variance(self) -> float:
        return self.__numberOfTrials * self.__success * self.failure

    def standardDeviation(self) -> float:
        return sqrt(self.variance())

    def __eq__(self, distribution: BinomialDistribution) -> bool:
        return self.__numberOfTrials == distribution.__numberOfTrials and self.__success == distribution.__success

    def __ne__(self, distribution: BinomialDistribution) -> bool:
        return not (self == distribution)

    def __str__(self) -> str:
        return "(# of trials: " + str(self.__numberOfTrials) + \
               "), (success: " + str(self.__success) + \
               "), (failure: " + str(self.failure) + ")"
