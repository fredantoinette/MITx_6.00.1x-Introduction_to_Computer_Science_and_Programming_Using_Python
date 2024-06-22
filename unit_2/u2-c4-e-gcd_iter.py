def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = min(a, b)
    while a % divisor != 0 or b % divisor != 0:
        divisor -= 1
    return divisor