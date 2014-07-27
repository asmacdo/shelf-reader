from unittest import TestCase

from shelf_reader.models import CallNumber


class TestValidate(TestCase):

    def test_length(self):
        self.assertRaises(ValueError, CallNumber, "M")
        CallNumber("M1")

    def test_invalid_chars(self):
        self.assertRaises(ValueError, CallNumber, "M_V")

    def test_loc(self):
        CallNumber('M1624.8 L36N6')

    def test_dewey(self):
        CallNumber('001.209 K632')


class TestTokens(TestCase):

    def test_loc(self):
        call_num = CallNumber('M1624.8 L36N6')
        self.assertTrue(str(call_num) == "['M', '1624.8', 'L', '0.36', 'N', '0.6']")

    def test_dewey(self):
        call_num = CallNumber('001.209 K632')
        self.assertTrue(str(call_num) == "['001.209', 'K', '0.632']")


class TestCMP(TestCase):

    def test_loc(self):
        call_a = CallNumber('M1624.8 L37B4')
        call_b = CallNumber('M1624.8 L45S6')
        self.assertTrue(call_a < call_b)
