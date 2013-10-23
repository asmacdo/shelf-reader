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
        if LEGAL_CHARS.match(value) is None:
            raise ValueError('you suck')

    def __cmp__(self, other):
        # if I am a float
        if set(self.value) & set(string.digits):
            # if other is a float
            if set(other.value) & set(string.digits):
                return cmp(float(self.value), float(other.value))

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
