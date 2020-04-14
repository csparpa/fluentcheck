import unittest

from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestFileFormatAssertions(unittest.TestCase):
    # noinspection PyUnresolvedReferences
    def test_is_yaml(self):
        res = Check("hello").is_yaml()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_yaml()
            self.fail()
        except CheckError:
            pass

    # noinspection PyUnresolvedReferences
    def test_is_not_yaml(self):
        res = Check("xxx: {").is_not_yaml()
        self.assertIsInstance(res, Check)
        try:
            Check("valid_yaml").is_not_yaml()
            self.fail()
        except CheckError:
            pass

    # noinspection PyUnresolvedReferences
    def test_is_xml(self):
        obj = """<Agenda>
     <type>gardening</type>
     <Activity>
       <type>cooking</type>
     </Activity>
    </Agenda>"""
        res = Check(obj).is_xml()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_xml()
            self.fail()
        except CheckError:
            pass

    # noinspection PyUnresolvedReferences
    def test_is_not_xml(self):
        res = Check('[123]').is_not_xml()
        self.assertIsInstance(res, Check)
        try:
            Check("<Agenda>ok</Agenda>").is_not_xml()
            self.fail()
        except CheckError:
            pass

    # noinspection PyUnresolvedReferences
    def test_is_json_pass(self):
        obj = '{"name": "pass"}'
        self.assertIsInstance(Check(obj).is_json(), Check)

    # noinspection PyUnresolvedReferences
    def test_is_json_fail(self):
        obj = "goodbye"
        with self.assertRaises(CheckError):
            Check(obj).is_json()

    # noinspection PyUnresolvedReferences
    def test_is_not_json_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Check(obj).is_not_json(), Check)

    # noinspection PyUnresolvedReferences
    def test_is_not_json_fail(self):
        obj = '{"name": "pass"}'
        with self.assertRaises(CheckError):
            Check(obj).is_not_json()
