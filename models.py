import re
import string


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

        try:
            float(value)
        except ValueError:
            if not value.isalpha():
                raise ValueError('Token contains letters and numbers')

    def __cmp__(self, other):
        # case insensitive for alpha chars
        if self.value.isalpha() and other.value.isalpha():
            return cmp(self.value.lower(), other.value.lower())

        # for all cases involving letters, this will suffice
        return cmp(self.value, other.value)


class CallNumber(object):
    def __init__(self, value):
        self.value = value

    @property
    def tokens(self):
        # TODO: add sophisticated logic here to figure out how to create some
        # tokens!
        pass

    def __cmp__(self, other):
        return cmp(self.tokens, other.tokens)
        

if __name__ == '__main__':
    pass
    # do stuff here like get user input and tell them how cool their situation is
