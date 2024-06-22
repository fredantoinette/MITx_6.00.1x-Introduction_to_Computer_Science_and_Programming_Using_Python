def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    mid = len(aStr) // 2
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
    elif aStr[mid] == char:
        return True
    else:
        if aStr[mid] < char:
            return isIn(char, aStr[(mid + 1) :])
        else:
            return isIn(char, aStr[: mid])
