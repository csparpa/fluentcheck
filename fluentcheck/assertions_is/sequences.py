from fluentcheck.assertions_is.base_is import IsBase


class __IsSequences(IsBase):
    @property
    def empty(self) -> "Is":
        self.check.is_empty()
        return self

    @property
    def not_empty(self) -> "Is":
        self.check.is_not_empty()
        return self

    @property
    def iterable(self) -> "Is":
        self.check.is_iterable()
        return self

    @property
    def not_iterable(self) -> "Is":
        self.check.is_not_iterable()
        return self

    @property
    def couple(self) -> "Is":
        self.check.is_couple()
        return self

    @property
    def triplet(self) -> "Is":
        self.check.is_triplet()
        return self

    # noinspection SpellCheckingInspection
    def nuple(self, dimension: int) -> "Is":
        self.check.is_nuple(dimension)
        return self

    def has_dimensionality(self, dimensionality: int) -> "Is":
        self.check.has_dimensionality(dimensionality)
        return self

    @property
    def tuple(self) -> "Is":
        self.check.is_tuple()
        return self

    @property
    def list(self) -> "Is":
        self.check.is_list()
        return self
