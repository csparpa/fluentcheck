import types as t
from ..exceptions import CheckError


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


def is_of_type(self, _type):
    try:
        assert isinstance(self._val, _type)
        return self
    except AssertionError:
        raise CheckError('{} is not of type {}'.format(self._val, _type))


def is_not_of_type(self, _type):
    try:
        assert not isinstance(self._val, _type)
        return self
    except AssertionError:
        raise CheckError('{} is of type {}'.format(self._val, _type))


def is_module(self):
    try:
        assert isinstance(self._val, t.ModuleType)
        return self
    except AssertionError:
        raise CheckError('{} is not a module'.format(self._val))


def is_not_module(self):
    try:
        assert not isinstance(self._val, t.ModuleType)
        return self
    except AssertionError:
        raise CheckError('{} is a module'.format(self._val))


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