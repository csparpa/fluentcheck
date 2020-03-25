from fluentcheck.assertions_is.base_is import IsBase


class __IsTypes(IsBase):
    def subtype_of(self, class_type) -> "Is":
        self.check.is_subtype_of(class_type)
        return self

    def not_subtype_of(self, class_type) -> "Is":
        self.check.is_not_subtype_of(class_type)
        return self

    def of_type(self, class_type) -> "Is":
        self.check.is_of_type(class_type)
        return self

    def not_of_type(self, class_type) -> "Is":
        self.check.is_not_of_type(class_type)
        return self

    @property
    def module(self) -> "Is":
        self.check.is_module()
        return self

    @property
    def not_module(self) -> "Is":
        self.check.is_not_module()
        return self

    @property
    def runnable(self) -> "Is":
        self.check.is_runnable()
        return self

    @property
    def not_runnable(self) -> "Is":
        self.check.is_not_runnable()
        return self
