import json
import re
import yaml
from ..exceptions import CheckError
from xml.etree import ElementTree


def is_string(self):
    try:
        assert isinstance(self._val, str)
        return self
    except AssertionError:
        raise CheckError('{} is not a string'.format(self._val))


def is_not_string(self):
    try:
        assert not isinstance(self._val, str)
        return self
    except AssertionError:
        raise CheckError('{} is a string'.format(self._val))


def contains_numbers(self):
    self.is_string()
    try:
        assert any(char.isdigit() for char in self._val)
        return self
    except AssertionError:
        raise CheckError('{} does not contain numbers'.format(self._val))


def not_contains_numbers(self):
    self.is_string()
    try:
        assert not any(char.isdigit() for char in self._val)
        return self
    except AssertionError:
        raise CheckError('{} does not contain numbers'.format(self._val))


def contains_numbers_only(self):
    self.is_string()
    try:
        assert self._val.isdigit()
        return self
    except AssertionError:
        raise CheckError('{} also contains numbers'.format(self._val))


def contains_chars(self):
    self.is_string()
    try:
        assert bool(re.search('[a-zA-Z]', self._val))
        return self
    except AssertionError:
        raise CheckError('{} does not contain chars'.format(self._val))


def not_contains_chars(self):
    self.is_string()
    try:
        assert not bool(re.search('[a-zA-Z]', self._val))
        return self
    except AssertionError:
        raise CheckError('{} contains chars'.format(self._val))


def contains_chars_only(self):
    self.is_string()
    try:
        assert self._val.isalpha()
        return self
    except AssertionError:
        raise CheckError('{} also contains alphanumeric chars'.format(self._val))


def contains_spaces(self):
    self.is_string()
    try:
        assert ' ' in self._val
        return self
    except AssertionError:
        raise CheckError('{} does not contain whitespaces'.format(self._val))


def not_contains_spaces(self):
    self.is_string()
    try:
        assert not ' ' in self._val
        return self
    except AssertionError:
        raise CheckError('{} contains whitespaces'.format(self._val))


def contains_char(self, _char):
    self.is_string()
    try:
        assert _char in self._val
        return self
    except AssertionError:
        raise CheckError('{} does not contain char: {}'.format(self._val,
                                                               _char))


def not_contains_char(self, _char):
    self.is_string()
    try:
        assert not _char in self._val
        return self
    except AssertionError:
        raise CheckError('{} contains char: {}'.format(self._val, _char))


def is_shorter_than(self, n_chars):
    self.is_string()
    try:
        assert len(self._val) < n_chars
        return self
    except AssertionError:
        raise CheckError('{} is longer than {}'.format(self._val, n_chars))


def is_longer_than(self, n_chars):
    self.is_string()
    try:
        assert len(self._val) > n_chars
        return self
    except AssertionError:
        raise CheckError('{} is shorter than {}'.format(self._val, n_chars))


def has_length(self, n_items):
    self.is_string()
    try:
        assert len(self._val) == n_items
        return self
    except AssertionError:
        raise CheckError('{} is not long {}'.format(self._val, n_items))


def has_not_length(self, n_items):
    self.is_string()
    try:
        assert len(self._val) != n_items
        return self
    except AssertionError:
        raise CheckError('{} is long {}'.format(self._val, n_items))


def is_lowercase(self):
    self.is_string()
    if self.is_empty():
        return self
    try:
        assert all([c.islower() for c in self._val])
        return self
    except AssertionError:
        raise CheckError('{} is not lowercase'.format(self._val))


def is_not_lowercase(self):
    self.is_string()
    if self.is_empty():
        return self
    try:
        assert any([not c.islower() for c in self._val])
        return self
    except AssertionError:
        raise CheckError('{} is lowercase'.format(self._val))


def is_uppercase(self):
    self.is_string()
    if self.is_empty():
        return self
    try:
        assert all([c.isupper() for c in self._val])
        return self
    except AssertionError:
        raise CheckError('{} is not uppercase'.format(self._val))


def is_not_uppercase(self):
    self.is_string()
    if self.is_empty():
        return self
    try:
        assert any([not c.isupper() for c in self._val])
        return self
    except AssertionError:
        raise CheckError('{} is uppercase'.format(self._val))


def is_snakecase(self):
    self.is_string()
    if self.is_empty():
        return self
    try:
        tokens = self._val.split('_')
        assert len(tokens) > 1
        assert not any([' ' in t for t in tokens])
        return self
    except AssertionError:
        raise CheckError('{} is not snakecase'.format(self._val))


def is_not_snakecase(self):
    self.is_string()
    if self.is_empty():
        return self
    try:
        self.is_snakecase()
        raise CheckError('{} is snakecase'.format(self._val))
    except AssertionError:
        return self


def is_camelcase(self):
    self.is_string()
    try:
        assert (self._val != self._val.lower() and self._val != self._val.upper())
        return self
    except AssertionError:
        raise CheckError('{} is not camelcase'.format(self._val))


def is_not_camelcase(self):
    self.is_string()
    try:
        assert not (self._val != self._val.lower() and self._val != self._val.upper())
        return self
    except AssertionError:
        raise CheckError('{} is camelcase'.format(self._val))


def is_json(self):
    self.is_string()
    try:
        json.loads(self._val)
        return self
    except ValueError:
        raise CheckError('{} is not valid JSON'.format(self._val))


def is_not_json(self):
    self.is_string()
    try:
        json.loads(self._val)
        raise CheckError('{} is valid JSON'.format(self._val))
    except ValueError:
        return self


def is_yaml(self):
    self.is_string()
    try:
        yaml.loads(self._val)
        return self
    except ValueError:
        raise CheckError('{} is not valid YAML'.format(self._val))


def is_not_yaml(self):
    self.is_string()
    try:
        yaml.loads(self._val)
        raise CheckError('{} is valid YAML'.format(self._val))
    except ValueError:
        return self


def is_xml(self):
    self.is_string()
    try:
        ElementTree.fromstring(self._val)
        return self
    except ValueError:
        raise CheckError('{} is not valid XML'.format(self._val))


def is_not_xml(self):
    self.is_string()
    try:
        ElementTree.fromstring(self._val)
        raise CheckError('{} is valid XML'.format(self._val))
    except ValueError:
        return self


def matches(self, regex):
    self.is_string()
    try:
        pattern = re.compile(regex)
        assert pattern.match(self._val) is not None
        return self
    except AssertionError:
        raise CheckError('{} does not match pattern: {}'.format(self._val,
                                                                regex))


def not_matches(self, regex):
    self.is_string()
    try:
        pattern = re.compile(regex)
        assert not pattern.match(self._val) is not None
        return self
    except AssertionError:
        raise CheckError('{} matches pattern: {}'.format(self._val, regex))
