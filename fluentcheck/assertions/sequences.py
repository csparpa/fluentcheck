from ..exceptions import CheckError


def is_empty(self):
    try:
        assert len(self._val) == 0
        return self
    except:
        raise CheckError('{} is not empty'.format(self._val))


def is_not_empty(self):
    try:
        assert len(self._val) != 0
        return self
    except:
        raise CheckError('{} is empty'.format(self._val))


def is_iterable(self):
    try:
        iter(self._val)
        return self
    except TypeError:
        raise CheckError('{} is not iterable'.format(self._val))


def is_not_iterable(self):
    try:
        iter(self._val)
        raise CheckError('{} is iterable'.format(self._val))
    except TypeError:
        return self


def is_couple(self):
    self.is_iterable()
    try:
        assert len(self._val) == 2
        return self
    except AssertionError:
        raise CheckError('{} is not a sequence of 2 items'.format(self._val))


def is_triplet(self):
    self.is_iterable()
    try:
        assert len(self._val) == 3
        return self
    except AssertionError:
        raise CheckError('{} is not a sequence of 3 items'.format(self._val))


def is_nuple(self, dimension):
    self.is_iterable()
    try:
        assert len(self._val) == dimension
        return self
    except AssertionError:
        raise CheckError('{} is not a sequence of {} items'.format(self._val, dimension))


def has_dimensionality(self, dimensionality):
    self.is_not_string()

    def get_dimensionality(item):
        try:
            iter(item)
        except TypeError:
            return 0
        return 1 + get_dimensionality(item[0])

    actual_dimensionality = get_dimensionality(self._val)
    if actual_dimensionality == dimensionality:
        return self
    else:
        raise CheckError('{} has actual dimensionality of {}, not {}'.format(
            self._val, actual_dimensionality, dimensionality))


# Tuples
def is_tuple(self):
    try:
        assert isinstance(self._val, tuple)
        return self
    except AssertionError:
        raise CheckError('{} is not a tuple'.format(self._val))


# List
def is_list(self):
    try:
        assert isinstance(self._val, list)
        return self
    except AssertionError:
        raise CheckError('{} is not a list'.format(self._val))
