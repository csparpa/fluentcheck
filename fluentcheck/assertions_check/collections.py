from ..exceptions import CheckError


def is_set(check_obj):
    try:
        assert isinstance(check_obj.value, set)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not a set'.format(check_obj.value))


def is_not_set(check_obj):
    try:
        assert not isinstance(check_obj.value, set)
        return check_obj
    except AssertionError:
        raise CheckError('{} is a set'.format(check_obj.value))


def is_subset_of(check_obj, _set):
    check_obj.is_set()
    try:
        assert check_obj.value.issubset(_set)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not subset of {}'.format(check_obj.value, _set))


def is_not_subset_of(check_obj, _set):
    check_obj.is_set()
    try:
        assert not check_obj.value.issubset(_set)
        return check_obj
    except AssertionError:
        raise CheckError('{} is subset of {}'.format(check_obj.value, _set))


def is_superset_of(check_obj, _set):
    check_obj.is_set()
    try:
        assert check_obj.value.issuperset(_set)
        return check_obj
    except AssertionError:
        raise CheckError('{} is not superset of {}'.format(check_obj.value, _set))


def is_not_superset_of(check_obj, _set):
    check_obj.is_set()
    try:
        assert not check_obj.value.issuperset(_set)
        return check_obj
    except AssertionError:
        raise CheckError('{} is superset of {}'.format(check_obj.value, _set))


def intersects(check_obj, _set):
    check_obj.is_set()
    try:
        assert len(check_obj.value.intersection(_set)) != 0
        return check_obj
    except AssertionError:
        raise CheckError('{} does not intersect {}'.format(check_obj.value, _set))


def not_intersects(check_obj, _set):
    check_obj.is_set()
    try:
        assert len(check_obj.value.intersection(_set)) == 0
        return check_obj
    except AssertionError:
        raise CheckError('{} intersects {}'.format(check_obj.value, _set))

