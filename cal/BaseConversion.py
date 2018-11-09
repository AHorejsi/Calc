def intToBinary(intValue):
    if intValue < 0:
        isNegative = True
        intValue = abs(intValue)
    else:
        isNegative = False

    binStr = _convertIntToString(intValue, 2)

    return binStr


def floatToBinary(floatValue):
    pass


def intToHexadecimal(intValue):
    if intValue < 0:
        isNegative = True
        intValue = abs(intValue)
    else:
        isNegative = False

    hexStr = _convertIntToString(intValue, 16)

    return hexStr


def floatToHexadecimal(floatValue):
    pass


def intToOctal(intValue):
    if intValue < 0:
        isNegative = True
        intValue = abs(intValue)
    else:
        isNegative = False

    octStr = _convertIntToString(intValue, 8)

    return octStr


def floatToOctal(floatValue):
    pass


def _convertIntToString(intValue, base):
    digits = "0123456789ABCDEF"
    result = ""

    while intValue > 1:
        index = int(intValue % base)
        result += digits[index]
        intValue /= base

    return result[::-1]  # This code reverses the string
