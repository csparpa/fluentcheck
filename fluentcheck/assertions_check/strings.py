import json
import re
from xml.etree import ElementTree

import yaml

from ..exceptions import CheckError


def is_string(check_obj):
    try:
        assert isinstance(check_obj._val, str)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a string'.format(check_obj._val)) from e


def is_not_string(check_obj):
    try:
        assert not isinstance(check_obj._val, str)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is a string'.format(check_obj._val)) from e


def contains_numbers(check_obj):
    check_obj.is_string()
    try:
        assert any(char.isdigit() for char in check_obj._val)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not contain numbers'.format(check_obj._val)) from e


def not_contains_numbers(check_obj):
    check_obj.is_string()
    try:
        assert not any(char.isdigit() for char in check_obj._val)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not contain numbers'.format(check_obj._val)) from e


def contains_numbers_only(check_obj):
    check_obj.is_string()
    try:
        assert check_obj._val.isdigit()
        return check_obj
    except AssertionError as e:
        raise CheckError('{} also contains numbers'.format(check_obj._val)) from e


def contains_chars(check_obj):
    check_obj.is_string()
    try:
        assert bool(re.search('[a-zA-Z]', check_obj._val))
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not contain chars'.format(check_obj._val)) from e


def not_contains_chars(check_obj):
    check_obj.is_string()
    try:
        assert not bool(re.search('[a-zA-Z]', check_obj._val))
        return check_obj
    except AssertionError as e:
        raise CheckError('{} contains chars'.format(check_obj._val)) from e


def contains_chars_only(check_obj):
    check_obj.is_string()
    try:
        assert check_obj._val.isalpha()
        return check_obj
    except AssertionError as e:
        raise CheckError('{} also contains alphanumeric chars'.format(check_obj._val)) from e


def contains_spaces(check_obj):
    check_obj.is_string()
    try:
        assert ' ' in check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not contain whitespaces'.format(check_obj._val)) from e


def not_contains_spaces(check_obj):
    check_obj.is_string()
    try:
        assert not ' ' in check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} contains whitespaces'.format(check_obj._val)) from e


def contains_char(check_obj, _char):
    check_obj.is_string()
    try:
        assert _char in check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not contain char: {}'.format(check_obj._val,
                                                               _char)) from e

def same_as(check_obj, __char):
    check_obj.is_string()
    try:
        assert __char == check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not match : {}'.format(check_obj._val,
                                                               _char)) from e

def not_same_as():
    check_obj.is_string()
    try:
        assert __char != check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is same as : {}'.format(check_obj._val,
                                                               _char)) from e

def not_contains_char(check_obj, _char):
    check_obj.is_string()
    try:
        assert not _char in check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} contains char: {}'.format(check_obj._val, _char)) from e


def is_shorter_than(check_obj, n_chars):
    check_obj.is_string()
    try:
        assert len(check_obj._val) < n_chars
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is longer than {}'.format(check_obj._val, n_chars)) from e


def is_longer_than(check_obj, n_chars):
    check_obj.is_string()
    try:
        assert len(check_obj._val) > n_chars
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is shorter than {}'.format(check_obj._val, n_chars)) from e


def has_length(check_obj, n_items):
    check_obj.is_string()
    try:
        assert len(check_obj._val) == n_items
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not long {}'.format(check_obj._val, n_items)) from e


def has_not_length(check_obj, n_items):
    check_obj.is_string()
    try:
        assert len(check_obj._val) != n_items
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is long {}'.format(check_obj._val, n_items)) from e


def is_lowercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert all([c.islower() for c in check_obj._val])
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not lowercase'.format(check_obj._val)) from e


def is_not_lowercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert any([not c.islower() for c in check_obj._val])
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is lowercase'.format(check_obj._val)) from e


def is_uppercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert all([c.isupper() for c in check_obj._val])
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not uppercase'.format(check_obj._val)) from e


def is_not_uppercase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        assert any([not c.isupper() for c in check_obj._val])
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is uppercase'.format(check_obj._val)) from e


def is_snakecase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        tokens = check_obj._val.split('_')
        assert len(tokens) > 1
        assert not any([' ' in t for t in tokens])
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not snakecase'.format(check_obj._val)) from e


def is_not_snakecase(check_obj):
    check_obj.is_string()
    if check_obj.is_empty():
        return check_obj
    try:
        check_obj.is_snakecase()
        raise CheckError('{} is snakecase'.format(check_obj._val))
    except AssertionError:
        return check_obj


def is_camelcase(check_obj):
    check_obj.is_string()
    try:
        assert (check_obj._val != check_obj._val.lower() and check_obj._val != check_obj._val.upper())
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not camelcase'.format(check_obj._val)) from e


def is_not_camelcase(check_obj):
    check_obj.is_string()
    try:
        assert not (check_obj._val != check_obj._val.lower() and check_obj._val != check_obj._val.upper())
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is camelcase'.format(check_obj._val)) from e


def is_json(check_obj):
    check_obj.is_string()
    try:
        json.loads(check_obj._val)
        return check_obj
    except ValueError:
        raise CheckError('{} is not valid JSON'.format(check_obj._val))


def is_not_json(check_obj):
    check_obj.is_string()
    try:
        json.loads(check_obj._val)
        raise CheckError('{} is valid JSON'.format(check_obj._val))
    except ValueError:
        return check_obj


def is_yaml(check_obj):
    check_obj.is_string()
    try:
        yaml.safe_load(check_obj._val)
    except Exception as e:
        raise CheckError('{} is not valid YAML'.format(check_obj._val)) from e
    else:
        return check_obj


def is_not_yaml(check_obj):
    check_obj.is_string()
    try:
        yaml.safe_load(check_obj._val)
    except Exception:
        return check_obj
    else:
        raise CheckError('{} is valid YAML'.format(check_obj._val))


def is_xml(check_obj):
    check_obj.is_string()
    try:
        ElementTree.fromstring(check_obj._val)
    except Exception as e:
        raise CheckError('{} is not valid XML'.format(check_obj._val)) from e
    else:
        return check_obj


def is_not_xml(check_obj):
    check_obj.is_string()
    try:
        ElementTree.fromstring(check_obj._val)
    except Exception:
        return check_obj
    else:
        raise CheckError('{} is valid XML'.format(check_obj._val))


def matches(check_obj, regex):
    check_obj.is_string()
    try:
        pattern = re.compile(regex)
        assert pattern.match(check_obj._val) is not None
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not match pattern: {}'.format(check_obj._val, regex)) from e


def not_matches(check_obj, regex):
    check_obj.is_string()
    try:
        pattern = re.compile(regex)
        assert not pattern.match(check_obj._val) is not None
        return check_obj
    except AssertionError as e:
        raise CheckError('{} matches pattern: {}'.format(check_obj._val, regex)) from e
