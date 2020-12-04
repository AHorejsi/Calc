from __future__ import annotations
from typing import Union, Optional


class MathEntity:
    """
    Superclass for all mathematical entities that represent some type of mathematical
    value. Contains the operations of addition, subtraction, multiplication, division
    and floor division. Any implementing subclass does not need to implement all of
    these operations
    """

    def __add__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs addition with this entity on the left side of the
        addition operator and another mathematical entity on the

        :param mathEntity: The mathematical entity being added to this
            entity
        :return: The sum of this entity and the given entity
        """

        from calc._AdditionMediator import doAddition

        return doAddition(self, mathEntity)

    def __iadd__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Updates the value of this entity by performing addition with
        this entity on the left side of the addition operator and another
        mathematical entity on the right side.
        :param mathEntity: The mathematical entity being added to this
            entity
        :return: The sum of this entity and the given entity
        """

        return self + mathEntity

    def __radd__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs addition with this entity on the right side of the
        addition operator and another mathematical entity on the
        left side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity that this entity
            is being added to
        :return: The sum of the given entity and this entity
        """

        from calc._AdditionMediator import doAddition

        return doAddition(mathEntity, self)

    def __sub__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs subtraction with this entity on the left side of the
        subtraction operator and another mathematical entity on the
        right side

        :param mathEntity: The mathematical entity being subtracted from
            this entity
        :return: The difference of this entity and the given entity
        """

        from calc._SubtractionMediator import doSubtraction

        return doSubtraction(self, mathEntity)

    def __isub__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Updates the value of this entity by performing subtraction with
        this entity on the left side of the subtraction operator and another
        mathematical entity on the right side

        :param mathEntity: The mathematical entity being subtracted this
            entity
        :return: The difference of this entity and the given entity
        """

        return self - mathEntity

    def __rsub__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs subtraction with this entity on the right side of the
        subtraction operator and another mathematical entity on the
        left side

        :param mathEntity: The mathematical entity that this entity
            is being subtracted from
        :return: The difference of the given entity and this entity
        """

        from calc._SubtractionMediator import doSubtraction

        return doSubtraction(mathEntity, self)

    def __mul__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs multiplication with this entity on the left side of the
        multiplication operator and another mathematical entity on the
        right side

        :param mathEntity: The mathematical entity being multiplied to
            this entity
        :return: The product of this entity and the given entity
        """

        from calc._MultiplicationMediator import doMultiplication

        return doMultiplication(self, mathEntity)

    def __imul__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Updates the value of this entity by performing multiplication with
        this entity on the left side of the multiplication operator and another
        mathematical entity on the right side

        :param mathEntity: The mathematical entity being multiplied to this
            entity
        :return: The product of this entity and the given entity
        """

        return self * mathEntity

    def __rmul__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs multiplication with this entity on the right side of the
        multiplication operator and another mathematical entity on the
        left side

        :param mathEntity: The mathematical entity that this entity
            is being multiplied to
        :return: The product of the given entity and this entity
        """

        from calc._MultiplicationMediator import doMultiplication

        return doMultiplication(mathEntity, self)

    def __truediv__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs division with this entity on the left side of the
        division operator and another mathematical entity on the
        right side

        :param mathEntity: The mathematical entity being divided from
            this entity
        :return: The quotient of this entity and the given entity
        """

        from calc._DivisionMediator import doDivision

        return doDivision(self, mathEntity)

    def __itruediv__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Updates the value of this entity by performing division with
        this entity on the left side of the division operator and another
        mathematical entity on the right side

        :param mathEntity: The mathematical entity being divided from this
            entity
        :return: The quotient of this entity and the given entity
        """

        return self / mathEntity

    def __rtruediv__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
        """
        Performs division with this entity on the right side of the
        division operator and another mathematical entity on the
        left side

        :param mathEntity: The mathematical entity that this entity
            is being divided from
        :return: The quotient of the given entity and this entity
        """

        from calc._DivisionMediator import doDivision

        return doDivision(mathEntity, self)

    def __pow__(self, mathEntity: Union[MathEntity, int, float, complex], modulo: Optional[int]=None) -> Union[MathEntity, float]:
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

        from calc._ExponentiationMediator import doExponentiation

        return doExponentiation(self, mathEntity)

    def __ipow__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
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

    def __rpow__(self, mathEntity: Union[MathEntity, int, float, complex]) -> Union[MathEntity, float]:
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

        from calc._ExponentiationMediator import doExponentiation

        return doExponentiation(mathEntity, self)

    def __pos__(self) -> MathEntity:
        """
        Returns a reference to this
        mathematical entity

        :return: This mathematical entity
        """

        return self

    def __neg__(self) -> Union[MathEntity, float]:
        """
        Negates this mathematical entity

        :return: The negation of this
            mathematical entity
        """

        return self * -1

    def __eq__(self, mathEntity: Union[MathEntity, int, float, complex]) -> bool:
        """
        Checks if this mathematical entity is equal to
        another mathematical entity

        :param mathEntity: The entity that this entity is be compared
            to in order to check for equality
        :return: True if the two given mathematical entities are equal,
            false otherwise
        """

        from calc._EqualityMediator import doEquality

        return doEquality(self, mathEntity)

    def __ne__(self, mathEntity: Union[MathEntity, int, float, complex]) -> bool:
        """
        Checks if this mathematical entity is not equal to
        another mathematical entity

        :param mathEntity: The entity that this entity is be compared
            to in order to check for inequality
        :return: True if the two given mathematical entities are unequal,
            false otherwise
        """

        return not (self == mathEntity)

    def __repr__(self) -> str:
        """
        Returns a string for the Python shell. Returns the
        same string as the __str__ method

        :return: A string representation for the Python shell
        """

        return str(self)
