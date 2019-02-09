from re import fullmatch, split
from calc import Complex, Quaternion, Vector, Matrix, MathEntity
from typing import Optional


def parseInt(valueString: str) -> Optional[int]:
    """
    Checks if the given string represents a valid int.
    If it does, returns the int value that it corresponds
    to. Otherwise returns None

    :param valueString: The string to be parsed to an int
    :return: The int value represented by the given string.
        If the string does not represent a valid int, returns
        None
    """

    if fullmatch("\s*(\-?\d+)\s*", valueString) is not None:
        return int(valueString)
    else:
        return None


def parseFloat(valueString: str) -> Optional[float]:
    """
    Checks if the given string represents a valid float.
    If it does, returns the float value that it corresponds
    to. Otherwise, returns None

    :param valueString: The string to be parsed to a float
    :return: The float value represented by the given string.
        If the string does not represent a valid float, returns
        None
    """

    if fullmatch("\s*((\-?\d+\.\d+)(e[\+|\-]?\d+)?)\s*", valueString) is not None:
        return float(valueString)
    else:
        return None


def parseComplex(valueString: str) -> Optional[Complex]:
    """
    Checks if the given string represents a valid Complex number.
    If it does, returns the Complex value that it corresponds to.
    Otherwise, returns None

    :param valueString: The string to be parsed to a Complex number
    :return: The Complex value represented by the given string.
        If the string does not represent a valid Complex number,
        returns None
    """

    if fullmatch("\s*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?i)\s*", valueString) is not None:
        strValue = valueString.replace("i", "j")
        builtInComplex = complex(strValue)

        return Complex.fromBuiltInComplex(builtInComplex)
    else:
        return None


def parseQuaternion(valueString: str) -> Optional[Quaternion]:
    """
    Checks if the given string represents a valid Quaternion.
    If it does, returns the Quaternion value that it corresponds
    to. Otherwise, returns None

    :param valueString: The string to be parsed to a Quaternion
    :return: The Quaternion value represented by the given string.
        If the string does not represent a valid Quaternion, returns
        None
    """

    if fullmatch("\s*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?i"
                 "[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?j[\+|\-](\d+(\.\d+)?)(e[\+|\-]?\d+)?k)\s*",
            valueString) is not None:
        nums = split("[ijk]", valueString)
        com = complex(nums[0] + "j")

        return Quaternion(com.real, com.imag, float(nums[1]), float(nums[2]))


def parseVector(valueString: str) -> Optional[Vector]:
    """
    Checks if the given string represents a valid Vector.
    If it does, returns the Vector value that it corresponds
    to. Otherwise, returns None

    :param valueString: The string to be parsed to a Vector
    :return: The Vector value represented by the given string.
        If the string does not represent a valid Vector, returns
        None
    """

    if fullmatch("\s*<((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?\s*\,\s*)*((\-?\d+(\.\d+)?)(e[\+|\-]?\d+)?)?>\s*", valueString) is not None:
        nums = split("\s*\,\s*", valueString[1 : len(valueString) - 1])
        listOfNums = []

        for numStr in nums:
            listOfNums.append(float(numStr.replace(" ", "")))

        return Vector(listOfNums)
    else:
        return None


def parseMatrix(valueString: str) -> Optional[Matrix]:
    """
    Checks if the given string represents a valid Matrix.
    If it does, returns the Matrix value that it corresponds
    to. Otherwise, returns None

    :param valueString: The string to be parsed to a Matrix
    :return: The Matrix value represented by the given string.
        If the string does not represent a valid Matrix, returns
        None
    """

    if fullmatch("\s*(\["
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
    """
    Checks if the given string represents a valid Bool.
    If it does, returns the Bool value that it corresponds
    to. Otherwise, returns None

    :param valueString: The string to be parsed to a Bool
    :return: The Bool value that is represented by the
        given string. If the string does not represent a
        valid Bool, returns None
    """

    if fullmatch("\s*[t|T][r|R][u|U][e|E]\s*", valueString) is not None:
        return True
    elif fullmatch("\s*[f|F][a|A][l|L][s|S][e|E]\s*", valueString) is not None:
        return False
    else:
        return None


def parseVariableValue(valueString: str) -> Optional[MathEntity, int, float, bool]:
    """
    Checks if the given string represents a valid
    mathematical entity. If it does, returns the
    given mathematical entity with the given value
    represented by the string. If it does not, returns
    None

    :param valueString: The string to be parsed into
        a mathematical entity
    :return: Returns the mathematical entity represented
        by the given string
    """

    for func in [parseInt, parseFloat, parseComplex, parseQuaternion, parseVector, parseMatrix, parseBool]:
        value = func(valueString)

        if value is not None:
            return value

    return None
