import unittest

from fluentcheck import Is
from fluentcheck.exceptions import CheckError


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

    #################################################
    # NOT IN Check tests
    # def test_is_lowercase_pass(self):
    #     obj = "hello world"
    #     self.assertIsInstance(Is(obj).lowercase, Is)

    def test_is_lowercase_fail(self):
        obj = "good Bye"
        with self.assertRaises(CheckError):
            Is(obj).lowercase

    # TODO: Why does this fail?
    # def test_is_not_lowercase_pass(self):
    #     obj = "HELLOWORLD"
    #     self.assertIsInstance(Is(obj).not_lowercase, Is)

    def test_is_not_lowercase_fail(self):
        obj = "Goodbye"
        with self.assertRaises(CheckError):
            Is(obj).not_lowercase

    # TODO: THis is broken in check
    # fluentcheck.exceptions.CheckError: HELLO WORLD is not empty
    # def test_is_uppercase_pass(self):
    #     obj = "HELLO WORLD"
    #     self.assertIsInstance(Is(obj).uppercase, Is)

    def test_is_uppercase_fail(self):
        obj = "Goodbye"
        with self.assertRaises(CheckError):
            Is(obj).uppercase

    # TODO: Why does this fail? Need input example.
    # def test_is_not_uppercase_pass(self):
    #     obj = "helloworld"
    #     self.assertIsInstance(Is(obj).not_uppercase, Is)

    def test_is_not_uppercase_fail(self):
        obj = "good Bye"
        with self.assertRaises(CheckError):
            Is(obj).not_uppercase

    def test_is_camelcase_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).camelcase, Is)

    def test_is_camelcase_fail(self):
        obj = "goodbye"
        with self.assertRaises(CheckError):
            Is(obj).camelcase

    def test_is_not_camelcase_pass(self):
        obj = "hello world"
        self.assertIsInstance(Is(obj).not_camelcase, Is)

    def test_is_not_camelcase_fail(self):
        obj = "GoodBye"
        with self.assertRaises(CheckError):
            Is(obj).not_camelcase

    # TODO:
    # Why does this fail?
    # def test_is_snakecase_pass(self):
    #     obj = "hello_world"
    #     self.assertIsInstance(Is(obj).snakecase, Is)

    def test_is_snakecase_fail(self):
        obj = "goodbye"
        with self.assertRaises(CheckError):
            Is(obj).snakecase

    # TODO: Why does this fail?
    # def test_is_not_snakecase_pass(self):
    #     obj = "HelloWorld"
    #     self.assertIsInstance(Is(obj).not_snakecase, Is)

    def test_is_not_snakecase_fail(self):
        obj = "good_bye"
        with self.assertRaises(CheckError):
            Is(obj).not_snakecase

    # TODO: Need some example input here.
    # def test_is_unicode_pass(self):
    #     obj = "Hello world"
    #     self.assertIsInstance(Is(obj).unicode, Is)
    #
    # def test_is_unicode_fail(self):
    #     obj = "goodbye"
    #     with self.assertRaises(CheckError):
    #         Is(obj).unicode
    #
    # def test_is_not_unicode_pass(self):
    #     obj = "Hello world"
    #     self.assertIsInstance(Is(obj).not_unicode, Is)
    #
    # def test_is_not_unicode_fail(self):
    #     obj = "goodbye"
    #     with self.assertRaises(CheckError):
    #         Is(obj).not_unicode

    def test_is_matches_pass(self):
        obj = 'abyss'
        pattern = '^a...s$'
        self.assertIsInstance(Is(obj).matches(pattern), Is)

    def test_is_matches_fail(self):
        obj = "goodbye"
        pattern = '^a...s$'
        with self.assertRaises(CheckError):
            Is(obj).matches(pattern)

    def test_is_not_matches_pass(self):
        obj = "goodbye"
        pattern = '^a...s$'
        self.assertIsInstance(Is(obj).not_matches(pattern), Is)

    def test_is_not_matches_fail(self):
        obj = 'abyss'
        pattern = '^a...s$'
        with self.assertRaises(CheckError):
            Is(obj).not_matches(pattern)
