class MathEntity:
    def __add__(self, entity):
        from cal.Operations import addition

        return addition(self, entity)

    def __iadd__(self, entity):
        return self + entity

    def __radd__(self, entity):
        from cal.Operations import addition

        return addition(entity, self)

    def __sub__(self, entity):
        from cal.Operations import subtraction

        return subtraction(self, entity)

    def __isub__(self, entity):
        return self - entity

    def __rsub__(self, entity):
        from cal.Operations import subtraction

        return subtraction(entity, self)

    def __mul__(self, entity):
        from cal.Operations import multiplication

        return multiplication(self, entity)

    def __imul__(self, entity):
        return self * entity

    def __rmul__(self, entity):
        from cal.Operations import multiplication

        return multiplication(entity, self)

    def __truediv__(self, entity):
        from cal.Operations import division

        return division(self, entity)

    def __itruediv__(self, entity):
        return self / entity

    def __rtruediv__(self, entity):
        from cal.Operations import division

        return division(entity, self)

    def __neg__(self):
        from cal.Operations import negation

        return negation(self)

    def __eq__(self, entity):
        from cal.Operations import equality

        return equality(self, entity)

    def __ne__(self, entity):
        from cal.Operations import inequality

        return inequality(self, entity)
