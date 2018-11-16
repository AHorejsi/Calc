from eqnparse.EquationParser import EquationParser


class MathEquationParser(EquationParser):
    __instance = None

    @staticmethod
    def getInstance():
        if MathEquationParser.__instance is None:
            return MathEquationParser()
        else:
            return MathEquationParser.__instance

    def __init__(self):
        if MathEquationParser.__instance is None:
            MathEquationParser.__instance = self
            self.variableList = {}
        else:
            raise Exception("This is a singleton class")
