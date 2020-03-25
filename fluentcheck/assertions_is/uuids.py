from fluentcheck.assertions_is.base_is import IsBase


class __IsUUIDs(IsBase):
    @property
    def uuid1(self) -> "Is":
        self.check.is_uuid1()
        return self

    @property
    def not_uuid1(self) -> "Is":
        self.check.is_not_uuid1()
        return self

    @property
    def uuid4(self) -> "Is":
        self.check.is_uuid4()
        return self

    @property
    def not_uuid4(self) -> "Is":
        self.check.is_not_uuid4()
        return self
