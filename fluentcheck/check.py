import inspect
from .exceptions import CheckError


class Check:

    NUMERIC_TYPES = (int, float, complex)

    def __new__(cls, *args, **kwargs):
        # import assertion functions from submodules
        from fluentcheck.assertions import numbers as ass_numb
        from fluentcheck.assertions import sequences as ass_seq
        from fluentcheck.assertions import strings as ass_str
        from fluentcheck.assertions import booleans as ass_bool
        from fluentcheck.assertions import dicts as ass_dicts
        from fluentcheck.assertions import types as ass_types
        from fluentcheck.assertions import geo as ass_geo
        from fluentcheck.assertions import uuids as ass_uuids
        from fluentcheck.assertions import collections as ass_colls
        instance = super(Check, cls).__new__(cls)
        for module in [ass_numb, ass_seq, ass_str, ass_bool, ass_dicts, ass_types,
                       ass_geo, ass_uuids, ass_colls]:
            for item in inspect.getmembers(module, inspect.isfunction):
                func_name = item[0]
                func = item[1]
                bound_method = func.__get__(instance, instance.__class__)
                setattr(instance, func_name, bound_method)
        return instance

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
