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

    def test_is_long(self):
        # check what Python version we're running
        try:
            val = long(123)
            res = Check(val).is_long()
            self.assertIsInstance(res, Check)

            try:
                Check('not-a-number').is_long()
                self.fail()
            except CheckError:
                pass
        except NameError:  # it's Python3
            try:
                Check(123).is_long()
                self.fail()
            except CheckError:
                pass

    def test_is_not_long(self):
        try:
            res = Check(123).is_not_long()
            self.assertIsInstance(res, Check)

            try:
                val = long(123)
                Check(val).is_not_long()
                self.fail()
            except CheckError:  # it's Python3
                pass
        except CheckError:
            a=1
            try:
                Check(123).is_not_long()
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
    
    # UUIDs

    def test_is_uuid1(self):
        res = Check('5245eb82-31e6-11e9-8bfa-d8cb8a1a56c7').is_uuid1()
        self.assertIsInstance(res, Check)
        try:
            Check('9f9b0fc0-e3bb-43af-9894-7b73c83374d1').is_uuid1() #Version 4 UUID should not validate as version 1
            self.fail()
        except CheckError:
            pass
        try:
            Check('fluent').is_uuid1()
            self.fail()
        except CheckError:
            pass 

    def test_is_not_uuid1(self):
        res = Check('9f9b0fc0-e3bb-43af-9894-7b73c83374d1').is_not_uuid1() # version 4 uuid
        self.assertIsInstance(res, Check)
        try:
            Check('fluent').is_not_uuid1()
        except:
            self.fail()
    """ try:
            Check('9194da68-31e8-11e9-8677-d8cb8a1a56c7').is_not_uuid1() # valid version 1 uuid
            self.fail()
        except CheckError:
            pass"""

    def test_is_uuid4(self):
        res = Check('80d2fde3-dc11-4e0c-a23d-3ebbfb203681').is_uuid4()
        self.assertIsInstance(res, Check)
        try:
            Check('e3cad24c-31e7-11e9-8936-d8cb8a1a56c7').is_uuid4() # Version 1 UUID should not validate as version 4
            self.fail()
        except CheckError:
            pass
        try:
            Check('fluent').is_uuid4()
            self.fail()
        except CheckError:
            pass

    def test_is_not_uuid4(self):
        res = Check('f2b7a812-31e8-11e9-898b-d8cb8a1a56c7').is_not_uuid4() # version 1 uuid
        self.assertIsInstance(res, Check)
    """    res = Check('fluent').is_not_uuid4()
        self.assertIsInstance(res, Check)
        try:
            Check('725655d0-9840-4aec-9e3e-83e707dfa37c').is_not_uuid4() # version 4 uuid
            self.fail()
        except CheckError:
            pass"""