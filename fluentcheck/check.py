import re
import json
import yaml
import types
from xml.etree import ElementTree


class CheckError(Exception):
    pass


class Check:

    NUMERIC_TYPES = (int, long, float, complex)

    def __init__(self, value):
        self._val = value

    @property
    def value(self):
        return self._val

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

    def is_real(self):
        self.is_number()
        try:
            assert not isinstance(self._val, complex)
            return self
        except AssertionError:
            raise CheckError('{} is not real'.format(self._val))

    def is_not_real(self):
        self.is_number()
        try:
            assert isinstance(self._val, complex)
            return self
        except AssertionError:
            raise CheckError('{} is real'.format(self._val))

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
        self.is_number().is_not_complex()
        try:
            assert float(self._val) > 0.
            return self
        except AssertionError:
            raise CheckError('{} is non-positive'.format(self._val))

    def is_negative(self):
        self.is_number().is_not_complex()
        try:
            assert float(self._val) < 0.
            return self
        except AssertionError:
            raise CheckError('{} is non-negative'.format(self._val))

    def is_zero(self):
        self.is_number().is_not_complex()
        try:
            assert float(self._val) == 0.
            return self
        except AssertionError:
            raise CheckError('{} is non-zero'.format(self._val))

    def is_at_least(self, lower):
        self.is_number()
        Check(lower).is_number()
        try:
            assert float(self._val) >= float(lower)
            return self
        except AssertionError:
            raise CheckError('{} is smaller than {}'.format(self._val, lower))

    def is_at_most(self, upper):
        self.is_number()
        Check(upper).is_number()
        try:
            assert float(self._val) <= float(upper)
            return self
        except AssertionError:
            raise CheckError('{} is bigger than {}'.format(self._val, upper))

    def is_between(self, lower, upper):
        self.is_number()
        Check(lower).is_number()
        Check(upper).is_number()
        self.is_at_least(lower).is_at_most(upper)
        return self

    # Sequences

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

    def is_iterable(self):
        try:
            iter(self._val)
            return self
        except TypeError:
            raise CheckError('{} is not iterable'.format(self._val))

    def is_not_iterable(self):
        try:
            iter(self._val)
            raise CheckError('{} is iterable'.format(self._val))
        except TypeError:
            return self

    def is_couple(self):
        self.is_iterable()
        try:
            assert len(self._val) == 2
            return self
        except AssertionError:
            raise CheckError('{} is not a sequence of 2 items'.format(self._val))

    def is_triplet(self):
        self.is_iterable()
        try:
            assert len(self._val) == 3
            return self
        except AssertionError:
            raise CheckError('{} is not a sequence of 3 items'.format(self._val))

    def is_nuple(self, dimension):
        self.is_iterable()
        try:
            assert len(self._val) == dimension
            return self
        except AssertionError:
            raise CheckError('{} is not a sequence of {} items'.format(self._val, dimension))

    def has_dimensionality(self, dimensionality):
        self.is_not_string()

        def get_dimensionality(item):
            try:
                iter(item)
            except TypeError:
                return 0
            return 1 + get_dimensionality(item[0])
        actual_dimensionality = get_dimensionality(self._val)
        if actual_dimensionality == dimensionality:
            return self
        else:
            raise CheckError('{} has actual dimensionality of {}, not {}'.format(
                self._val, actual_dimensionality, dimensionality))

    # Tuples
    def is_tuple(self):
        try:
            assert isinstance(self._val, tuple)
            return self
        except AssertionError:
            raise CheckError('{} is not a tuple'.format(self._val))

    # List
    def is_list(self):
        try:
            assert isinstance(self._val, list)
            return self
        except AssertionError:
            raise CheckError('{} is not a list'.format(self._val))

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

    def is_unicode(self):
        try:
            assert isinstance(self._val, unicode)
            return self
        except AssertionError:
            raise CheckError('{} is not Unicode'.format(self._val))

    def is_not_unicode(self):
        try:
            assert not isinstance(self._val, unicode)
            return self
        except AssertionError:
            raise CheckError('{} is Unicode'.format(self._val))

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

    # Booleans
    def is_boolean(self):
        try:
            assert isinstance(self._val, bool)
            return self
        except AssertionError:
            raise CheckError('{} is not boolean'.format(self._val))

    def is_not_boolean(self):
        try:
            assert not isinstance(self._val, bool)
            return self
        except AssertionError:
            raise CheckError('{} is boolean'.format(self._val))

    def is_truthy(self):
        try:
            assert self._val
            return self
        except AssertionError:
            raise CheckError('{} is falsy'.format(self._val))

    def is_falsy(self):
        try:
            assert not self._val
            return self
        except AssertionError:
            raise CheckError('{} is truthy'.format(self._val))

    def is_not_truthy(self):
        self.is_falsy()

    def is_not_falsy(self):
        self.is_truthy()

    def is_true(self):
        self.is_boolean()
        self.is_truthy()

    def is_false(self):
        self.is_boolean()
        self.is_falsy()

    def is_not_true(self):
        self.is_false()

    def is_not_false(self):
        self.is_true()

    def has_same_truth_of(self, value):
        try:
            assert bool(self._val) == bool(value)
            return self
        except AssertionError:
            raise CheckError('{} has a different truth of {}'.format(self._val,
                                                                     value))
    def has_opposite_truth_of(self, value):
        try:
            assert bool(self._val) != bool(value)
            return self
        except AssertionError:
            raise CheckError('{} has the same truth of {}'.format(self._val,
                                                                  value))

    # Dictionaries
    def is_dict(self):
        try:
            assert isinstance(self._val, dict)
            return self
        except AssertionError:
            raise CheckError('{} is not a dict'.format(self._val))

    def is_not_dict(self):
        try:
            assert not isinstance(self._val, dict)
            return self
        except AssertionError:
            raise CheckError('{} is a dict'.format(self._val))

    def has_keys(self, *args):
        self.is_dict()
        cur_key = ''
        try:
            for key in args:
                cur_key = key
                assert key in self._val
            return self
        except AssertionError:
            raise CheckError('{} does not contain key: {}'.format(self._val,
                                                                  cur_key))

    def has_not_keys(self, *args):
        self.is_dict()
        cur_key = ''
        try:
            for key in args:
                cur_key = key
                assert not key in self._val
            return self
        except AssertionError:
            raise CheckError('{} does contains key: {}'.format(self._val,
                                                               cur_key))

    # Types hierarchy

    def is_subtype_of(self, _type):
        try:
            assert issubclass(self._val.__class__, _type)
            return self
        except AssertionError:
            raise CheckError('{} is not subtype of {}'.format(self._val, _type))

    def is_not_subtype_of(self, _type):
        try:
            assert issubclass(self._val.__class__, _type)
            raise CheckError('{} is subtype of {}'.format(self._val, _type))
        except AssertionError:
            return self

    # Custom types

    def is_of_type(self, _type):
        try:
            assert isinstance(self._val, _type)
            return self
        except AssertionError:
            raise CheckError('{} is not of type {}'.format(self._val,
                                                           _type))

    def is_not_of_type(self, _type):
        try:
            assert not isinstance(self._val, _type)
            return self
        except AssertionError:
            raise CheckError('{} is of type {}'.format(self._val,
                                                       _type))
    # Modules

    def is_module(self):
        try:
            assert isinstance(self._val, types.ModuleType)
            return self
        except AssertionError:
            raise CheckError('{} is not a module'.format(self._val))

    def is_not_module(self):
        try:
            assert not isinstance(self._val, types.ModuleType)
            return self
        except AssertionError:
            raise CheckError('{} is a module'.format(self._val))

    # Functions

    def is_runnable(self):
        try:
            assert isinstance(self._val, types.FunctionType)
            return self
        except AssertionError:
            raise CheckError('{} is not runnable'.format(self._val))

    def is_not_runnable(self):
        try:
            assert not isinstance(self._val, types.FunctionType)
            return self
        except AssertionError:
            raise CheckError('{} is runnable'.format(self._val))

    # Any type

    def equals(self, expected):
        try:
            assert self._val == expected
            return self
        except AssertionError:
            raise CheckError('{} does not equal {}'.format(self._val, expected))

    def not_equals(self, expected):
        try:
            assert self._val == expected
            raise CheckError('{} equals {}'.format(self._val, expected))
        except AssertionError:
            return self

    # Geographic coords

    def is_latitude(self):
        self.is_real()
        try:
            self.is_between(-90.0, 90.0)
            return self
        except AssertionError:
            raise CheckError('{} is not a valid latitude'.format(self._val))

    def is_longitude(self):
        self.is_real()
        try:
            self.is_between(-180.0, 180.0)
            return self
        except AssertionError:
            raise CheckError('{} is not a valid longitude'.format(self._val))

    def is_azimuth(self):
        try:
            self.is_number().is_positive()
        except:
            raise CheckError('{} is not a valid azimuth'.format(self._val))

    def is_geopoint(self):
        self.is_couple()
        try:
            first = Check(self._val[0])
            first.is_long()
            second = Check(self._val[1])
            second.is_latitude()
        except AssertionError:
            raise CheckError('{} is not a valid geographic point'.format(self._val))