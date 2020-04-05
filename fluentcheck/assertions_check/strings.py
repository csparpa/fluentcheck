import json
import re
import yaml
from ..exceptions import CheckError
from xml.etree import ElementTree


def is_string(check_obj):
    try:
        assert isinstance(check_obj.value, str)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a string'.format(check_obj.value))


def is_not_string(check_obj):
    try:
        assert not isinstance(check_obj.value, str)
        return check_obj
    except AssertionError:
        raise CheckError('{} is a string'.format(check_obj.value))


def contains_numbers(check_obj):
    check_obj.is_string()
    try:
        assert any(char.isdigit() for char in check_obj.value)
        return check_obj
    except AssertionError:
        raise CheckError('{} does not contain numbers'.format(check_obj.value))


def not_contains_numbers(check_obj):
    check_obj.is_string()
    try:
        assert not any(char.isdigit() for char in check_obj.value)
        return check_obj
    except AssertionError:
        raise CheckError('{} does not contain numbers'.format(check_obj.value))


def contains_numbers_only(check_obj):
    check_obj.is_string()
    try:
        assert check_obj.value.isdigit()
        return check_obj
    except AssertionError:
        raise CheckError('{} also contains numbers'.format(check_obj.value))


def contains_chars(check_obj):
    check_obj.is_string()
    try:
        assert bool(re.search('[a-zA-Z]', check_obj.value))
        return check_obj
    except AssertionError:
        raise CheckError('{} does not contain chars'.format(check_obj.value))


def not_contains_chars(check_obj):
    check_obj.is_string()
    try:
        assert not bool(re.search('[a-zA-Z]', check_obj.value))
        return check_obj
    except AssertionError:
        raise CheckError('{} contains chars'.format(check_obj.value))


def contains_chars_only(check_obj):
    check_obj.is_string()
    try:
        assert check_obj.value.isalpha()
        return check_obj
    except AssertionError:
        raise CheckError('{} also contains alphanumeric chars'.format(check_obj.value))


def contains_spaces(check_obj):
    check_obj.is_string()
    try:
        assert ' ' in check_obj.value
        return check_obj
    except AssertionError:
        raise CheckError('{} does not contain whitespaces'.format(check_obj.value))


def not_contains_spaces(check_obj):
    check_obj.is_string()
    try:
        assert not ' ' in check_obj.value
        return check_obj
    except AssertionError:
        raise CheckError('{} contains whitespaces'.format(check_obj.value))


def contains_char(check_obj, _char):
    check_obj.is_string()
    try:
        assert _char in check_obj.value
        return check_obj
    except AssertionError:
        raise CheckError('{} does not contain char: {}'.format(check_obj.value,
                                                               _char))


def not_contains_char(check_obj, _char):
    check_obj.is_string()
    try:
        assert not _char in check_obj.value
        return check_obj
    except AssertionError:
        raise CheckError('{} contains char: {}'.format(check_obj.value, _char))


def is_shorter_than(check_obj, n_chars):
    check_obj.is_string()
    try:
        assert len(check_obj.value) < n_chars
        return check_obj
    except AssertionError:
        raise CheckError('{} is longer than {}'.format(check_obj.value, n_chars))


def is_longer_than(check_obj, n_chars):
    check_obj.is_string()
    try:
        assert len(check_obj.value) > n_chars
        return check_obj
    except AssertionError:
        raise CheckError('{} is shorter than {}'.format(check_obj.value, n_chars))


def has_length(check_obj, n_items):
    check_obj.is_string()
    try:
        assert len(check_obj.value) == n_items
        return check_obj
    except AssertionError:
        raise CheckError('{} is not long {}'.format(check_obj.value, n_items))


def has_not_length(check_obj, n_items):
    check_obj.is_string()
    try:
        assert len(check_obj.value) != n_items
        return check_obj
    except AssertionError:
        raise CheckError('{} is long {}'.format(check_obj.value, n_items))


def is_lowercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert all([c.islower() for c in check_obj.value])
        return check_obj
    except AssertionError:
        raise CheckError('{} is not lowercase'.format(check_obj.value))


def is_not_lowercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert any([not c.islower() for c in check_obj.value])
        return check_obj
    except AssertionError:
        raise CheckError('{} is lowercase'.format(check_obj.value))


def is_uppercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert all([c.isupper() for c in check_obj.value])
        return check_obj
    except AssertionError:
        raise CheckError('{} is not uppercase'.format(check_obj.value))


def is_not_uppercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert any([not c.isupper() for c in check_obj.value])
        return check_obj
    except AssertionError:
        raise CheckError('{} is uppercase'.format(check_obj.value))


def is_snakecase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        tokens = check_obj.value.split('_')
        assert len(tokens) > 1
        assert not any([' ' in t for t in tokens])
        return check_obj
    except AssertionError:
        raise CheckError('{} is not snakecase'.format(check_obj.value))


def is_not_snakecase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        check_obj.is_snakecase()
        raise CheckError('{} is snakecase'.format(check_obj.value))
    except AssertionError:
        return check_obj


def is_camelcase(check_obj):
    check_obj.is_string()
    try:
        assert (check_obj.value != check_obj.value.lower() and check_obj.value != check_obj.value.upper())
        return check_obj
    except AssertionError:
        raise CheckError('{} is not camelcase'.format(check_obj.value))


def is_not_camelcase(check_obj):
    check_obj.is_string()
    try:
        assert not (check_obj.value != check_obj.value.lower() and check_obj.value != check_obj.value.upper())
        return check_obj
    except AssertionError:
        raise CheckError('{} is camelcase'.format(check_obj.value))


def is_json(check_obj):
    check_obj.is_string()
    try:
        json.loads(check_obj.value)
        return check_obj
    except ValueError:
        raise CheckError('{} is not valid JSON'.format(check_obj.value))


def is_not_json(check_obj):
    check_obj.is_string()
    try:
        json.loads(check_obj.value)
        raise CheckError('{} is valid JSON'.format(check_obj.value))
    except ValueError:
        return check_obj


def is_yaml(check_obj):
    check_obj.is_string()
    try:
        yaml.load(check_obj.value)
    except Exception:
        raise CheckError('{} is not valid YAML'.format(check_obj.value))
    else:
        return check_obj


def is_not_yaml(check_obj):
    check_obj.is_string()
    try:
        yaml.load(check_obj.value)
    except Exception:
        return check_obj
    else:
        raise CheckError('{} is valid YAML'.format(check_obj.value))


def is_xml(check_obj):
    check_obj.is_string()
    try:
        ElementTree.fromstring(check_obj.value)
    except Exception:
        raise CheckError('{} is not valid XML'.format(check_obj.value))
    else:
        return check_obj


def is_not_xml(check_obj):
    check_obj.is_string()
    try:
        ElementTree.fromstring(check_obj.value)
    except Exception:
        return check_obj
    else:
        raise CheckError('{} is valid XML'.format(check_obj.value))


def matches(check_obj, regex):
    check_obj.is_string()
    try:
        pattern = re.compile(regex)
        assert pattern.match(check_obj.value) is not None
        return check_obj
    except AssertionError:
        raise CheckError('{} does not match pattern: {}'.format(check_obj.value,
                                                                regex))


def not_matches(check_obj, regex):
    check_obj.is_string()
    try:
        pattern = re.compile(regex)
        assert not pattern.match(check_obj.value) is not None
        return check_obj
    except AssertionError:
        raise CheckError('{} matches pattern: {}'.format(check_obj.value, regex))
