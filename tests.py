import unittest
from fluentcheck.check import Check, CheckError


class TestCheck(unittest.TestCase):

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
        self.assertTrue(all([not isinstance(val, kls)for kls in Check.NUMERIC_TYPES]))
        try:
            Check(val).is_number()
            self.fail()
        except CheckError:
            pass

        # this tests are only for Python2
        try:
            val = long('110011010', base=2)  # 410L
            res = Check(val).is_number()
            self.assertIsInstance(res, Check)
        except NameError:
            pass

    def test_is_not_number(self):
        val = 'not-a-number'
        self.assertTrue(all([not isinstance(val, kls)for kls in Check.NUMERIC_TYPES]))
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

        # this tests are only for Python2
        try:
            val = long('110011010', base=2)  # 410L
            try:
                res = Check(val).is_not_number()
                self.fail()
            except CheckError:
                pass
        except NameError:
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