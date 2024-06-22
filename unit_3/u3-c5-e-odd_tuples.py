def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new = ()
    for i in range(len(aTup)):
        if (i + 1) % 2 == 1:
            new = new + (aTup[i],)
    return new


# alternative

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[::2]
