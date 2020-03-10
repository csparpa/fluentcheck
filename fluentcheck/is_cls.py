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

    @property
    def boolean(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_boolean()
        return self

    @property
    def not_boolean(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_boolean()
        return self

    @property
    def true(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_true()
        return self

    @property
    def false(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_false()
        return self

    @property
    def not_true(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_true()
        return self

    @property
    def not_false(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_false()
        return self

    @property
    def falsy(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_falsy()
        return self

    @property
    def not_falsy(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_falsy()
        return self

    @property
    def truthy(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_truthy()
        return self

    @property
    def not_truthy(self):
        # noinspection PyUnresolvedReferences
        Check(self.object).is_not_truthy()
        return self

    def has_same_truth_of(self, compare_obj):
        # noinspection PyUnresolvedReferences
        Check(self.object).has_same_truth_of(compare_obj)
        return self

    def has_opposite_truth_of(self, compare_obj):
        # noinspection PyUnresolvedReferences
        Check(self.object).has_opposite_truth_of(compare_obj)
        return self
