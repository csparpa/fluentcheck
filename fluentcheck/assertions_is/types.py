from .. import Is
from ..classes import Check


def subtype_of(check_obj, class_type) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_subtype_of(class_type)
    return check_obj


def not_subtype_of(check_obj, class_type) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_subtype_of(class_type)
    return check_obj


def of_type(check_obj, class_type) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_of_type(class_type)
    return check_obj


def not_of_type(check_obj, class_type) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_of_type(class_type)
    return check_obj


def module(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_module()
    return check_obj


def not_module(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_module()
    return check_obj


def runnable(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_runnable()
    return check_obj


def not_runnable(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_runnable()
    return check_obj
