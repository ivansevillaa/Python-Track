def convert(number):
    """Convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
        The rules of raindrops are that if a given number:
            has 3 as a factor, add 'Pling' to the result.
            has 5 as a factor, add 'Plang' to the result.
            has 7 as a factor, add 'Plong' to the result.
            does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

    Args:
        number (int): any integer

    Returns:
        (str): raindrop sounds or the number given
    """
    raindrops = ""

    if number % 3 == 0:
        raindrops += "Pling"

    if number % 5 == 0:
        raindrops += "Plang"

    if number % 7 == 0:
        raindrops += "Plong"

    return raindrops or str(number)
