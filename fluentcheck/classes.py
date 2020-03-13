import importlib
import inspect
import pkgutil
from inspect import signature
from typing import Any

from .assertions_is.base_is import IsBase
from .assertions_is.booleans import __IsBoolAsserts
from .exceptions import CheckError


class Check:

    NUMERIC_TYPES = (int, float, complex)
    ASSERTIONS_PACKAGE = 'fluentcheck.assertions_check'

    def _import_assertion_modules(self):
        ass = importlib.import_module(Check.ASSERTIONS_PACKAGE)
        assertion_modules = list()
        for _1, module_name, _2 in pkgutil.iter_modules(ass.__path__):
            assertion_modules.append(importlib.import_module(ass.__name__ + '.' + module_name))
        return assertion_modules

    def __new__(cls, *args, **kwargs):
        # retrieve all modules in assertion package
        assertion_modules = cls._import_assertion_modules(cls)
        # bind Check object instance with assertion functions from assertion modules
        instance = super(Check, cls).__new__(cls)
        for module in assertion_modules:
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

    # Basic checks

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


class Is(__IsBoolAsserts):
    #
    # ASSERTIONS_PACKAGE = 'fluentcheck.assertions_is'
    #
    # def _import_assertion_modules(self):
    #     ass = importlib.import_module(Is.ASSERTIONS_PACKAGE)
    #     assertion_modules = list()
    #     for _1, module_name, _2 in pkgutil.iter_modules(ass.__path__):
    #         assertion_modules.append(importlib.import_module(ass.__name__ + '.' + module_name))
    #     return assertion_modules
    #
    # def __new__(cls, *args, **kwargs):
    #     # retrieve all modules in assertion package
    #     assertion_modules = cls._import_assertion_modules(cls)
    #     # bind Is object instance with assertion functions from assertion modules
    #     instance = super(Is, cls).__new__(cls)
    #     for module in assertion_modules:
    #         for item in inspect.getmembers(module, inspect.isfunction):
    #             func_name = item[0]
    #             func = item[1]
    #             if len(signature(func).parameters) == 1:  # should be attached as a property
    #                 setattr(Is, func_name, property(func, None, None, None))
    #             else:   # should be attached as a bound method
    #                 bound_method = func.__get__(instance, instance.__class__)
    #                 setattr(instance, func_name, bound_method)
    #     return instance
    #
    # def __init__(self, object_under_test: Any):
    #     self.object = object_under_test
    #
    # def __call__(self, *args, **kwargs):
    #     return self

    @property
    def none(self) -> "Is":
        Check(self.object).is_none()
        return self

    @property
    def not_none(self) -> "Is":
        Check(self.object).is_not_none()
        return self