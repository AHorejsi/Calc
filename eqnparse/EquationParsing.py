from eqnparse._VariableDictionary import _VariableDictionary
from eqnparse._FunctionDictionary import _FunctionDictionary


def parseMathEquation(equationString):
    varDict = _VariableDictionary.instance()
    funcDict = _FunctionDictionary.instance()
