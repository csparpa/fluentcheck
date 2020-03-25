import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


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


    def test_is_not_number(self):
        val = 'not-a-number'
        self.assertTrue(all([not isinstance(val, kls) for kls in Check.NUMERIC_TYPES]))
        res = Check(val).is_not_number()
        self.assertIsInstance(res, Check)

        # test failures

        # ints
        val = 123
        try:
            Check(val).is_not_number()
            self.fail()
        except CheckError:
            pass

        # floats
        val = float(123)
        try:
            Check(val).is_not_number()
            self.fail()
        except CheckError:
            pass

        # complexes
        val = complex(33.44, 55.66)
        try:
            Check(val).is_not_number()
            self.fail()
        except CheckError:
            pass


    def test_is_integer(self):
        res = Check(123).is_integer()
        self.assertIsInstance(res, Check)

        try:
            Check(float(123)).is_integer()
            self.fail()
        except CheckError:
            pass


    def test_is_not_integer(self):
        res = Check('test').is_not_integer()
        self.assertIsInstance(res, Check)

        try:
            Check(123).is_not_integer()
            self.fail()
        except CheckError:
            pass


    def test_is_float(self):
        res = Check(123.9).is_float()
        self.assertIsInstance(res, Check)

        try:
            Check(123).is_float()
            self.fail()
        except CheckError:
            pass


    def test_is_not_float(self):
        res = Check('test').is_not_float()
        self.assertIsInstance(res, Check)

        try:
            Check(123.9).is_not_float()
            self.fail()
        except CheckError:
            pass


    def test_is_real(self):
        res = Check(123.9).is_real()
        self.assertIsInstance(res, Check)

        try:
            val = complex(1.2, 3.4)
            Check(val).is_real()
            Check('test').is_real()
            self.fail()
        except CheckError:
            pass


    def test_is_not_real(self):
        val = complex(1.2, 3.4)
        res = Check(val).is_not_real()
        self.assertIsInstance(res, Check)

        try:
            Check('test').is_not_real()
            self.fail()
        except:
            pass

        try:
            Check(123.9).is_not_real()
            self.fail()
        except CheckError:
            pass


    def test_is_complex(self):
        val = complex(1.2, 3.4)
        res = Check(val).is_complex()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_complex()
            self.fail()
        except CheckError:
            pass


    def test_is_not_complex(self):
        res = Check('test').is_not_complex()
        self.assertIsInstance(res, Check)

        try:
            val = complex(1.2, 3.4)
            Check(val).is_not_complex()
            self.fail()
        except CheckError:
            pass


    def test_is_positive(self):
        res = Check(2).is_positive()
        self.assertIsInstance(res, Check)
        try:
            Check(0).is_positive()
            self.fail()
        except CheckError:
            pass
        try:
            Check(-1).is_positive()
            self.fail()
        except CheckError:
            pass


    def test_is_not_positive(self):
        res = Check(-1).is_not_positive()
        self.assertIsInstance(res, Check)
        res = Check(0).is_not_positive()
        self.assertIsInstance(res, Check)

        try:
            Check(123).is_not_positive()
            self.fail()
        except CheckError:
            pass


    def test_is_negative(self):
        res = Check(-2).is_negative()
        self.assertIsInstance(res, Check)
        try:
            Check(0).is_negative()
            self.fail()
        except CheckError:
            pass
        try:
            Check(1).is_negative()
            self.fail()
        except CheckError:
            pass


    def test_is_not_negative(self):
        res = Check(1).is_not_negative()
        self.assertIsInstance(res, Check)
        res = Check(0).is_not_negative()
        self.assertIsInstance(res, Check)

        try:
            Check(-1).is_not_negative()
            self.fail()
        except CheckError:
            pass


    def test_is_zero(self):
        res = Check(0).is_zero()
        self.assertIsInstance(res, Check)
        try:
            Check(1).is_zero()
            self.fail()
        except CheckError:
            pass


    def test_is_not_zero(self):
        res = Check(1).is_not_zero()
        self.assertIsInstance(res, Check)
        try:
            Check(0).is_not_zero()
            self.fail()
        except CheckError:
            pass


    def test_is_at_least(self):
        res = Check(7).is_at_least(6.5)
        self.assertIsInstance(res, Check)
        res = Check(7).is_at_least(7)
        self.assertIsInstance(res, Check)
        try:
            Check(7).is_at_least(99)
            self.fail()
        except CheckError:
            pass


    def test_is_at_most(self):
        res = Check(6.5).is_at_most(7)
        self.assertIsInstance(res, Check)
        res = Check(7).is_at_most(7)
        self.assertIsInstance(res, Check)
        try:
            Check(7).is_at_most(3)
            self.fail()
        except CheckError:
            pass


    def test_is_between(self):
        res = Check(5.4).is_between(5, 6)
        self.assertIsInstance(res, Check)
        try:
            Check(5.4).is_between(2, 3)
            self.fail()
        except CheckError:
            pass


    def test_is_not_between(self):
        res = Check(5.4).is_not_between(1, 2)
        self.assertIsInstance(res, Check)
        try:
            Check(5.4).is_not_between(5, 6)
            self.fail()
        except CheckError:
            pass
