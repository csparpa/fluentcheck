import importlib
import inspect
import pkgutil
from inspect import signature
from typing import Any, Set, List
from .classes import Check


class Is:

    ASSERTIONS_PACKAGE = 'fluentcheck.assertions_is'

    def _import_assertion_modules(self):
        ass = importlib.import_module(Is.ASSERTIONS_PACKAGE)
        assertion_modules = list()
        for _1, module_name, _2 in pkgutil.iter_modules(ass.__path__):
            assertion_modules.append(importlib.import_module(ass.__name__ + '.' + module_name))
        return assertion_modules

    def __new__(cls, *args, **kwargs):
        # retrieve all modules in assertion package
        assertion_modules = cls._import_assertion_modules(cls)
        # bind Is object instance with assertion functions from assertion modules
        instance = super(Is, cls).__new__(cls)
        for module in assertion_modules:
            for item in inspect.getmembers(module, inspect.isfunction):
                func_name = item[0]
                func = item[1]
                if len(signature(func).parameters) == 1:  # should be attached as a property
                    setattr(Is, func_name, property(func, None, None, None))
                else:   # should be attached as a bound method
                    bound_method = func.__get__(instance, instance.__class__)
                    setattr(instance, func_name, bound_method)
        return instance

    def __init__(self, object_under_test: Any):
        self.object = object_under_test

    def __call__(self, *args, **kwargs):
        return self

    @property
    def none(self) -> "Is":
        Check(self.object).is_none()
        return self

    @property
    def not_none(self) -> "Is":
        Check(self.object).is_not_none()
        return self
