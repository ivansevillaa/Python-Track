def two_fer(name="you"):
    '''
    Returns the string 'One for X, one for me.' Where X is the given name.
    If the name is missing, returns the string 'One for you, one for me.'

    Parameters:
        name (str): Any string

    Returns:
        (str): 'One for X, one for me.'
    '''
    return f'One for {name}, one for me.'


two_fer()
