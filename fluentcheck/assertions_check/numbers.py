from ..classes import Check
from ..exceptions import CheckError


def is_number(check_obj):
    try:
        assert isinstance(check_obj.value, check_obj.NUMERIC_TYPES)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a number'.format(check_obj.value))


def is_not_number(check_obj):
    try:
        assert not isinstance(check_obj.value, check_obj.NUMERIC_TYPES)
        return check_obj
    except AssertionError:
        raise CheckError('{} is a number'.format(check_obj.value))


def is_integer(check_obj):
    try:
        assert isinstance(check_obj.value, int)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not integer'.format(check_obj.value))


def is_not_integer(check_obj):
    try:
        assert not isinstance(check_obj.value, int)
        return check_obj
    except AssertionError:
        raise CheckError('{} is integer'.format(check_obj.value))


def is_float(check_obj):
    try:
        assert isinstance(check_obj.value, float)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not float'.format(check_obj.value))


def is_not_float(check_obj):
    try:
        assert not isinstance(check_obj.value, float)
        return check_obj
    except AssertionError:
        raise CheckError('{} is float'.format(check_obj.value))


def is_real(check_obj):
    check_obj.is_number()
    try:
        assert not isinstance(check_obj.value, complex)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not real'.format(check_obj.value))


def is_not_real(check_obj):
    check_obj.is_number()
    try:
        assert isinstance(check_obj.value, complex)
        return check_obj
    except AssertionError:
        raise CheckError('{} is real'.format(check_obj.value))


def is_complex(check_obj):
    try:
        assert isinstance(check_obj.value, complex)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not complex'.format(check_obj.value))


def is_not_complex(check_obj):
    try:
        assert not isinstance(check_obj.value, complex)
        return check_obj
    except AssertionError:
        raise CheckError('{} is complex'.format(check_obj.value))


def is_positive(check_obj):
    check_obj.is_real()
    try:
        assert float(check_obj.value) > 0.
        return check_obj
    except AssertionError:
        raise CheckError('{} is zero or negative'.format(check_obj.value))


def is_not_positive(check_obj):
    check_obj.is_real()
    try:
        assert float(check_obj.value) <= 0
        return check_obj
    except AssertionError:
        raise CheckError('{} is positive'.format(check_obj.value))


def is_negative(check_obj):
    check_obj.is_real()
    try:
        assert float(check_obj.value) < 0.
        return check_obj
    except AssertionError:
        raise CheckError('{} is zero or positive'.format(check_obj.value))


def is_not_negative(check_obj):
    check_obj.is_real()
    try:
        assert float(check_obj.value) >= 0
        return check_obj
    except AssertionError:
        raise CheckError('{} is negative'.format(check_obj.value))


def is_zero(check_obj):
    check_obj.is_real()
    try:
        assert float(check_obj.value) == 0.
        return check_obj
    except AssertionError:
        raise CheckError('{} is non-zero'.format(check_obj.value))


def is_not_zero(check_obj):
    check_obj.is_real()
    try:
        assert float(check_obj.value) != 0.
        return check_obj
    except AssertionError:
        raise CheckError('{} is non-zero'.format(check_obj.value))


def is_at_least(check_obj, lower):
    check_obj.is_real()
    Check(lower).is_real()
    try:
        assert float(check_obj.value) >= float(lower)
        return check_obj
    except AssertionError:
        raise CheckError('{} is smaller than {}'.format(check_obj.value, lower))


def is_at_most(check_obj, upper):
    check_obj.is_real()
    Check(upper).is_real()
    try:
        assert float(check_obj.value) <= float(upper)
        return check_obj
    except AssertionError:
        raise CheckError('{} is bigger than {}'.format(check_obj.value, upper))


def is_between(check_obj, lower, upper):
    check_obj.is_real()
    Check(lower).is_real()
    Check(upper).is_real()
    check_obj.is_at_least(lower).is_at_most(upper)
    return check_obj


def is_not_between(check_obj, lower, upper):
    check_obj.is_real()
    Check(lower).is_real()
    Check(upper).is_real()
    try:
        assert float(check_obj.value) <= lower or float(check_obj.value) >= upper
        return check_obj
    except AssertionError:
        raise CheckError('{} is between {} and {}'.format(check_obj.value, lower, upper))


def is_equals(check_obj, number):
    check_obj.is_real()
    Check(number).is_real()
    try:
        assert float(check_obj.value) == float(number)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not equals to {}'.format(check_obj.value, number))


def is_not_equals(check_obj, number):
    check_obj.is_real()
    Check(number).is_real()
    try:
        assert float(check_obj.value) != float(number)
        return check_obj
    except AssertionError:
        raise CheckError('{} is equals to {}'.format(check_obj.value, number))
