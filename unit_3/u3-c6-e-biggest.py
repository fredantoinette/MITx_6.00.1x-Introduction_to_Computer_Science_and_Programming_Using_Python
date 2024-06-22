def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    max_value = 0
    keys = aDict.keys()
    result = None
    for key in keys:
        if len(aDict[key]) >= max_value:
            max_value = len(aDict[key])
            result = key
    return result

# test
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))
