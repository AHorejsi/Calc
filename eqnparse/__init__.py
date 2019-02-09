from eqnparse.ValueParsing import parseInt, parseFloat, parseComplex, parseQuaternion, parseVector, parseMatrix, \
                                  parseBool, parseVariableValue
from eqnparse.EquationParsing import parseMathEquation
from eqnparse._VariableDictionary import _VariableDictionary

for val in _VariableDictionary.instance().iterUniversalVars():
    print(val)