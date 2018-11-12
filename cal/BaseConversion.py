baseOfBinary = 2
baseOfHexadecimal = 16
baseOfOctal = 8
intToStrDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
strToIntDigits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                  "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def intToBinary(intValue):
    return _convertIntDecimal(intValue, baseOfBinary)


def intTpHexadecimal(intValue):
    return _convertIntDecimal(intValue, baseOfHexadecimal)


def intToOctal(intValue):
    return _convertIntDecimal(intValue, baseOfOctal)


def _convertIntDecimal(intValue, base):
    if intValue == 0:
        return "0"

    if intValue < 0:
        isNegative = True
        intValue = abs(intValue)
    else:
        isNegative = False

    strRep = ""

    while intValue > 1:
        index = intValue % base
        strRep += intToStrDigits[index]
        intValue /= base

    strRep = strRep[::-1]  # This code reverses the string

    if isNegative:
        strRep = "-" + strRep

    return strRep


def binaryToInt(binStr):
    return _convertStr(binStr, baseOfBinary)


def hexadecimalToInt(hexStr):
    return _convertStr(hexStr, baseOfHexadecimal)


def octalToInt(octStr):
    return _convertStr(octStr, baseOfOctal)


def _convertStr(strRep, base):
    if strRep.startswith("-"):
        isNegative = True
        strRep = strRep[1:]
    else:
        isNegative = False

    intValue = 0
    exponent = len(strRep) - 1

    for digit in strRep:
        intValue += int(strToIntDigits[digit]) * (base ** exponent)
        exponent -= 1

    if isNegative:
        intValue = -intValue

    return intValue
