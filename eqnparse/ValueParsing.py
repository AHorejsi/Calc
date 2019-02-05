from re import fullmatch, split
from calc import Complex, Quaternion, Vector, Matrix, MathEntity
from typing import Optional


def parseInt(valueString: str) -> Optional[int]:
    if fullmatch("\s*(\-?\d+)\s*", valueString) is not None:
        return int(valueString)
    else:
        return None


def parseFloat(valueString: str) -> Optional[float]:
    if fullmatch("\s*((\-?\d+\.\d+)(e[\+|\-]?\d+)?)\s*", valueString) is not None:
        return float(valueString)
    else:
        return None


def parseComplex(valueString: str) -> Optional[Complex]:
    if fullmatch("\s*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?i)\s*", valueString) is not None:
        strValue = valueString.replace("i", "j")
        builtInComplex = complex(strValue)

        return Complex.fromBuiltInComplex(builtInComplex)
    else:
        return None


def parseQuaternion(valueString: str) -> Optional[Quaternion]:
    if fullmatch(
            "\s*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?i[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?j[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?k)\s*",
            valueString) is not None:
        nums = split("[ijk]", valueString)
        com = complex(nums[0] + "j")

        return Quaternion(com.real, com.imag, float(nums[1]), float(nums[2]))


def parseVector(valueString: str) -> Optional[Vector]:
    if fullmatch("\s*(<((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?\s*\,\s*)*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?)?>)\s*", valueString) is not None:
        nums = split(",", valueString[1 : len(valueString) - 1])
        listOfNums = []

        for numStr in nums:
            listOfNums.append(float(numStr.replace(" ", "")))

        return Vector(listOfNums)
    else:
        return None


def parseMatrix(valueString: str) -> Optional[Matrix]:
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


def parseBool(valueString: str) -> Optional[bool]:
    if fullmatch("[t|T][r|R][u|U][e|E]", valueString) is not None:
        return True
    elif fullmatch("[f|F][a|A][l|L][s|S][e|E]", valueString) is not None:
        return False
    else:
        return None


def parseVariableValue(valueString: str) -> Optional[MathEntity]:
    for func in [parseInt, parseFloat, parseComplex, parseQuaternion, parseVector, parseMatrix, parseBool]:
        value = func(valueString)

        if value is not None:
            return value

    return None
