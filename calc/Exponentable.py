from calc.MathFunction import exp, log


class Exponentable:
    """
    Instances of this class are instances of MathEntity
    which are capable of exponent operations
    """

    def __pow__(self, mathEntity, modulo=None):
        """
        Takes this mathematical entity to the power of
        another mathematical entity

        :param mathEntity: The mathematical entity
            that is acts as the exponent for this
            operation
        :param modulo: Another mathematical entity
            that the result of this mathematical entity
            taken to the power of another mathematical
            entity will be modded by
        :return: The result of taking this mathematical
            entity to the power of this another mathematical
            entity
        """

        return exp(log(self) * mathEntity)

    def __ipow__(self, mathEntity):
        """
        Updates this mathematical entity by taking this
        mathematical entity to the power of
        another mathematical entity

        :param mathEntity: The mathematical entity
            that is acts as the exponent for this
            operation
        :return: The result of taking this mathematical
            entity to the power of this another mathematical
            entity
        """

        return self ** mathEntity

    def __rpow__(self, mathEntity):
        """
        Takes another mathematical entity to the power of
        this mathematical entity

        :param mathEntity: The mathematical entity
            that is acts as the base for this
            operation
        :param modulo: Another mathematical entity
            that the result of another mathematical entity
            taken to the power of this mathematical
            entity will be modded by
        :return: The result of taking another mathematical
            entity to the power of this this mathematical
            entity
        """

        return exp(log(mathEntity) * self)
