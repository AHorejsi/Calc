from eqnparse._VariableDictionary import _VariableDictionary
from eqnparse._FunctionDictionary import _FunctionDictionary
from calc import MathEntity
from typing import Union, Optional


def parseEquation(equationString: str) -> Optional[Union[int, float, bool, MathEntity]]:
    varDict = _VariableDictionary.instance()
    funcDict = _FunctionDictionary.instance()
