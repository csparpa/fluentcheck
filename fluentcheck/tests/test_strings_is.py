import unittest

from fluentcheck import Is
from fluentcheck.check import Check, CheckError


# noinspection PyStatementEffect
class TestIsStringsAssertions(unittest.TestCase):

    def test_is_string_pass(self):
        self.assertIsInstance(Is("Hello").string, Is)

    def test_is_subtype_of_fail(self):
        with self.assertRaises(CheckError):
            Is(123).string

    def test_is_not_string_pass(self):
        self.assertIsInstance(Is(123).not_string, Is)

    def test_is_not_subtype_of_fail(self):
        obj = "I actually am a string"
        with self.assertRaises(CheckError):
            Is(obj).not_string

    def test_is_contains_numbers_pass(self):
        obj = "Hello123World"
        self.assertIsInstance(Is(obj).contains_numbers, Is)

    def test_is_contains_numbers_fail(self):
        obj = "Hello world"
        with self.assertRaises(CheckError):
            Is(obj).contains_numbers

    def test_is_not_contains_numbers_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).not_contains_numbers, Is)

    def test_is_not_contains_numbers_fail(self):
        obj = "Hello123World"
        with self.assertRaises(CheckError):
            Is(obj).not_contains_numbers

    def test_is_only_numbers_pass(self):
        obj = "12399"
        self.assertIsInstance(Is(obj).only_numbers, Is)

    def test_is_only_numbers_fail(self):
        with self.assertRaises(CheckError):
            Is("123Hello123World").only_numbers
        with self.assertRaises(CheckError):
            Is("Hello World").only_numbers

    def test_is_contains_chars_pass(self):
        obj = "12a3"
        self.assertIsInstance(Is(obj).contains_chars, Is)

    def test_is_contains_chars_fail(self):
        with self.assertRaises(CheckError):
            Is("01234").contains_chars

    def test_is_not_contains_chars_pass(self):
        obj = "123"
        self.assertIsInstance(Is(obj).not_contains_chars, Is)

    def test_is_not_contains_chars_fail(self):
        with self.assertRaises(CheckError):
            Is("012a34").not_contains_chars

    def test_is_contains_chars_only_pass(self):
        obj = "abc"
        self.assertIsInstance(Is(obj).only_chars, Is)

    def test_is_contains_chars_only_fail(self):
        with self.assertRaises(CheckError):
            Is("012a34").only_chars

    def test_is_contains_spaces_pass(self):
        obj = "hello world"
        self.assertIsInstance(Is(obj).contains_spaces, Is)

    def test_is_contains_spaces_fail(self):
        with self.assertRaises(CheckError):
            Is("goodbye").contains_spaces

    def test_is_contains_char_pass(self):
        obj = "hello world"
        self.assertIsInstance(Is(obj).contains_char('w'), Is)

    def test_is_contains_char_fail(self):
        with self.assertRaises(CheckError):
            Is("goodbye").contains_char('z')

    def test_is_not_contains_char_pass(self):
        obj = "hello world"
        self.assertIsInstance(Is(obj).not_contains_char('z'), Is)

    def test_is_not_contains_char_fail(self):
        with self.assertRaises(CheckError):
            Is("goodbye").not_contains_char('y')

    def test_is_shorter_than_pass(self):
        obj = "Hi"
        self.assertIsInstance(Is(obj).shorter_than(5), Is)

    def test_is_shorter_than_fail(self):
        with self.assertRaises(CheckError):
            Is("goodbye").shorter_than(4)

    def test_is_longer_than_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).longer_than(5), Is)

    def test_is_longer_than_fail(self):
        with self.assertRaises(CheckError):
            Is("goodbye").longer_than(7)

    def test_is_length_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).length(len(obj)), Is)

    def test_is_length_fail(self):
        obj = "goodbye"
        with self.assertRaises(CheckError):
            Is(obj).length(len(obj) - 1)
        with self.assertRaises(CheckError):
            Is(obj).length(len(obj) + 1)

    def test_is_not_length_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).not_length(len(obj) + 1), Is)
        self.assertIsInstance(Is(obj).not_length(len(obj) - 1), Is)

    def test_is_not_length_fail(self):
        obj = "goodbye"
        with self.assertRaises(CheckError):
            Is(obj).not_length(len(obj))
