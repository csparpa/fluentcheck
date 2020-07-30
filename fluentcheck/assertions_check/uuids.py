from uuid import UUID

from ..exceptions import CheckError


def is_uuid1(check_obj):
    try:
        assert (UUID(check_obj.value).version == 1)
        return check_obj
    except (AssertionError, AttributeError, ValueError) as e:
        raise CheckError('{} is not a valid uuid1 exception: {}'.format(check_obj._val, e)) from e


def is_not_uuid1(check_obj):
    try:
        assert UUID(check_obj._val).version != 1
        return check_obj
    except ValueError as ve:  # check_obj._val is not a UUID at all
        raise CheckError('{} is not a valid uuid'.format(check_obj._val)) from ve
    except Exception as e:  # check_obj._val is a UUID, but is indeed v1
        raise CheckError('{} is a uuid1'.format(check_obj._val)) from e


def is_uuid4(check_obj):
    try:
        assert (UUID(check_obj.value).version == 4)
        return check_obj
    except (AssertionError, AttributeError, ValueError) as e:
        raise CheckError('{} is not a valid uuid4'.format(check_obj._val)) from e


def is_not_uuid4(check_obj):
    try:
        assert UUID(check_obj._val).version != 4
        return check_obj
    except ValueError as ve:  # check_obj._val is not a UUID at all
        raise CheckError('{} is not a valid uuid'.format(check_obj._val)) from ve
    except Exception as e:  # check_obj._val is a UUID, but is indeed v4
        raise CheckError('{} is a uuid4'.format(check_obj._val)) from e
