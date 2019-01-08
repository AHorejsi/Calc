from math import floor


class MathEntity:
    """
    Superclass for all mathematical entities that represent some kind of mathematical
    value. Contains the operations of addition, subtraction, multiplication, division
    and floor division. Any implementing subclass does not need to implement all of
    these operations
    """

    def __add__(self, mathEntity):
        """
        Performs addition with this entity on the left side of the
        addition operator and another mathematical entity on the
        right side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity being added to this
            entity
        :return: The sum of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        raise ArithmeticError("Left addition is not possible with this type")

    def __iadd__(self, mathEntity):
        """
        Updates the value of this entity by performing addition with
        this entity on the left side of the addition operator and another
        mathematical entity on the right side. By default, this method
        raises an ArithmeticError

        :param mathEntity: The mathematical entity being added to this
            entity
        :return: The sum of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
             override the addition operator
        """

        return self + mathEntity

    def __radd__(self, mathEntity):
        """
        Performs addition with this entity on the right side of the
        addition operator and another mathematical entity on the
        left side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity that this entity
            is being added to
        :return: The sum of the given entity and this entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        raise ArithmeticError("Right addition is not possible with this type")

    def __sub__(self, mathEntity):
        """
        Performs subtraction with this entity on the left side of the
        subtraction operator and another mathematical entity on the
        right side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity being subtracted from
            this entity
        :return: The difference of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        raise ArithmeticError("Left subtraction is not possible with this type")

    def __isub__(self, mathEntity):
        """
        Updates the value of this entity by performing subtraction with
        this entity on the left side of the subtraction operator and another
        mathematical entity on the right side. By default, this method
        raises an ArithmeticError

        :param mathEntity: The mathematical entity being subtracted this
            entity
        :return: The difference of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
             override the subtraction operator
        """

        return self - mathEntity

    def __rsub__(self, mathEntity):
        """
        Performs subtraction with this entity on the right side of the
        subtraction operator and another mathematical entity on the
        left side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity that this entity
            is being subtracted from
        :return: The difference of the given entity and this entity
        :exception ArithmeticError: Raised if the subclass does not
             override this method
        """

        raise ArithmeticError("Right subtraction is not possible with this type")

    def __mul__(self, mathEntity):
        """
        Performs multiplication with this entity on the left side of the
        multiplication operator and another mathematical entity on the
        right side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity being multiplied to
            this entity
        :return: The product of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        raise ArithmeticError("Left multiplication is not possible with this type")

    def __imul__(self, mathEntity):
        """
        Updates the value of this entity by performing multiplication with
        this entity on the left side of the multiplication operator and another
        mathematical entity on the right side. By default, this method
        raises an ArithmeticError

        :param mathEntity: The mathematical entity being multiplied to this
            entity
        :return: The product of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
             override the multiplication operator
        """

        return self * mathEntity

    def __rmul__(self, mathEntity):
        """
        Performs multiplication with this entity on the right side of the
        multiplication operator and another mathematical entity on the
        left side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity that this entity
            is being multiplied to
        :return: The product of the given entity and this entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        raise ArithmeticError("Right multiplication is not possible with this type")

    def __truediv__(self, mathEntity):
        """
        Performs division with this entity on the left side of the
        division operator and another mathematical entity on the
        right side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity being divided from
            this entity
        :return: The quotient of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        raise ArithmeticError("Left division is not possible with this type")

    def __itruediv__(self, mathEntity):
        """
        Updates the value of this entity by performing division with
        this entity on the left side of the division operator and another
        mathematical entity on the right side. By default, this method
        raises an ArithmeticError

        :param mathEntity: The mathematical entity being divided from this
            entity
        :return: The quotient of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
             override the division operator
        """

        return self / mathEntity

    def __rtruediv__(self, mathEntity):
        """
        Performs division with this entity on the right side of the
        division operator and another mathematical entity on the
        left side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity that this entity
            is being divided from
        :return: The quotient of the given entity and this entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        raise ArithmeticError("Right division is not possible with this type")

    def __floordiv__(self, mathEntity):
        """
        Performs floor division with this entity on the left side of the
        floor division operator and another mathematical entity on the
        right side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity being divided from
            this entity
        :return: The floor quotient of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
            override the division operator and the floor function
        """

        trueDiv = self / mathEntity
        floorDiv = floor(trueDiv)

        return floorDiv

    def __ifloordiv__(self, mathEntity):
        """
        Updates the value of this entity by performing floor division with
        this entity on the left side of the floor division operator and another
        mathematical entity on the right side. By default, this method
        raises an ArithmeticError

        :param mathEntity: The mathematical entity being floor divided from
            this entity
        :return: The floor quotient of this entity and the given entity
        :exception ArithmeticError: Raised if the subclass does not
            override the floor division operator
        """

        return self // mathEntity

    def __rfloordiv__(self, mathEntity):
        """
        Performs floor division with this entity on the right side of the
        floor division operator and another mathematical entity on the
        left side. By default, this method raises an ArithmeticError

        :param mathEntity: The mathematical entity that this entity
            is being floor divided from
        :return: The floor quotient of the given entity and this entity
        :exception ArithmeticError: Raised if the subclass does not
            override this method
        """

        trueDiv = mathEntity / self
        floorDiv = floor(trueDiv)

        return floorDiv

    def __eq__(self, mathEntity):
        """
        Checks if this mathematical entity is equal to
        another mathematical entity

        :param mathEntity: The entity that this entity is be compared
            to in order to check for equality
        :return: True if the two given mathematical entities are equal,
            false otherwise
        """

        raise NotImplementedError("This method must be implemented")

    def __ne__(self, mathEntity):
        """
        Checks if this mathematical entity is not equal to
        another mathematical entity

        :param mathEntity: The entity that this entity is be compared
            to in order to check for inequality
        :return: True if the two given mathematical entities are unequal,
            false otherwise
        """

        return not (self == mathEntity)

    def __repr__(self):
        """
        Returns a string for the Python shell. Returns the
        same string as the __str__ method

        :return: A string representation for the Python
            shell
        """

        return str(self)
