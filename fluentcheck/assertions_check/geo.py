from ..classes import Check
from ..exceptions import CheckError


def is_latitude(check_obj):
    check_obj.is_real()
    try:
        check_obj.is_between(-90.0, 90.0)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a valid latitude'.format(check_obj.value))


def is_longitude(check_obj):
    check_obj.is_real()
    try:
        check_obj.is_between(-180.0, 180.0)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a valid longitude'.format(check_obj.value))


def is_azimuth(check_obj):
    try:
        check_obj.is_number().is_positive()
    except:
        raise CheckError('{} is not a valid azimuth'.format(check_obj.value))


def is_geopoint(check_obj):
    check_obj.is_couple()
    try:
        first = Check(check_obj.value[0])
        first.is_long()
        second = Check(check_obj.value[1])
        second.is_latitude()
    except AssertionError:
        raise CheckError('{} is not a valid geographic point'.format(check_obj.value))
