from typing import Any, Set, List

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

    @property
    def dict(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_dict()
        return self

    @property
    def not_dict(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_dict()
        return self

    @property
    def number(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_number()
        return self

    @property
    def integer(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_integer()
        return self

    @property
    def float(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_float()
        return self

    @property
    def not_float(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_float()
        return self

    @property
    def not_number(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_number()
        return self

    @property
    def not_integer(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_integer()
        return self

    @property
    def real(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_real()
        return self

    @property
    def not_real(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_real()
        return self

    @property
    def complex(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_complex()
        return self

    @property
    def not_complex(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_complex()
        return self

    @property
    def positive(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_positive()
        return self

    @property
    def negative(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_negative()
        return self

    @property
    def not_negative(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_negative()
        return self

    @property
    def not_positive(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_positive()
        return self

    @property
    def zero(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_zero()
        return self

    @property
    def nonzero(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_zero()
        return self

    @property
    def uuid1(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_uuid1()
        return self

    @property
    def not_uuid1(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_uuid1()
        return self

    @property
    def uuid4(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_uuid4()
        return self

    @property
    def not_uuid4(self) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_uuid4()
        return self

    def has_keys(self, *keys) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).has_keys(*keys)
        return self

    def not_has_keys(self, *keys) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).has_not_keys(*keys)
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

    def at_least(self, number) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_at_least(number)
        return self

    def at_most(self, number) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_at_most(number)
        return self

    def between(self, lower_bound, upper_bound) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_between(lower_bound, upper_bound)
        return self

    def not_between(self, lower_bound, upper_bound) -> "Is":
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_between(lower_bound, upper_bound)
        return self
