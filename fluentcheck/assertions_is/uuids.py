from ..is_cls import Is
from ..classes import Check


def uuid1(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_uuid1()
    return check_obj


def not_uuid1(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_uuid1()
    return check_obj


def uuid4(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_uuid4()
    return check_obj


def not_uuid4(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_not_uuid4()
    return check_obj
