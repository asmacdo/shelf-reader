from unittest import TestCase

from shelf_reader.models import Token


class TestValidate(TestCase):

    def test_invalid_chars(self):
        self.assertRaises(ValueError, Token, '_')

    def test_alphanum(self):
        self.assertRaises(ValueError, Token, '2.2R')

    def test_float(self):
        Token('1.2')

    def test_alpha(self):
        Token('WORD')


class TestCmp(TestCase):
    def test_both_letters(self):
        a = Token('abcd')
        b = Token('xyz')
        self.assertTrue(a < b)
        self.assertFalse(b < a)

    def test_integers(self):
        a = Token('1')
        b = Token('2')
        self.assertTrue(a < b)

    def test_both_floats(self):
        a = Token('1.2')
        b = Token('2.3')
        self.assertTrue(a < b)

    def test_float_letters(self):
        a = Token('a')
        b = Token('2.2')
        self.assertTrue(a > b)
        self.assertFalse(a < b)

    def test_capital_agnostic(self):
        a = Token('a')
        b = Token('A')
        self.assertTrue(a <= b)
        self.assertFalse(a > b)

