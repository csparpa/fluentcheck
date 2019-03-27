from ..check import Check
from ..exceptions import CheckError
from uuid import UUID


def is_uuid1(self):
    try:
        assert (UUID(self.value).version == 1)
        return self
    except (AssertionError, AttributeError, ValueError) as e:
        raise CheckError('{} is not a valid uuid1 exception: {}'.format(self._val, e))


def is_not_uuid1(self):
    try:
        assert UUID(self._val).version != 1
        return self
    except ValueError:  # self._val is not a UUID at all
        raise CheckError('{} is not a valid uuid'.format(self._val))
    except:  # self._val is a UUID, but is indeed v1
        raise CheckError('{} is a uuid1'.format(self._val))


def is_uuid4(self):
    try:
        assert (UUID(self.value).version == 4)
        return self
    except (AssertionError, AttributeError, ValueError):
        raise CheckError('{} is not a valid uuid4'.format(self._val))


def is_not_uuid4(self):
    try:
        assert UUID(self._val).version != 4
        return self
    except ValueError:  # self._val is not a UUID at all
        raise CheckError('{} is not a valid uuid'.format(self._val))
    except:  # self._val is a UUID, but is indeed v4
        raise CheckError('{} is a uuid4'.format(self._val))
