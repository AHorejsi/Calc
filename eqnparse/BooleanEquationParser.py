from eqnparse.EquationParser import EquationParser


class BooleanEquationParser(EquationParser):
    __instance = None

    @staticmethod
    def getInstance():
        if BooleanEquationParser.__instance is None:
            return BooleanEquationParser()
        else:
            return BooleanEquationParser.__instance

    def __init__(self):
        if BooleanEquationParser.__instance is None:
            BooleanEquationParser.__instance = self
        else:
            raise Exception("This is a singleton class")
