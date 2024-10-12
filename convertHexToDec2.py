# Python code​​​​​​‌​‌‌‌‌‌​‌‌​‌​‌​​‌‌​​​‌​‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
  
    for item in hexNum:
        if item not in hexNumbers:
            return None

    exponent = len(hexNum) - 1
    dec = 0
    for item in hexNum:
        dec = dec + hexNumbers[item] * (16 ** exponent)
        exponent = exponent - 1

    return dec