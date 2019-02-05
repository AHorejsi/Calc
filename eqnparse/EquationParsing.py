from eqnparse._VariableDictionary import _VariableDictionary
from eqnparse._FunctionDictionary import _FunctionDictionary
from calc import MathEntity
from typing import Union


def parseMathEquation(equationString: str) -> Union[int, float, bool, MathEntity, None]:
    varDict = _VariableDictionary.instance()
    funcDict = _FunctionDictionary.instance()

    return None
