import re
import string
from utils import check_type, isfloat


# probably needs improvement
LEGAL_CHARS = re.compile('^[a-zA-Z0-9 \.]+$')


class Token(object):
    def __init__(self, value):
        self._validate(value)
        self.value = value

    @staticmethod
    def _validate(value):
        """
        Ensures that a candidate token contains only valid characters and that
        a single token contains only letters or only numbers
        :param value: string that will be the value of the token
        """
        if LEGAL_CHARS.match(value) is None:
            raise ValueError('Contains illegal characters')

        # Must either be a float or alpha chars
        if not isfloat(value) and not value.isalpha():
            raise ValueError('Token contains letters and numbers')

    def __cmp__(self, other):
        # case insensitive for alpha chars
        if self.value.isalpha() and other.value.isalpha():
            return cmp(self.value.lower(), other.value.lower())

        # for all cases involving letters, this will suffice
        return cmp(self.value, other.value)

    def __repr__(self):
        return self.value


class CallNumber(object):
    def __init__(self, value):
        self._validate(value)
        self.value = value

    @staticmethod
    def _validate(value):
        if len(value) < 2:
            raise ValueError("Call numbers must be at least two characters")

        if LEGAL_CHARS.match(value) is None:
            raise ValueError('Contains illegal characters')

    @property
    def tokens(self):
        tokens_list = []
        new_token = self.value[0]

        for i in range(len(self.value) - 1):
            c = self.value[i]
            d = self.value[i + 1]
            if check_type(c) == check_type(d):  # d should be added to part of previous token
                new_token += d
            else:
                if check_type(new_token) != 2:  # Prevents adding a space as a token
                    tokens_list.append(Token(new_token))  # Adds completed token to the list

                if (check_type(c) == 0) and (check_type(d) == 1) and (i > 1):
                    """
                    Numbers following a letter other than the first letter are
                    treated as decimals
                    """

                    d = '0.' + d

                new_token = d

        tokens_list.append(Token(new_token))
        return tokens_list

    def __cmp__(self, other):
        return cmp(self.tokens, other.tokens)

    def __repr__(self):
        return [token.__repr__() for token in self.tokens]


if __name__ == '__main__':
    pass
    # do stuff here like get user input and tell them how cool their situation is
