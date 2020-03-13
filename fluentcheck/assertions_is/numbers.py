from .. import Is
from ..classes import Check


def number(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_number()
    return check_obj


def not_number(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_number()
    return check_obj


def integer(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_integer()
    return check_obj


def not_integer(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_integer()
    return check_obj


def float(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_float()
    return check_obj


def not_float(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_float()
    return check_obj


def real(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_real()
    return check_obj


def not_real(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_real()
    return check_obj


def complex(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_complex()
    return check_obj


def not_complex(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_complex()
    return check_obj


def positive(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_positive()
    return check_obj


def not_positive(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_positive()
    return check_obj


def negative(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_negative()
    return check_obj


def not_negative(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_negative()
    return check_obj


def zero(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_zero()
    return check_obj


def nonzero(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_zero()
    return check_obj


def at_least(check_obj, number) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_at_least(number)
    return check_obj


def at_most(check_obj, number) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_at_most(number)
    return check_obj


def between(check_obj, lower_bound, upper_bound) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_between(lower_bound, upper_bound)
    return check_obj


def not_between(check_obj, lower_bound, upper_bound) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_between(lower_bound, upper_bound)
    return check_obj