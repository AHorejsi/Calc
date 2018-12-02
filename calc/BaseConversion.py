baseOfBinary = 2
baseOfHexadecimal = 16
baseOfOctal = 8
intToStrDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
strToIntDigits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                  "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def intToBinary(intValue):
    """
    Computes the binary representation of the given int value

    :param intValue: The int value whose binary representation
        is desired
    :return: A string representation of the binary representation
        of the given int value
    """

    return _convertIntDecimal(intValue, baseOfBinary)


def intToHexadecimal(intValue):
    """
    Computes the hexadecimal representation of the given int value

    :param intValue: The int value whose hexadecimal value
        is desired
    :return: A string representation of the hexadecimal representation
        of the given int value
    """

    return _convertIntDecimal(intValue, baseOfHexadecimal)


def intToOctal(intValue):
    """
    Computes the octal representation of the given int value

    :param intValue: The int value whose octal value
        is desired
    :return: A string representation of the octal representation
        of the given int value
    """

    return _convertIntDecimal(intValue, baseOfOctal)


def _convertIntDecimal(intValue, base):
    """
    Computes the given int value to its representation of its
    with the given base

    :param intValue: The int value whose representation in another
        base system is to be computed
    :param base: The base the given int value is to be converted to
    :return: A string representation of the given int value to its
        representation in the given base system
    """

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
    """
    Computes the decimal representation of the given binary number

    :param binStr: A string representing a binary number
    :return: An int value equal to the given binary number
    """

    return _convertStr(binStr, baseOfBinary)


def hexadecimalToInt(hexStr):
    """
    Computes the decimal representation of the given hexadecimal
    number

    :param hexStr: A string representing a hexadecimal number
    :return: An int value equal to the given hexadecimal number
    """

    return _convertStr(hexStr, baseOfHexadecimal)


def octalToInt(octStr):
    """
    Computes the decimal representation of the given octal number

    :param octStr: A string representing an octal number
    :return: An int value equal to the given octal number
    """

    return _convertStr(octStr, baseOfOctal)


def _convertStr(strRep, base):
    """
    Computes the decimal representation of the given number

    :param strRep: A string representing the number to be converted
    :param base: The base of the number represented by "strRep"
    :return: An int value equal to the given number
    """

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