from .. import Is
from ..classes import Check


def dict(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_dict()
    return check_obj


def not_dict(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_dict()
    return check_obj


def has_keys(check_obj, *keys) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).has_keys(*keys)
    return check_obj


def has_not_keys(check_obj, *keys) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).has_not_keys(*keys)
    return check_obj
