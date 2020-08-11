def is_armstrong_number(number):
    """An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    Args:
        number (int): any integer

    Returns:
        boolean: returns if a number is an armstrong number
    """
    exp = len(str(number))

    return sum((int(digit)**exp for digit in str(number))) == number
