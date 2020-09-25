from ..exceptions import CheckError


def is_boolean(check_obj):
    try:
        assert isinstance(check_obj._val, bool)
        return check_obj
    except AssertionError as ae:
        raise CheckError('{} is not boolean'.format(check_obj._val)) from ae


def is_not_boolean(check_obj):
    try:
        assert not isinstance(check_obj._val, bool)
        return check_obj
    except AssertionError as ae:
        raise CheckError('{} is boolean'.format(check_obj._val)) from ae


def is_truthy(check_obj):
    try:
        assert check_obj._val
        return check_obj
    except AssertionError as ae:
        raise CheckError('{} is falsy'.format(check_obj._val)) from ae


def is_falsy(check_obj):
    try:
        assert not check_obj._val
        return check_obj
    except AssertionError as ae:
        raise CheckError('{} is truthy'.format(check_obj._val)) from ae


def is_not_truthy(check_obj):
    return check_obj.is_falsy()


def is_not_falsy(check_obj):
    return check_obj.is_truthy()


def is_true(check_obj):
    return check_obj.is_truthy().is_boolean()


def is_false(check_obj):
    return check_obj.is_falsy().is_boolean()


def is_not_true(check_obj):
    return check_obj.is_false()


def is_not_false(check_obj):
    return check_obj.is_true()


def has_same_truth_of(check_obj, value):
    try:
        assert bool(check_obj._val) == bool(value)
        return check_obj
    except AssertionError as ae:
        raise CheckError('{} has a different truth of {}'.format(check_obj._val,
                                                                 value)) from ae


def has_opposite_truth_of(check_obj, value):
    try:
        assert bool(check_obj._val) != bool(value)
        return check_obj
    except AssertionError as ae:
        raise CheckError('{} has the same truth of {}'.format(check_obj._val,
                                                              value)) from ae
