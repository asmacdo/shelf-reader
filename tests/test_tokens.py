import unittest

import models


class TestValidate(unittest.TestCase):
    def test_invalid_chars(self):
        self.assertRaises(ValueError, models.Token, '_')

    def test_float(self):
        models.Token('1.2')


class TestCmp(unittest.TestCase):
    def test_both_letters(self):
        a = models.Token('abcd')
        b = models.Token('xyz')

        self.assertTrue(a < b)
        self.assertTrue(b > a)

    def test_both_floats(self):
        a = models.Token('1.2')
        b = models.Token('2.3')

        self.assertTrue(a < b)
        self.assertTrue(b > a)
