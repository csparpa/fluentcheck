from ..exceptions import CheckError


def is_boolean(self):
    try:
        assert isinstance(self._val, bool)
        return self
    except AssertionError:
        raise CheckError('{} is not boolean'.format(self._val))


def is_not_boolean(self):
    try:
        assert not isinstance(self._val, bool)
        return self
    except AssertionError:
        raise CheckError('{} is boolean'.format(self._val))


def is_truthy(self):
    try:
        assert self._val
        return self
    except AssertionError:
        raise CheckError('{} is falsy'.format(self._val))


def is_falsy(self):
    try:
        assert not self._val
        return self
    except AssertionError:
        raise CheckError('{} is truthy'.format(self._val))


def is_not_truthy(self):
    self.is_falsy()


def is_not_falsy(self):
    self.is_truthy()


def is_true(self):
    self.is_boolean()
    self.is_truthy()


def is_false(self):
    self.is_boolean()
    self.is_falsy()


def is_not_true(self):
    self.is_false()


def is_not_false(self):
    self.is_true()


def has_same_truth_of(self, value):
    try:
        assert bool(self._val) == bool(value)
        return self
    except AssertionError:
        raise CheckError('{} has a different truth of {}'.format(self._val,
                                                                 value))


def has_opposite_truth_of(self, value):
    try:
        assert bool(self._val) != bool(value)
        return self
    except AssertionError:
        raise CheckError('{} has the same truth of {}'.format(self._val,
                                                              value))