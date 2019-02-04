from __future__ import annotations
from typing import Union, Optional
from math import nan


class MathEntity(object):
    """
    Superclass for all mathematical entities that represent some type of mathematical
    value. Contains the operations of addition, subtraction, multiplication, division
    and floor division. Any implementing subclass does not need to implement all of
    these operations
    """

    def __add__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs addition with this entity on the left side of the
        addition operator and another mathematical entity on the

        :param mathEntity: The mathematical entity being added to this
            entity
        :return: The sum of this entity and the given entity
        """

        from calc._OperationMediator import doAddition

        return doAddition(self, mathEntity)

    def __iadd__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Updates the value of this entity by performing addition with
        this entity on the left side of the addition operator and another
        mathematical entity on the right side.
        :param mathEntity: The mathematical entity being added to this
            entity
        :return: The sum of this entity and the given entity
        """

        return self + mathEntity

    def __radd__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs addition with this entity on the right side of the
        addition operator and another mathematical entity on the
        left side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity that this entity
            is being added to
        :return: The sum of the given entity and this entity
        """

        from calc._OperationMediator import doAddition

        return doAddition(mathEntity, self)

    def __sub__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs subtraction with this entity on the left side of the
        subtraction operator and another mathematical entity on the
        right side

        :param mathEntity: The mathematical entity being subtracted from
            this entity
        :return: The difference of this entity and the given entity
        """

        from calc._OperationMediator import doSubtraction

        return doSubtraction(self, mathEntity)

    def __isub__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Updates the value of this entity by performing subtraction with
        this entity on the left side of the subtraction operator and another
        mathematical entity on the right side

        :param mathEntity: The mathematical entity being subtracted this
            entity
        :return: The difference of this entity and the given entity
        """

        return self - mathEntity

    def __rsub__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs subtraction with this entity on the right side of the
        subtraction operator and another mathematical entity on the
        left side

        :param mathEntity: The mathematical entity that this entity
            is being subtracted from
        :return: The difference of the given entity and this entity
        """

        from calc._OperationMediator import doSubtraction

        return doSubtraction(mathEntity, self)

    def __mul__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs multiplication with this entity on the left side of the
        multiplication operator and another mathematical entity on the
        right side

        :param mathEntity: The mathematical entity being multiplied to
            this entity
        :return: The product of this entity and the given entity
        """

        from calc._OperationMediator import doMultiplication

        return doMultiplication(self, mathEntity)

    def __imul__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Updates the value of this entity by performing multiplication with
        this entity on the left side of the multiplication operator and another
        mathematical entity on the right side

        :param mathEntity: The mathematical entity being multiplied to this
            entity
        :return: The product of this entity and the given entity
        """

        return self * mathEntity

    def __rmul__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs multiplication with this entity on the right side of the
        multiplication operator and another mathematical entity on the
        left side

        :param mathEntity: The mathematical entity that this entity
            is being multiplied to
        :return: The product of the given entity and this entity
        """

        from calc._OperationMediator import doMultiplication

        return doMultiplication(mathEntity, self)

    def __truediv__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs division with this entity on the left side of the
        division operator and another mathematical entity on the
        right side

        :param mathEntity: The mathematical entity being divided from
            this entity
        :return: The quotient of this entity and the given entity
        """

        from calc._OperationMediator import doDivision

        return doDivision(self, mathEntity)

    def __itruediv__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Updates the value of this entity by performing division with
        this entity on the left side of the division operator and another
        mathematical entity on the right side

        :param mathEntity: The mathematical entity being divided from this
            entity
        :return: The quotient of this entity and the given entity
        """

        return self / mathEntity

    def __rtruediv__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs division with this entity on the right side of the
        division operator and another mathematical entity on the
        left side

        :param mathEntity: The mathematical entity that this entity
            is being divided from
        :return: The quotient of the given entity and this entity
        """

        from calc._OperationMediator import doDivision

        return doDivision(mathEntity, self)

    def __floordiv__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs floor division with this entity on the left side of the
        floor division operator and another mathematical entity on the
        right side

        :param mathEntity: The mathematical entity being divided from
            this entity
        :return: The floor quotient of this entity and the given entity
        """

        from calc._OperationMediator import doFloorDivision

        return doFloorDivision(self, mathEntity)

    def __ifloordiv__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Updates the value of this entity by performing floor division with
        this entity on the left side of the floor division operator and another
        mathematical entity on the right side

        :param mathEntity: The mathematical entity being floor divided from
            this entity
        :return: The floor quotient of this entity and the given entity
        """

        return self // mathEntity

    def __rfloordiv__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
        """
        Performs floor division with this entity on the right side of the
        floor division operator and another mathematical entity on the
        left side

        :param mathEntity: The mathematical entity that this entity
            is being floor divided from
        :return: The floor quotient of the given entity and this entity
        """

        from calc._OperationMediator import doFloorDivision

        return doFloorDivision(mathEntity, self)

    def __pow__(self: MathEntity, mathEntity: Union[MathEntity, int, float], modulo: Optional[int]=None) -> Union[MathEntity, nan]:
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

        from calc._OperationMediator import doExponentiation

        return doExponentiation(self, mathEntity)

    def __ipow__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
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

    def __rpow__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> Union[MathEntity, nan]:
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

        from calc._OperationMediator import doExponentiation

        return doExponentiation(mathEntity, self)

    def __pos__(self: MathEntity) -> MathEntity:
        """
        Returns a reference to this mathematical entity

        :return: This mathematical entity
        """

        return self

    def __neg__(self: MathEntity) -> Union[MathEntity, nan]:
        """
        Negates this mathematical entity

        :return: The negation of this mathematical entity
        """

        from calc._OperationMediator import doNegation

        return doNegation(self)

    def __eq__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> bool:
        """
        Checks if this mathematical entity is equal to
        another mathematical entity

        :param mathEntity: The entity that this entity is be compared
            to in order to check for equality
        :return: True if the two given mathematical entities are equal,
            false otherwise
        """

        from calc._OperationMediator import doEquality

        return doEquality(self, mathEntity)

    def __ne__(self: MathEntity, mathEntity: Union[MathEntity, int, float]) -> bool:
        """
        Checks if this mathematical entity is not equal to
        another mathematical entity

        :param mathEntity: The entity that this entity is be compared
            to in order to check for inequality
        :return: True if the two given mathematical entities are unequal,
            false otherwise
        """

        return not (self == mathEntity)

    def __repr__(self: MathEntity) -> str:
        """
        Returns a string for the Python shell. Returns the
        same string as the __str__ method

        :return: A string representation for the Python shell
        """

        return str(self)
