from fluentcheck.assertions_is.base_is import IsBase


class __IsNumbers(IsBase):
    @property
    def number(self) -> "Is":
        self.check.is_number()
        return self

    @property
    def not_number(self) -> "Is":
        self.check.is_not_number()
        return self

    @property
    def integer(self) -> "Is":
        self.check.is_integer()
        return self

    @property
    def not_integer(self) -> "Is":
        self.check.is_not_integer()
        return self

    @property
    def float(self) -> "Is":
        self.check.is_float()
        return self

    @property
    def not_float(self) -> "Is":
        self.check.is_not_float()
        return self

    @property
    def real(self) -> "Is":
        self.check.is_real()
        return self

    @property
    def not_real(self) -> "Is":
        self.check.is_not_real()
        return self

    @property
    def complex(self) -> "Is":
        self.check.is_complex()
        return self

    @property
    def not_complex(self) -> "Is":
        self.check.is_not_complex()
        return self

    @property
    def positive(self) -> "Is":
        self.check.is_positive()
        return self

    @property
    def not_positive(self) -> "Is":
        self.check.is_not_positive()
        return self

    @property
    def negative(self) -> "Is":
        self.check.is_negative()
        return self

    @property
    def not_negative(self) -> "Is":
        self.check.is_not_negative()
        return self

    @property
    def zero(self) -> "Is":
        self.check.is_zero()
        return self

    @property
    def nonzero(self) -> "Is":
        self.check.is_not_zero()
        return self

    def at_least(self, number) -> "Is":
        self.check.is_at_least(number)
        return self

    def equal_to(self,number) -> "Is":
        self.check.is_equal_to(number)
        return self

    def not_equal_to(self,number) -> "Is":
        self.check.is_not_equal_to(number)
        return self

    def at_most(self, number) -> "Is":
        self.check.is_at_most(number)
        return self

    def between(self, lower_bound, upper_bound) -> "Is":
        self.check.is_between(lower_bound, upper_bound)
        return self

    def not_between(self, lower_bound, upper_bound) -> "Is":
        self.check.is_not_between(lower_bound, upper_bound)
        return self
