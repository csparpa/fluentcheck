import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestBasicChecks(unittest.TestCase):

    def test_is_none(self):
        res = Check(None).is_none()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_none()
            self.fail()
        except CheckError:
            pass

    def test_is_not_none(self):
        res = Check(123).is_not_none()
        self.assertIsInstance(res, Check)
        try:
            Check(None).is_not_none()
            self.fail()
        except CheckError:
            pass
