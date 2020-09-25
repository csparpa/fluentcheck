import types as t
from ..exceptions import CheckError


def is_subtype_of(check_obj, _type):
    try:
        assert issubclass(check_obj._val.__class__, _type)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not subtype of {}'.format(check_obj._val, _type))


def is_not_subtype_of(check_obj, _type):
    try:
        assert not issubclass(check_obj._val.__class__, _type)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is subtype of {}'.format(check_obj._val, _type)) from e


def is_of_type(check_obj, _type):
    try:
        assert isinstance(check_obj._val, _type)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not of type {}'.format(check_obj._val, _type)) from e


def is_not_of_type(check_obj, _type):
    try:
        assert not isinstance(check_obj._val, _type)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is of type {}'.format(check_obj._val, _type)) from e


def is_module(check_obj):
    try:
        assert isinstance(check_obj._val, t.ModuleType)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a module'.format(check_obj._val)) from e


def is_not_module(check_obj):
    try:
        assert not isinstance(check_obj._val, t.ModuleType)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is a module'.format(check_obj._val)) from e


def is_runnable(check_obj):
    try:
        assert isinstance(check_obj._val, t.FunctionType)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not runnable'.format(check_obj._val)) from e


def is_not_runnable(check_obj):
    try:
        assert not isinstance(check_obj._val, t.FunctionType)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is runnable'.format(check_obj._val)) from e
