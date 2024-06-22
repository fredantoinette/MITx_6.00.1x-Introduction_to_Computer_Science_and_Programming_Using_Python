def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    list_values = []
    values = aDict.values()
    for v1 in values:
        for v2 in v1:
            list_values.append(v2)
    return len(list_values)


# alternative

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    values = aDict.values()
    for v in values:
        result += len(v)
    return result


# test
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(how_many(animals))
