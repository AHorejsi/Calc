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
        Multiplies the given mathematical entity by -1 by default.
        Therefore, the multiplication operator must be overloaded
        for this method to work. Override this method if that
        behavior does not negate a given kind of mathematical entity

        :return: The negation of this mathematical entity
        """

        return self * -1
