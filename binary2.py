"""Return binary value from int value."""


def getBit(x: int):
    """Returns bit value from integer."""
    bin: str = ""
    if x % 2 != 0:
        bin = "1"
    else:
        bin = "0"
    return bin


def getList(x: int):
    """Returns new list of integers divided by 2."""
    newList = []
    while x >= 1:
        newList.append(x)
        x = x // 2
    newList.reverse()
    return newList

def binaryList(numList):
    """Returns binary list from list returned from getList function."""
    binary: str = ""
    for x in numList:
        binary += getBit(x) 
    return binary
       

print(binaryList(getList(int(input("Enter a number: ")))))