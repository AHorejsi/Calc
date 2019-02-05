from re import fullmatch, split
from calc import Complex, Quaternion, Vector, Matrix


def parseInt(valueString):
    if fullmatch("\s*(\-?\d+)\s*", valueString) is not None:
        return int(valueString)
    else:
        return None


def parseFloat(valueString):
    if fullmatch("\s*((\-?\d+\.\d+)(e[\+|\-]?\d+)?)\s*", valueString) is not None:
        return float(valueString)
    else:
        return None


def parseComplex(valueString):
    if fullmatch("\s*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?i)\s*", valueString) is not None:
        strValue = valueString.replace("i", "j")
        builtInComplex = complex(strValue)

        return Complex.fromBuiltInComplex(builtInComplex)
    else:
        return None


def parseQuaternion(valueString):
    if fullmatch(
            "\s*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?i[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?j[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?k)\s*",
            valueString) is not None:
        nums = split("[ijk]", valueString)
        com = complex(nums[0] + "j")

        return Quaternion(com.real, com.imag, float(nums[1]), float(nums[2]))


def parseVector(valueString):
    if fullmatch("\s*(<((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?\s*\,\s*)*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?)?>)\s*", valueString) is not None:
        nums = split(",", valueString[1 : len(valueString) - 1])
        listOfNums = []

        for numStr in nums:
            listOfNums.append(float(numStr.replace(" ", "")))

        return Vector(listOfNums)
    else:
        return None


def parseMatrix(valueString):
    if fullmatch(
    "\s*(\["
    "(\["
    "((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?i)"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?j)([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?k)))?)?"
    "\s*\,\s*)*"
    "((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?i)"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?j)([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?k)))?)?)?"
    "\]\s*\,\s*)*"
    "(\["
    "((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?i)"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?j)([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?k)))?)?"
    "\s*\,\s*)*"
    "((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?i)"
    "([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?j)([\+|\-]((\d+(\.\d+)?)(e[\+|\-]?\d+)?k)))?)?)?"
    "\])?\])\s*", valueString) is not None:
        rows = list(filter(lambda string: string != "", split("\[\[|\]\]|\]\s*\,\s*\[", valueString)))
        table = []

        for row in rows:
            newRow = []
            listOfNums = split("\s*\,\s*", row)

            for numStr in listOfNums:
                for func in [parseInt, parseFloat, parseComplex, parseQuaternion]:
                    value = func(numStr)

                    if value is not None:
                        newRow.append(value)

            table.append(newRow)

        return Matrix(table)
    else:
        return None


def parseBool(valueString):
    if fullmatch("[t|T][r|R][u|U][e|E]", valueString) is not None:
        return True
    elif fullmatch("[f|F][a|A][l|L][s|S][e|E]", valueString) is not None:
        return False
    else:
        return None


def parseVariableValue(valueString):
    for func in [parseInt, parseFloat, parseComplex, parseQuaternion, parseVector, parseMatrix, parseBool]:
        value = func(valueString)

        if value is not None:
            return value

    return None
