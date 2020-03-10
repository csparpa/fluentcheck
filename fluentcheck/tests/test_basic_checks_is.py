import unittest
from fluentcheck import Is
from fluentcheck.exceptions import CheckError


# noinspection PyStatementEffect
class TestIsBasicChecks(unittest.TestCase):

    def test_is_none_pass(self):
        obj = None
        self.assertIsInstance(Is(obj).none, Is)

    def test_is_none_fail(self):
        obj = "I am not none"
        with self.assertRaises(CheckError):
            Is(obj).none

    def test_is_not_none_pass(self):
        obj = "I am not none"
        self.assertIsInstance(Is(obj).not_none, Is)

    def test_is_not_none_fail(self):
        obj = None
        with self.assertRaises(CheckError):
            Is(obj).not_none
