from typing import Any, Set

from fluentcheck import Check


class Is:
    def __init__(self, object_under_test: Any):
        self.object = object_under_test

    @property
    def none(self) -> "Is":
        Check(self.object).is_none()
        return self

    @property
    def not_none(self) -> "Is":
        Check(self.object).is_not_none()
        return self

    @property
    def boolean(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_boolean()
        return self

    @property
    def not_boolean(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_boolean()
        return self

    @property
    def true(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_true()
        return self

    @property
    def false(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_false()
        return self

    @property
    def not_true(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_true()
        return self

    @property
    def not_false(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_false()
        return self

    @property
    def falsy(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_falsy()
        return self

    @property
    def not_falsy(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_falsy()
        return self

    @property
    def truthy(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_truthy()
        return self

    @property
    def not_truthy(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_truthy()
        return self

    @property
    def set(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_set()
        return self

    @property
    def not_set(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_set()
        return self

    def subset_of(self, full_set: Set[Any]) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_subset_of(full_set)
        return self

    def not_subset_of(self, full_set: Set[Any]) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_subset_of(full_set)
        return self

    def superset_of(self, full_set: Set[Any]) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_superset_of(full_set)
        return self

    def not_superset_of(self, subset: Set[Any]) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_superset_of(subset)
        return self

    def intersects(self, other_set: Set[Any]) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).intersects(other_set)
        return self

    def not_intersects(self, other_set: Set[Any]) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).not_intersects(other_set)
        return self

    def has_same_truth_of(self, compare_obj) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).has_same_truth_of(compare_obj)
        return self

    def has_opposite_truth_of(self, compare_obj) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).has_opposite_truth_of(compare_obj)
        return self
