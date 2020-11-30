import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestDictsAssertions(unittest.TestCase):

    def test_is_dict(self):
        res = Check({}).is_dict()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_dict()
            self.fail()
        except CheckError:
            pass

    def test_is_not_dict(self):
        res = Check(set()).is_not_dict()
        self.assertIsInstance(res, Check)
        try:
            Check({}).is_not_dict()
            self.fail()
        except CheckError:
            pass

    def test_has_keys(self):
        d = { 1: 'one', 2: 'two'}
        res = Check(d).has_keys(1,2)
        self.assertIsInstance(res, Check)
        try:
            Check(d).has_keys(3,4)
            self.fail()
        except CheckError:
            pass

    def test_has_not_keys(self):
        d = { 1: 'one', 2: 'two'}
        res = Check(d).has_not_keys(3,4)
        self.assertIsInstance(res, Check)
        try:
            Check(d).has_not_keys(1,2)
            self.fail()
        except CheckError:
            pass

    