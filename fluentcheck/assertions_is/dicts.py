from fluentcheck.assertions_is.base_is import IsBase


class __IsDicts(IsBase):

    @property
    def dict(self) -> "Is":
        self.check.is_dict()
        return self

    @property
    def not_dict(self) -> "Is":
        self.check.is_not_dict()
        return self

    def has_keys(self, *keys) -> "Is":
        self.check.has_keys(*keys)
        return self

    def has_not_keys(self, *keys) -> "Is":
        self.check.has_not_keys(*keys)
        return self
