class Negatable:
    """
    This class should be extended by classes that extend the MathEntity
    class. Instances of this class overload the negation operator
    """

    def __pos__(self):
        """
        Returns a reference to this mathematical entity

        :return: This mathematical entity
        """

        return self

    def __neg__(self):
        """
        Negates this mathematical entity

        :return: The negation of this mathematical entity
        """

        from calc._OperationMediator import doNegation

        return doNegation(self)
