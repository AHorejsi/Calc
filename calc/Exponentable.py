class Exponentable:
    def __pow__(self, power, modulo=None):
        raise NotImplementedError("This method must be implemented")

    def __ipow__(self, mathEntity):
        return self ** mathEntity

    def __rpow__(self, mathEntity):
        raise NotImplementedError("This method must be implemented")
