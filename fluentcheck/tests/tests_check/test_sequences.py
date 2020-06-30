import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestSequencesAssertions(unittest.TestCase):
    def test_is_empty(self):
        res = Check('').is_empty()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_empty()
            self.fail()
        except CheckError:
            pass

    def test_is_not_empty(self):
        res = Check('123').is_not_empty()
        self.assertIsInstance(res, Check)
        try:
            Check([]).is_not_empty()
            self.fail()
        except CheckError:
            pass

    def test_is_iterable(self):
        res = Check(range(6)).is_iterable()
        self.assertIsInstance(res, Check)
        try:
            Check(8).is_iterable()
            self.fail()
        except CheckError:
            pass
