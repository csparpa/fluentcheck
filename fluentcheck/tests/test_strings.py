import unittest
from fluentcheck.check import Check, CheckError


class TestNumbersAssertions(unittest.TestCase):

    def test_is_number(self):
        # ints
        val = 123
        res = Check(val).is_number()
        self.assertIsInstance(res, Check)

        # floats
        val = float(123)
        res = Check(val).is_number()
        self.assertIsInstance(res, Check)

        # complexes
        val = complex(33.44, 55.66)
        res = Check(val).is_number()
        self.assertIsInstance(res, Check)

        # test failure
        val = 'not-a-number'
        self.assertTrue(all([not isinstance(val, kls) for kls in Check.NUMERIC_TYPES]))
        try:
            Check(val).is_number()
            self.fail()
        except CheckError:
            pass