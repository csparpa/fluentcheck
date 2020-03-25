from typing import Any, Set
from .base_is import IsBase


class __IsCollections(IsBase):
    @property
    def set(self) -> "Is":
        self.check.is_set()
        return self

    @property
    def not_set(self) -> "Is":
        self.check.is_not_set()
        return self

    def subset_of(self, full_set: Set[Any]) -> "Is":
        self.check.is_subset_of(full_set)
        return self

    def not_subset_of(self, full_set: Set[Any]) -> "Is":
        self.check.is_not_subset_of(full_set)
        return self

    def superset_of(self, full_set: Set[Any]) -> "Is":
        self.check.is_superset_of(full_set)
        return self

    def not_superset_of(self, subset: Set[Any]) -> "Is":
        self.check.is_not_superset_of(subset)
        return self

    def intersects(self, other_set: Set[Any]) -> "Is":
        self.check.intersects(other_set)
        return self

    def not_intersects(self, other_set: Set[Any]) -> "Is":
        self.check.not_intersects(other_set)
        return self
