class MathEntity:
    def __add__(self, mathEntity):
        raise ArithmeticError("Left addition is not possible with this type")

    def __iadd__(self, mathEntity):
        return self + mathEntity

    def __radd__(self, mathEntity):
        raise ArithmeticError("Right addition is not possible with this type")

    def __sub__(self, mathEntity):
        raise ArithmeticError("Left subtraction is not possible with this type")

    def __isub__(self, mathEntity):
        return self - mathEntity

    def __rsub__(self, mathEntity):
        raise ArithmeticError("Right subtraction is not possible with this type")

    def __mul__(self, mathEntity):
        raise ArithmeticError("Left multiplication is not possible with this type")

    def __imul__(self, mathEntity):
        return self * mathEntity

    def __rmul__(self, mathEntity):
        raise ArithmeticError("Right multiplication is not possible with this type")

    def __truediv__(self, mathEntity):
        raise ArithmeticError("Left division is not possible with this type")

    def __itruediv__(self, mathEntity):
        return self / mathEntity

    def __rtruediv__(self, mathEntity):
        raise ArithmeticError("Right division is not possible with this type")

    def __eq__(self, mathEntity):
        raise NotImplementedError("This method must be implemented")

    def __ne__(self, mathEntity):
        return not (self == mathEntity)
