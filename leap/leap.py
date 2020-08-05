def leap_year(year):
    '''
    Returns if it is a leap year.

    Parameters:
        year (int): Any integer

    Returns:
        (boolean): If the year is leap returns True else returns False
    '''
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True

            return False

        return True

    return False
