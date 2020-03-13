from .. import Is
from ..classes import Check


def boolean(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_boolean()
    return check_obj


def not_boolean(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_boolean()
    return check_obj


def true(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_true()
    return check_obj


def false(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_false()
    return check_obj


def not_true(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_true()
    return check_obj


def not_false(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_false()
    return check_obj


def falsy(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_falsy()
    return check_obj


def not_falsy(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_falsy()
    return check_obj


def truthy(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_truthy()
    return check_obj


def not_truthy(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_truthy()
    return check_obj


def has_same_truth_of(check_obj, compare_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).has_same_truth_of(compare_obj)
    return check_obj


def has_opposite_truth_of(check_obj, compare_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).has_opposite_truth_of(compare_obj)
    return check_obj
