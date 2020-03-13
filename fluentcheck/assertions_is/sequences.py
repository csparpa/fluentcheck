from ..is_cls import Is
from ..classes import Check


def empty(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_empty()
    return check_obj


def not_empty(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_empty()
    return check_obj


def iterable(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_iterable()
    return check_obj


def not_iterable(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_iterable()
    return check_obj


def couple(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_couple()
    return check_obj


def triplet(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_triplet()
    return check_obj


def nuple(check_obj, dimension: int) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_nuple(dimension)
    return check_obj


def has_dimensionality(check_obj, dimensionality: int) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).has_dimensionality(dimensionality)
    return check_obj


def tuple(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_tuple()
    return check_obj


def list(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_list()
    return check_obj