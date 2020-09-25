from ..classes import Check
from ..exceptions import CheckError


def is_latitude(check_obj):
    check_obj.is_real()
    try:
        check_obj.is_between(-90.0, 90.0)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a valid latitude'.format(check_obj._val)) from e


def is_longitude(check_obj):
    check_obj.is_real()
    try:
        check_obj.is_between(-180.0, 180.0)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a valid longitude'.format(check_obj._val)) from e


def is_azimuth(check_obj):
    try:
        check_obj.is_number().is_positive()
        return check_obj
    except Exception as e:
        raise CheckError('{} is not a valid azimuth'.format(check_obj._val)) from e


def is_geopoint(check_obj):
    check_obj.is_couple()
    try:
        first = Check(check_obj._val[0])
        first.is_longitude()
        second = Check(check_obj._val[1])
        second.is_latitude()
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a valid geographic point'.format(check_obj._val)) from e
