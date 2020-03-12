import unittest
from fluentcheck import Is
from fluentcheck.exceptions import CheckError


# noinspection PyStatementEffect
class TestIsBasicChecks(unittest.TestCase):

    def test_is_none_pass(self):
        self.assertIsInstance(Is(None).none, Is)

    def test_is_none_fail(self):
        with self.assertRaises(CheckError):
            Is("I am not none").none

    def test_is_not_none_pass(self):
        self.assertIsInstance(Is("I am not none").not_none, Is)

    def test_is_not_none_fail(self):
        with self.assertRaises(CheckError):
            Is(None).not_none
