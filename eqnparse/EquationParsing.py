from eqnparse._VariableDictionary import _VariableDictionary
from re import fullmatch, split
from calc import Complex, Quaternion, Vector, Matrix


def parseMath(equation):
    pass


def parseBoolean(equation):
    pass

def parseVariableValue(strValue):
    if fullmatch("(-?\d+.?\d+)(e[-]?\d+)?[+|-](\d+.?\d+)(e[-]?\d+)?i", strValue) is not None:
        # Type is Complex
        strValue = strValue.replace("i", "j")
        builtInComplex = complex(strValue)

        return Complex.fromBuiltInComplex(builtInComplex)
    elif fullmatch("(-?\d+.?\d+)(e[-]?\d+)?[+|-](\d+.?\d+)(e[-]?\d+)?i[+|-](\d+.?\d+)(e[-]?\d+)?j[+|-](\d+.?\d+)(e[-]?\d+)?k",
            strValue) is not None:
        # Type is Quaternion

        nums = split("[ijk]", str)
        com = complex(nums[0] + "j")

        return Quaternion(com.real, com.imag, float(nums[1]), float(nums[2]))
    elif fullmatch("<((-?\d+.?\d+)(e[-]?\d+)?\s*,\s*)*((-?\d+.?\d+)(e[-]?\d+)?)?>", strValue) is not None:
        # Type is Vector

        nums = split(",", strValue[1: len(strValue) - 1])
        listOfNums = []

        for numStr in nums:
            listOfNums.append(float(numStr))

        return Vector(listOfNums)

    elif fullmatch("", strValue) is not None:
        # Type is Matrix

        rows = list(filter(lambda string: string != "", split("\[\[|\]\]|\],\[", strValue)))
        table = []

        for row in rows:
            newRow = []
            listOfNums = split(",", row)

            for numStr in listOfNums:
                newRow.append(float(numStr))

            table.append(newRow)

        return Matrix(table)

    return None
