import unittest

from fluentcheck import Is
from fluentcheck.exceptions import CheckError


# noinspection PyStatementEffect
class TestIsDictsAssertions(unittest.TestCase):

    def test_is_dict_pass(self):
        obj = {}
        self.assertIsInstance(Is(obj).dict, Is)

    def test_is_dict_fail(self):
        obj = set()
        with self.assertRaises(CheckError):
            Is(obj).dict

    def test_is_not_dict_pass(self):
        obj = set()
        self.assertIsInstance(Is(obj).not_dict, Is)

    def test_is_not_dict_fail(self):
        obj = {}
        with self.assertRaises(CheckError):
            Is(obj).not_dict

    def test_is_has_keys_pass(self):
        obj = {1: 'one', 2: 'two'}
        self.assertIsInstance(Is(obj).has_keys(*obj.keys()), Is)

    def test_is_has_keys_fail(self):
        obj = {1: 'one', 2: 'two'}
        with self.assertRaises(CheckError):
            Is(obj).has_keys(1, 3)

    def test_is_has_not_keys_pass(self):
        obj = {1: 'one', 2: 'two'}
        self.assertIsInstance(Is(obj).has_not_keys(7, 3), Is)

    def test_is_has_not_keys_fail(self):
        obj = {1: 'one', 2: 'two'}
        with self.assertRaises(CheckError):
            Is(obj).has_not_keys(*obj.keys())
