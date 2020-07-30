from ..exceptions import CheckError


def is_empty(check_obj):
    try:
        assert len(check_obj._val) == 0
        return check_obj
    except Exception as e:
        raise CheckError('{} is not empty'.format(check_obj._val)) from e


def is_not_empty(check_obj):
    try:
        assert len(check_obj._val) != 0
        return check_obj
    except Exception as e:
        raise CheckError('{} is empty'.format(check_obj._val)) from e


def is_iterable(check_obj):
    try:
        iter(check_obj._val)
        return check_obj
    except TypeError as e:
        raise CheckError('{} is not iterable'.format(check_obj._val)) from e


def is_not_iterable(check_obj):
    try:
        iter(check_obj._val)
        raise CheckError('{} is iterable'.format(check_obj._val))
    except TypeError:
        return check_obj


def is_couple(check_obj):
    check_obj.is_iterable()
    try:
        assert len(check_obj._val) == 2
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a sequence of 2 items'.format(check_obj._val)) from e


def is_triplet(check_obj):
    check_obj.is_iterable()
    try:
        assert len(check_obj._val) == 3
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a sequence of 3 items'.format(check_obj._val)) from e


def is_nuple(check_obj, dimension):
    check_obj.is_iterable()
    try:
        assert len(check_obj._val) == dimension
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a sequence of {} items'.format(check_obj._val, dimension)) from e


def has_dimensionality(check_obj, dimensionality):
    check_obj.is_not_string()

    def get_dimensionality(item):
        try:
            iter(item)
        except TypeError:
            return 0
        return 1 + get_dimensionality(item[0])

    actual_dimensionality = get_dimensionality(check_obj._val)
    if actual_dimensionality == dimensionality:
        return check_obj
    else:
        raise CheckError('{} has actual dimensionality of {}, not {}'.format(
            check_obj._val, actual_dimensionality, dimensionality))


# Tuples
def is_tuple(check_obj):
    try:
        assert isinstance(check_obj._val, tuple)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a tuple'.format(check_obj._val)) from e


# List
def is_list(check_obj):
    try:
        assert isinstance(check_obj._val, list)
        return check_obj
    except AssertionError as e:
        raise CheckError('{} is not a list'.format(check_obj._val)) from e
