from ..exceptions import CheckError


def is_empty(check_obj):
    try:
        assert len(check_obj.value) == 0
        return check_obj
    except:
        raise CheckError('{} is not empty'.format(check_obj.value))


def is_not_empty(check_obj):
    try:
        assert len(check_obj.value) != 0
        return check_obj
    except:
        raise CheckError('{} is empty'.format(check_obj.value))


def is_iterable(check_obj):
    try:
        iter(check_obj.value)
        return check_obj
    except TypeError:
        raise CheckError('{} is not iterable'.format(check_obj.value))


def is_not_iterable(check_obj):
    try:
        iter(check_obj.value)
        raise CheckError('{} is iterable'.format(check_obj.value))
    except TypeError:
        return check_obj


def is_couple(check_obj):
    check_obj.is_iterable()
    try:
        assert len(check_obj.value) == 2
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a sequence of 2 items'.format(check_obj.value))


def is_triplet(check_obj):
    check_obj.is_iterable()
    try:
        assert len(check_obj.value) == 3
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a sequence of 3 items'.format(check_obj.value))


def is_nuple(check_obj, dimension):
    check_obj.is_iterable()
    try:
        assert len(check_obj.value) == dimension
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a sequence of {} items'.format(check_obj.value, dimension))


def has_dimensionality(check_obj, dimensionality):
    check_obj.is_not_string()

    def get_dimensionality(item):
        try:
            iter(item)
        except TypeError:
            return 0
        return 1 + get_dimensionality(item[0])

    actual_dimensionality = get_dimensionality(check_obj.value)
    if actual_dimensionality == dimensionality:
        return check_obj
    else:
        raise CheckError('{} has actual dimensionality of {}, not {}'.format(
            check_obj.value, actual_dimensionality, dimensionality))


# Tuples
def is_tuple(check_obj):
    try:
        assert isinstance(check_obj.value, tuple)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a tuple'.format(check_obj.value))


# List
def is_list(check_obj):
    try:
        assert isinstance(check_obj.value, list)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a list'.format(check_obj.value))
