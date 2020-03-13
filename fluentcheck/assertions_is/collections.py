from .. import Is
from ..classes import Check
from typing import Any, Set


def set(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_set()
    return check_obj


def not_set(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_set()
    return check_obj


def subset_of(check_obj, full_set: Set[Any]) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_subset_of(full_set)
    return check_obj


def not_subset_of(check_obj, full_set: Set[Any]) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_subset_of(full_set)
    return check_obj


def superset_of(check_obj, full_set: Set[Any]) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_superset_of(full_set)
    return check_obj


def not_superset_of(check_obj, subset: Set[Any]) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_superset_of(subset)
    return check_obj


def intersects(check_obj, other_set: Set[Any]) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).intersects(other_set)
    return check_obj


def not_intersects(check_obj, other_set: Set[Any]) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).not_intersects(other_set)
    return check_obj
