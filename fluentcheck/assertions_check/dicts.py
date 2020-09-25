from ..exceptions import CheckError


def is_dict(check_obj):
    try:
        assert isinstance(check_obj._val, dict)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a dict'.format(check_obj._val)) from e


def is_not_dict(check_obj):
    try:
        assert not isinstance(check_obj._val, dict)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is a dict'.format(check_obj._val)) from e


def has_keys(check_obj, *args):
    check_obj.is_dict()
    cur_key = ''
    try:
        for key in args:
            cur_key = key
            assert key in check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does not contain key: {}'.format(check_obj._val,
                                                              cur_key)) from e


def has_not_keys(check_obj, *args):
    check_obj.is_dict()
    cur_key = ''
    try:
        for key in args:
            cur_key = key
            assert not key in check_obj._val
        return check_obj
    except AssertionError as e:
        raise CheckError('{} does contains key: {}'.format(check_obj._val, cur_key)) from e
