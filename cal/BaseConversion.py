baseOfBinary = 2
baseOfHexadecimal = 16
baseOfOctal = 8
intToStrDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
strToIntDigits = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9,
                  "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}


def intToBinary(intValue):
    if intValue < 0:
        isNegative = True
        intValue = abs(intValue)
    else:
        isNegative = False

    binStr = _convertIntDecimal(intValue, baseOfBinary)

    if isNegative:
        binStr = "-" + binStr

    return binStr


def intTpHexadecimal(intValue):
    if intValue < 0:
        isNegative = True
        intValue = abs(intValue)
    else:
        isNegative = False

    hexStr = _convertIntDecimal(intValue, baseOfHexadecimal)

    if isNegative:
        hexStr = "-" + hexStr

    return hexStr


def intToOctal(intValue):
    if intValue < 0:
        isNegative = True
        intValue = abs(intValue)
    else:
        isNegative = False

    octStr = _convertIntDecimal(intValue, baseOfOctal)

    if isNegative:
        octStr = "-" + octStr

    return octStr


def _convertIntDecimal(intValue, base):
    if intValue == 0:
        return "0"

    strRep = ""

    while intValue > 1:
        index = intValue % base
        strRep += intToStrDigits[index]
        intValue /= base

    return strRep[::-1]  # This code reverses the string


def binaryToInt(binStr):
    if binStr.startswith("-"):
        isNegative = True
        binStr = binStr[1:]
    else:
        isNegative = False

    intValue = _convertStr(binStr, baseOfBinary)

    if isNegative:
        intValue = -intValue

    return intValue


def hexadecimalToInt(hexStr):
    if hexStr.startswith("-"):
        isNegative = True
        hexStr = hexStr[1:]
    else:
        isNegative = False

    intValue = _convertStr(hexStr, baseOfHexadecimal)

    if isNegative:
        intValue = -intValue

    return intValue


def octalToInt(octStr):
    if octStr.startswith("-"):
        isNegative = True
        octStr = octStr[1:]
    else:
        isNegative = False

    intValue = _convertStr(octStr, baseOfOctal)

    if isNegative:
        intValue = -intValue

    return intValue


def _convertStr(strRep, base):
    intValue = 0
    exponent = len(strRep) - 1

    for digit in strRep:
        intValue += int(strToIntDigits[digit]) * (base ** exponent)
        exponent -= 1

    return intValue
