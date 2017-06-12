class CheckError(Exception):
    pass


class Check:

    NUMERIC_TYPES = (int, long, float, complex)

    def __init__(self, value):
        self._val = value

    # Nonethiness

    def is_none(self):
        try:
            assert self._val is None
            return self
        except AssertionError:
            raise CheckError('{} is not None'.format(self._val))

    def is_not_none(self):
        try:
            assert self._val is not None
            return self
        except AssertionError:
            raise CheckError('{} is None'.format(self._val))

    # Numbers

    def is_number(self):
        try:
            assert isinstance(self._val, self.NUMERIC_TYPES)
            return self
        except AssertionError:
            raise CheckError('{} is not a number'.format(self._val))

    def is_not_number(self):
        try:
            assert not isinstance(self._val, self.NUMERIC_TYPES)
            return self
        except AssertionError:
            raise CheckError('{} is a number'.format(self._val))

    def is_integer(self):
        try:
            assert isinstance(self._val, int)
            return self
        except AssertionError:
            raise CheckError('{} is not integer'.format(self._val))

    def is_not_integer(self):
        try:
            assert not isinstance(self._val, int)
            return self
        except AssertionError:
            raise CheckError('{} is integer'.format(self._val))

    def is_long(self):
        try:
            assert isinstance(self._val, long)
            return self
        except AssertionError:
            raise CheckError('{} is not long'.format(self._val))

    def is_not_long(self):
        try:
            assert not isinstance(self._val, long)
            return self
        except AssertionError:
            raise CheckError('{} is long'.format(self._val))

    def is_float(self):
        try:
            assert isinstance(self._val, float)
            return self
        except AssertionError:
            raise CheckError('{} is not float'.format(self._val))

    def is_not_float(self):
        try:
            assert not isinstance(self._val, float)
            return self
        except AssertionError:
            raise CheckError('{} is float'.format(self._val))

    def is_complex(self):
        try:
            assert isinstance(self._val, complex)
            return self
        except AssertionError:
            raise CheckError('{} is not complex'.format(self._val))

    def is_not_complex(self):
        try:
            assert not isinstance(self._val, complex)
            return self
        except AssertionError:
            raise CheckError('{} is complex'.format(self._val))


    # Strings

    # TBD

if __name__ == '__main__':
    val = 6j+5
    Check(val).is_not_none().is_complex().is_number()