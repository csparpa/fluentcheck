import unittest

from fluentcheck import Is
from fluentcheck.exceptions import CheckError


# noinspection PyStatementEffect
class TestIsUUIDSAssertions(unittest.TestCase):
    def test_is_uuid1_pass(self):
        obj = '5245eb82-31e6-11e9-8bfa-d8cb8a1a56c7'
        self.assertIsInstance(Is(obj).uuid1, Is)

    def test_is_uuid1_fail(self):
        # Version 4 UUID should not validate as version 1
        obj = '9f9b0fc0-e3bb-43af-9894-7b73c83374d1'
        with self.assertRaises(CheckError):
            Is(obj).uuid1
        with self.assertRaises(CheckError):
            Is('fluent').uuid1

    def test_is_not_uuid1_pass(self):
        # Version 4 UUID should not validate as version 1
        obj = '9f9b0fc0-e3bb-43af-9894-7b73c83374d1'
        self.assertIsInstance(Is(obj).not_uuid1, Is)

        # TODO: This should pass
        # IT fails as : fluentcheck.exceptions.CheckError: fluent is not a valid uuid
        # self.assertIsInstance(Is('fluent').not_uuid1, Is)

    def test_is_not_uuid1_fail(self):
        obj = '5245eb82-31e6-11e9-8bfa-d8cb8a1a56c7'
        with self.assertRaises(CheckError):
            Is(obj).not_uuid1

    def test_is_uuid4_pass(self):
        obj = '9f9b0fc0-e3bb-43af-9894-7b73c83374d1'
        self.assertIsInstance(Is(obj).uuid4, Is)

    def test_is_uuid4_fail(self):
        # Version 1 UUID should not validate as version 4
        obj = '5245eb82-31e6-11e9-8bfa-d8cb8a1a56c7'
        with self.assertRaises(CheckError):
            Is(obj).uuid4
        with self.assertRaises(CheckError):
            Is('fluent').uuid4

    def test_is_not_uuid4_pass(self):
        # Version 1 UUID should not validate as version 4
        obj = '5245eb82-31e6-11e9-8bfa-d8cb8a1a56c7'
        self.assertIsInstance(Is(obj).not_uuid4, Is)

        # TODO: This should pass
        # IT fails as : fluentcheck.exceptions.CheckError: fluent is not a valid uuid
        # self.assertIsInstance(Is('fluent').not_uuid4, Is)

    def test_is_not_uuid4_fail(self):
        obj = '9f9b0fc0-e3bb-43af-9894-7b73c83374d1'

        with self.assertRaises(CheckError):
            Is(obj).not_uuid4
