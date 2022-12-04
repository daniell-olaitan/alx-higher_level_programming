#!/usr/bin/python3
def multiple_returns(sentence):
    """Gets a tuple of sentence length and its first character

    Args:
        sentence: the given string

    Returns:
        the tuple of sentence length and its first character
    """
    str_len = len(sentence)
    if str_len == 0:
        return 0, None

    return str_len, sentence[0]
