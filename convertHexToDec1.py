# Python code​​​​​​‌​‌‌‌‌‌​‌‌​‌​‌​​‌‌​​​‌​‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):

    if len(hexNum) > 3: 
        return None
    
    for item in hexNum:
        if item not in hexNumbers:
            return None
    
    if len(hexNum) == 3:
        return (hexNumbers[hexNum[0]]*256)+(hexNumbers[hexNum[1]]*16)+(hexNumbers[hexNum[2]]*1)
    if len(hexNum) == 2:
        return (hexNumbers[hexNum[0]]*16)+(hexNumbers[hexNum[1]]*1)
    if len(hexNum) == 1:
        return (hexNumbers[hexNum[0]]*1)