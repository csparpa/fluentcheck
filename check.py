import re
import json
import yaml
from xml.etree import ElementTree


'''
Assert(val).is_not_None().is_dict().is_not_list().is_not_tuple().is_not_set().is_not_object()
Assert(val).not_contains(MyType1)
Assert(val).not_contains_any_of(MyType1, MyType2)
Assert(val).not_contains_strings()
Assert(val).not_contains_numbers(MyType1, MyType2)
Assert(val).is_not_of_type(MyType)
Assert(val).is_of_type(MyType)
Assert(val).is_module()
Assert(val).is_package()
'''

class CheckError(Exception):
    pass


class Check():

    NUMERIC_TYPES = (int, long, float, complex)

    def __init__(self, value):
        self._val = value

    # Nonethiness

    def is_none(self):
        try:
            assert self._val is None
            return self
        except AssertionError:
            raise CheckError('{} is not None'.format(self._val))

    def is_not_none(self):
        try:
            assert self._val is not None
            return self
        except AssertionError:
            raise CheckError('{} is None'.format(self._val))

    # Numbers

    def is_number(self):
        try:
            assert isinstance(self._val, self.NUMERIC_TYPES)
            return self
        except AssertionError:
            raise CheckError('{} is not a number'.format(self._val))

    def is_not_number(self):
        try:
            assert not isinstance(self._val, self.NUMERIC_TYPES)
            return self
        except AssertionError:
            raise CheckError('{} is a number'.format(self._val))

    def is_integer(self):
        try:
            assert isinstance(self._val, int)
            return self
        except AssertionError:
            raise CheckError('{} is not integer'.format(self._val))

    def is_not_integer(self):
        try:
            assert not isinstance(self._val, int)
            return self
        except AssertionError:
            raise CheckError('{} is integer'.format(self._val))

    def is_long(self):
        try:
            assert isinstance(self._val, long)
            return self
        except AssertionError:
            raise CheckError('{} is not long'.format(self._val))

    def is_not_long(self):
        try:
            assert not isinstance(self._val, long)
            return self
        except AssertionError:
            raise CheckError('{} is long'.format(self._val))

    def is_float(self):
        try:
            assert isinstance(self._val, float)
            return self
        except AssertionError:
            raise CheckError('{} is not float'.format(self._val))

    def is_not_float(self):
        try:
            assert not isinstance(self._val, float)
            return self
        except AssertionError:
            raise CheckError('{} is float'.format(self._val))

    def is_complex(self):
        try:
            assert isinstance(self._val, complex)
            return self
        except AssertionError:
            raise CheckError('{} is not complex'.format(self._val))

    def is_not_complex(self):
        try:
            assert not isinstance(self._val, complex)
            return self
        except AssertionError:
            raise CheckError('{} is complex'.format(self._val))

    def is_positive(self):
        self.is_not_complex()
        try:
            assert float(self._val) > 0.
            return self
        except AssertionError:
            raise CheckError('{} is non-positive'.format(self._val))

    def is_negative(self):
        self.is_not_complex()
        try:
            assert float(self._val) < 0.
            return self
        except AssertionError:
            raise CheckError('{} is non-negative'.format(self._val))

    def is_zero(self):
        self.is_not_complex()
        try:
            assert float(self._val) == 0.
            return self
        except AssertionError:
            raise CheckError('{} is non-zero'.format(self._val))

    def is_at_least(self, lower):
        Check(lower).is_number()
        try:
            assert float(self._val) >= float(lower)
            return self
        except AssertionError:
            raise CheckError('{} is smaller than {}'.format(self._val, lower))

    def is_at_most(self, upper):
        Check(upper).is_number()
        try:
            assert float(self._val) <= float(upper)
            return self
        except AssertionError:
            raise CheckError('{} is bigger than {}'.format(self._val, upper))

    def is_between(self, lower, upper):
        Check(lower).is_number()
        Check(upper).is_number()
        self.is_at_least(lower).is_at_most(upper)
        return self

    # Strings

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
        try:
            assert bool(re.search('[a-zA-Z]', self._val))
            return self
        except AssertionError:
            raise CheckError('{} does not contain chars'.format(self._val))

    def not_contains_chars(self):
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

    def contains(self, _char):
        self.is_string()
        try:
            assert _char in self._val
            return self
        except AssertionError:
            raise CheckError('{} does not contain char: {}'.format(self._val,
                                                                   _char))

    def not_contains(self, _char):
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

    def has_length(self, n_chars):
        self.is_string()
        try:
            assert len(self._val) == n_chars
            return self
        except AssertionError:
            raise CheckError('{} is not long {}'.format(self._val, n_chars))

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

    # multi-type methods

    def is_empty(self):
        try:
            assert len(self._val) == 0
            return self
        except:
            raise CheckError('{} is not empty'.format(self._val))

    def is_not_empty(self):
        try:
            assert len(self._val) != 0
            return self
        except:
            raise CheckError('{} is empty'.format(self._val))

if __name__ == '__main__':
    val = 's'
    Check(val).is_not_json().is_not_empty()