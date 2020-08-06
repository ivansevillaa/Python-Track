from string import ascii_lowercase


def is_pangram(sentence):
    '''
    Returns if a sentence is a pangram(sentence using every letter of the alphabet at least once).

    Parameters:
        sentence (str): Any string

    Returns:
        (boolean): If the sentence is a pangram returns True else returns False
    '''
    alphabet_set = set(ascii_lowercase)
    sentence_set = set(sentence.lower())

    return alphabet_set.issubset(sentence_set)
