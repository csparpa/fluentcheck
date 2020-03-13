from ..is_cls import Is
from ..classes import Check


def latitude(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_latitude()
    return check_obj


def longitude(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_longitude()
    return check_obj


def azimuth(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_azimuth()
    return check_obj


def geopoint(check_obj) -> "Is":
    # noinspection PyUnresolvedReferences
    Check(check_obj.object).is_geopoint()
    return check_obj