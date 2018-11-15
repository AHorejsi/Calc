class MathEntity:
    """
    Instances of this class represent some kind of mathematical entity. All types
    that extend this class must be capable of any of the following operations with
    itself or some other type of mathematical entity: addition, subtraction,
    multiplication, division, floor division, negation, rounding, equality.
    If a particular unary or binary operation cannot be performed on particular
    entity or entities, a TypeError should be raised

    Written by: Alex Horejsi
    """

    def __add__(self, entity):
        """
        Adds another mathematical entity to this one. Both mathematical entities must be of appropriate
        type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being added to this one
        :return: The sum of this entity and the given entity
        :exception TypeError: Raised when (self + entity) is not possible
        """

        from cal.Operations import addition

        return addition(self, entity)

    def __iadd__(self, entity):
        """
        Adds another mathematical entity to this one. Both mathematical entities must be of appropriate
        type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being added to this one
        :return: The sum of this entity and the given entity
        :exception TypeError: Raised when (self + entity) is not possible
        """

        return self + entity

    def __radd__(self, entity):
        """

        Adds this mathematical entity to another. Both mathematical entities must be of appropriate
        type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being added to this one
        :return: The sum of this entity and the given entity
        :exception TypeError: Raised when (entity + self) is not possible
        """

        from cal.Operations import addition

        return addition(entity, self)

    def __sub__(self, entity):
        """
        Subtracts another mathematical entity from this one. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being subtracted from this one
        :return: The difference of this entity and the given entity
        :exception TypeError: Raised when (self - entity) is not possible
        """

        from cal.Operations import subtraction

        return subtraction(self, entity)

    def __isub__(self, entity):
        """
        Subtracts another mathematical entity from this one. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being subtracted from this one
        :return: The difference of this entity and the given entity
        :exception TypeError: Raised when (self - entity) is not possible
        """

        return self - entity

    def __rsub__(self, entity):
        """
        Subtracts this mathematical entity from another one. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being subtracted by this one
        :return: The difference of the given entity and this one
        :exception TypeError: Raised when (entity - self) is not possible
        """

        from cal.Operations import subtraction

        return subtraction(entity, self)

    def __mul__(self, entity):
        """
        Multiplies this mathematical entity by another. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being multiplied to this one
        :return:  The product of this entity and the given entity
        :exception TypeError: Raise when (self * entity) is not possible
        """

        from cal.Operations import multiplication

        return multiplication(self, entity)

    def __imul__(self, entity):
        """
        Multiplies this mathematical entity by another. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being multiplied to this one
        :return:  The product of this entity and the given entity
        :exception TypeError: Raise when (self * entity) is not possible
        """

        return self * entity

    def __rmul__(self, entity):
        """
        Multiplies another mathematical entity by this one. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being multiplied by this one
        :return:  The product of the given entity and this one
        :exception TypeError: Raised when (entity - self) is not possible
        """

        from cal.Operations import multiplication

        return multiplication(entity, self)

    def __truediv__(self, entity):
        """
        Divides this mathematical entity by another. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being divided from this one
        :return: The quotient of this entity and the given entity
        :exception TypeError: Raised when (self / entity) is not possible
        """

        from cal.Operations import division

        return division(self, entity)

    def __itruediv__(self, entity):
        """
        Divides this mathematical entity by another. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being divided from this one
        :return: The quotient of this entity and the given entity
        :exception TypeError: Raised when (self / entity) is not possible
        """

        return self / entity

    def __rtruediv__(self, entity):
        """
        Divides another mathematical entity by this one. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being divided by this entity
        :return: The quotient of the given entity and this entity
        :exception TypeError: Raised when (entity / self) is not possible
        """

        from cal.Operations import division

        return division(entity, self)

    def __floordiv__(self, entity):
        """
        Floor divides this mathematical entity by another. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being floor divided from this entity
        :return: The floor quotient of this entity and the given entity
        :exception TypeError: Raised when (self // entity) is not possible
        """

        from cal.Operations import floorDivision

        return floorDivision(self, entity)

    def __ifloordiv__(self, entity):
        """
        Floor divides this mathematical entity by another. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being floor divided from this entity
        :return: The floor quotient of this entity and the given entity
        :exception TypeError: Raised when (self // entity) is not possible
        """

        return self // entity

    def __rfloordiv__(self, entity):
        """
        Floor divides another mathematical entity by this one. Both mathematical entities must be of
        appropriate type and on an appropriate side of the operator to be a valid mathematical
        expression

        :param entity: The mathematical entity being floor divided by this entity
        :return: The floor quotient of the given entity and this entity
        :exception TypeError: Raised when (entity // self) is not possible
        """

        from cal.Operations import floorDivision

        return floorDivision(entity, self)

    def __neg__(self):
        """
        Calculates the negation of this mathematical entity. This entity must be negatable

        :return: The negation of this mathematical entity
        :exception TypeError: Raised when (-self) is not possible
        """

        from cal.Operations import negation

        return negation(self)

    def __round__(self, decimalNum=None):
        """
        Rounds this mathematical entity to the given number of decimal places.
        If the given mathematical entity is composed of multiple numbers, then
        each component will be rounded to the given number of decimal places

        :param decimalNum: The number of decimal places to be rounded to
        :return: This entity with all of its components rounded to the given number of decimal places
        :exception TypeError: Raised when no rounding can be done
        """

        from cal.Operations import rounding

        if decimalNum is None:
            return rounding(self)
        else:
            return rounding(self, decimalNum)

    def __eq__(self, entity):
        """
        Checks if two mathematical entities are equal. Both mathematical entities
        do not need to be of the same type to be equal

        :param entity: The entity being tested against this entity for equality
        :return: True if both entities are equal, False otherwise
        """

        from cal.Operations import equality

        return equality(self, entity)

    def __ne__(self, entity):
        """
        Checks if two mathematical entities are not equal

        :param entity: The entity being tested against this entity for inequality
        :return: True if the two entities are not equal, False otherwise
        """

        return not self == entity
