from ..is_cls import Is
from ..classes import Check


def string(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_string()
    return check_obj


def not_string(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_string()
    return check_obj


def contains_numbers(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).contains_numbers()
    return check_obj


def not_contains_numbers(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).not_contains_numbers()
    return check_obj


def only_numbers(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).contains_numbers_only()
    return check_obj


def contains_chars(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).contains_chars()
    return check_obj


def not_contains_chars(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).not_contains_chars()
    return check_obj


def only_chars(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).contains_chars_only()
    return check_obj


def contains_spaces(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).contains_spaces()
    return check_obj


def lowercase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_lowercase()
    return check_obj


def not_lowercase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_lowercase()
    return check_obj


def uppercase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_uppercase()
    return check_obj


def not_uppercase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_uppercase()
    return check_obj


def camelcase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_camelcase()
    return check_obj


def not_camelcase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_camelcase()
    return check_obj


def snakecase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_snakecase()
    return check_obj


def not_snakecase(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_snakecase()
    return check_obj


def unicode(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_unicode()
    return check_obj


def not_unicode(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_unicode()
    return check_obj


def json(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_json()
    return check_obj


def not_json(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_json()
    return check_obj


def yaml(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_yaml()
    return check_obj


def not_yaml(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_yaml()
    return check_obj


def xml(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_xml()
    return check_obj


def not_xml(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_xml()
    return check_obj


def matches(check_obj, pattern: str) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).matches(pattern)
    return check_obj


def not_matches(check_obj, pattern: str) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).not_matches(pattern)
    return check_obj


def contains_char(check_obj, char: str) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).contains_char(char)
    return check_obj


def not_contains_char(check_obj, char: str) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).not_contains_char(char)
    return check_obj


def shorter_than(check_obj, max_length: int) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_shorter_than(max_length)
    return check_obj


def longer_than(check_obj, min_length: int) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_longer_than(min_length)
    return check_obj


def length(check_obj, exact_length: int) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).has_length(exact_length)
    return check_obj


def not_length(check_obj, exact_length: int) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).has_not_length(exact_length)
    return check_obj
