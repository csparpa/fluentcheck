import unittest

from fluentcheck import Is
from fluentcheck.exceptions import CheckError


# noinspection PyStatementEffect
class TestIsNumbersAssertions(unittest.TestCase):

    def test_is_number_pass(self):
        self.assertIsInstance(Is(7).number, Is)
        Is(123).number  # ints
        Is(float(123)).number  # floats
        Is(complex(33.44, 55.66)).number  # complex

    def test_is_number_fail(self):
        obj = 'not-a-number'
        with self.assertRaises(CheckError):
            Is(obj).number

    def test_is_not_number_pass(self):
        obj = 'not-a-number'
        self.assertIsInstance(Is(obj).not_number, Is)

    def test_is_not_number_fail(self):
        with self.assertRaises(CheckError):
            Is(123).not_number  # ints
        with self.assertRaises(CheckError):
            Is(float(123)).not_number  # floats
        with self.assertRaises(CheckError):
            Is(complex(33.44, 55.66)).not_number  # complex

    def test_is_integer_pass(self):
        obj = 123
        self.assertIsInstance(Is(obj).integer, Is)

    def test_is_integer_fail(self):
        with self.assertRaises(CheckError):
            Is(123.0).integer  # floats
        with self.assertRaises(CheckError):
            Is("Seventy Two").integer  # non-numbers

    def test_is_not_integer_pass(self):
        obj = "Seventy Two"
        self.assertIsInstance(Is(obj).not_integer, Is)

    def test_is_not_integer_fail(self):
        with self.assertRaises(CheckError):
            Is(123).not_integer

    def test_is_float_pass(self):
        self.assertIsInstance(Is(123.9).float, Is)

    def test_is_float_fail(self):
        with self.assertRaises(CheckError):
            Is(123).float

    def test_is_not_float_pass(self):
        self.assertIsInstance(Is(123).not_float, Is)

    def test_is_not_float_fail(self):
        with self.assertRaises(CheckError):
            Is(123.9).not_float

    def test_is_real_pass(self):
        self.assertIsInstance(Is(123.9).real, Is)

    def test_is_real_fail(self):
        with self.assertRaises(CheckError):
            Is(complex(1.2, 3.4)).real
        with self.assertRaises(CheckError):
            Is('seven').real

    def test_is_not_real_pass(self):
        obj = complex(1.2, 3.4)
        self.assertIsInstance(Is(obj).not_real, Is)

    def test_is_not_real_fail(self):
        with self.assertRaises(CheckError):
            Is('test').not_real
        with self.assertRaises(CheckError):
            Is(123.9).not_real

    def test_is_complex_pass(self):
        obj = complex(1.2, 3.4)
        self.assertIsInstance(Is(obj).complex, Is)

    def test_is_complex_fail(self):
        with self.assertRaises(CheckError):
            Is(123).complex
        with self.assertRaises(CheckError):
            Is(123.9).complex

    def test_is_not_complex_pass(self):
        self.assertIsInstance(Is(7).not_complex, Is)
        self.assertIsInstance(Is(7.0).not_complex, Is)

    def test_is_not_complex_fail(self):
        with self.assertRaises(CheckError):
            Is(complex(1.2, 3.4)).not_complex

    def test_is_positive_pass(self):
        self.assertIsInstance(Is(7).positive, Is)

    def test_is_positive_fail(self):
        with self.assertRaises(CheckError):
            Is(0).positive
        with self.assertRaises(CheckError):
            Is(-1).positive

    def test_is_not_positive_pass(self):
        self.assertIsInstance(Is(-1).not_positive, Is)
        self.assertIsInstance(Is(0).not_positive, Is)

    def test_is_not_positive_fail(self):
        with self.assertRaises(CheckError):
            Is(7).not_positive

    def test_is_negative_pass(self):
        self.assertIsInstance(Is(-.1).negative, Is)

    def test_is_negative_fail(self):
        with self.assertRaises(CheckError):
            Is(0).negative
        with self.assertRaises(CheckError):
            Is(1).negative

    def test_is_not_negative_pass(self):
        self.assertIsInstance(Is(0).not_negative, Is)
        self.assertIsInstance(Is(1).not_negative, Is)

    def test_is_not_negative_fail(self):
        with self.assertRaises(CheckError):
            Is(-1).not_negative

    def test_is_zero_pass(self):
        self.assertIsInstance(Is(0).zero, Is)

    def test_is_zero_fail(self):
        with self.assertRaises(CheckError):
            Is(-1).zero
        with self.assertRaises(CheckError):
            Is(1).zero

    def test_is_nonzero_pass(self):
        self.assertIsInstance(Is(1).nonzero, Is)
        self.assertIsInstance(Is(-1).nonzero, Is)

    def test_is_nonzero_fail(self):
        with self.assertRaises(CheckError):
            Is(0).nonzero

    def test_is_at_least_pass(self):
        obj = 7
        self.assertIsInstance(Is(obj).at_least(obj), Is)
        Is(obj).at_least(-obj).at_least(obj - .5).at_least(obj)

    def test_is_at_least_fail(self):
        with self.assertRaises(CheckError):
            Is(7).at_least(7 + .000001)

    def test_is_at_most_pass(self):
        obj = 7
        self.assertIsInstance(Is(obj).at_least(obj), Is)
        Is(obj).at_most(obj).at_most(obj + .5)

    def test_is_at_most_fail(self):
        with self.assertRaises(CheckError):
            Is(7).at_most(7 - .000001)

    def test_is_between_pass(self):
        self.assertIsInstance(Is(5.4).between(5, 6), Is)

    def test_is_between_fail(self):
        with self.assertRaises(CheckError):
            Is(7).between(5, 6)
        with self.assertRaises(CheckError):
            Is(4).between(5, 6)

    def test_is_not_between_pass(self):
        self.assertIsInstance(Is(7).not_between(5, 6), Is)
        self.assertIsInstance(Is(4).not_between(5, 6), Is)

    def test_is_not_between_fail(self):
        with self.assertRaises(CheckError):
            Is(5.5).not_between(5, 6)
