# -*- coding: utf-8 -*-

import re
from .mixins import ComparableMixin 
from .utils import check_type, isfloat



# probably needs improvement
LEGAL_CHARS = re.compile('^[a-zA-Z0-9 \.]+$')


class Token(ComparableMixin):
    """
    A part of a call number. A token can be either a decimal number or
    a string of letters.
    """
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

    def _cmpkey(self):
        """Return the key used for comparison"""
        if isfloat(self.value):
            return self.value
        return self.value.lower()

    def __str__(self):
        return self.value


class CallNumber(ComparableMixin):
    """ Call number is a collection of independent tokens.
    """

    def __init__(self, value):
        self._validate(value)
        self.value = value

    @staticmethod
    def _validate(value):
        """
        Ensures that a candidate call number contains only valid characters
        and is the appropriate length

        :param value: string representation of a call number
        """
        if len(value) < 2:
            raise ValueError("Call numbers must be at least two characters")

        if LEGAL_CHARS.match(value) is None:
            raise ValueError('Contains illegal characters')

    @property
    def tokens(self):
        """
        Breaks a call number into tokens, which are its atomic parts. A token
        will contain either letters or a number but not both.

        :return: a list of Token objects
        """
        tokens_list = []
        new_token = self.value[0]

        for i in range(len(self.value) - 1):
            c = self.value[i]
            d = self.value[i + 1]

            # d is part of token
            if check_type(c) == check_type(d):
                new_token += d

            # d is the beginning of a new token
            else:
                # Prevents adding a space as a token
                if check_type(new_token) != 2:
                    tokens_list.append(Token(new_token))

                if (check_type(c) == 0) and (check_type(d) == 1) and (i > 1):
                    """
                    In call number sorting rules, the first number should be
                    treated as a whole number and all following numbers should
                    be treated as decimals.

                    For example, M101 K78 would be M, 101, K, 0.78
                    """

                    d = '0.' + d

                new_token = d

        tokens_list.append(Token(new_token))
        return tokens_list

    def _cmpkey(self):
        """Return the key used for comparison"""
        return self.tokens


    def __str__(self):
        return str([str(token) for token in self.tokens])
