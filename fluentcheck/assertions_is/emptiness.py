from .base_is import IsBase


class __IsEmptiness(IsBase):
    @property
    def none(self) -> "Is":
        self.check.is_none()
        return self

    @property
    def not_none(self) -> "Is":
        self.check.is_not_none()
        return self
