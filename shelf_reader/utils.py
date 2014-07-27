# -*- coding: utf-8 -*-

def check_type(value):
    """
    Checks the type of character of the input.

    :param value:   character to check

    :returns:    0 if letter, 2 if space, or 1 if number
    """

    if value.isalpha():
        return 0
    elif value.isspace():
        return 2
    else:
        return 1  # number


def isfloat(value):
    """
    Determines whether the value is a float
    """
    try:
        float(value)
        return True
    except ValueError:
        return False