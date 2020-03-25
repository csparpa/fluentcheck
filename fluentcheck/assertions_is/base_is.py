from typing import Any


class IsBase:
    __check = None

    def __init__(self, object_under_test: Any):
        self.object = object_under_test

    def __call__(self, *args, **kwargs):
        return self

    @property
    def check(self):
        if not IsBase.__check:
            from ..classes import Check
            IsBase.__check = Check

        return IsBase.__check(self.object)
