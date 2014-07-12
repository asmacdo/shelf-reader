def check_type(value):
    """
    Checks the type of character of the input.

    :param c:   character to check

    :returns:    0 if letter, 2 if space, or 1 if number
    """

    if value.isalpha():
        return 0  # letter
    elif value.isspace():
        return 2  # space
    else:
        return 1  # number


def isfloat(value):
    """

    :param value:
    :return:
    """
    try:
        float(value)
        return True
    except ValueError:
        return False