from typing import Any

from fluentcheck import Check


class Is:
    def __init__(self, object: Any):
        self.object = object

    @property
    def none(self):
        Check(self.object).is_none()
        return self

    @property
    def not_none(self):
        Check(self.object).is_not_none()
        return self
