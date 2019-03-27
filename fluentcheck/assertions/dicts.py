from ..exceptions import CheckError


def is_dict(self):
    try:
        assert isinstance(self._val, dict)
        return self
    except AssertionError:
        raise CheckError('{} is not a dict'.format(self._val))


def is_not_dict(self):
    try:
        assert not isinstance(self._val, dict)
        return self
    except AssertionError:
        raise CheckError('{} is a dict'.format(self._val))


def has_keys(self, *args):
    self.is_dict()
    cur_key = ''
    try:
        for key in args:
            cur_key = key
            assert key in self._val
        return self
    except AssertionError:
        raise CheckError('{} does not contain key: {}'.format(self._val,
                                                              cur_key))


def has_not_keys(self, *args):
    self.is_dict()
    cur_key = ''
    try:
        for key in args:
            cur_key = key
            assert not key in self._val
        return self
    except AssertionError:
        raise CheckError('{} does contains key: {}'.format(self._val, cur_key))
