import unittest

from fluentcheck import Is
from fluentcheck.exceptions import CheckError


# noinspection PyStatementEffect
class TestIsFileFormatAssertions(unittest.TestCase):

    def test_is_json_pass(self):
        obj = '{"name": "pass"}'
        self.assertIsInstance(Is(obj).json, Is)

    def test_is_json_fail(self):
        obj = "goodbye"
        with self.assertRaises(CheckError):
            Is(obj).json

    def test_is_not_json_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).not_json, Is)

    def test_is_not_json_fail(self):
        obj = '{"name": "pass"}'
        with self.assertRaises(CheckError):
            Is(obj).not_json

    def test_is_yaml_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).yaml, Is)

    def test_is_yaml_fail(self):
        obj = "xxx: {"
        with self.assertRaises(CheckError):
            Is(obj).yaml

    def test_is_not_yaml_pass(self):
        obj = "xxx: {"
        self.assertIsInstance(Is(obj).not_yaml, Is)

    def test_is_not_yaml_fail(self):
        obj = """
     ---
      doe: "a deer, a female deer"
      calling-birds:
        - louie
        - fred
     """.strip()
        with self.assertRaises(CheckError):
             Is(obj).not_yaml

    def test_is_xml_pass(self):
        obj = """<Agenda>
     <type>gardening</type>
     <Activity>
       <type>cooking</type>
     </Activity>
    </Agenda>"""
        self.assertIsInstance(Is(obj).xml, Is)

    def test_is_xml_fail(self):
        obj = "not xml"
        with self.assertRaises(CheckError):
            Is(obj).xml

    def test_is_not_xml_pass(self):
        obj = "Hello world"
        self.assertIsInstance(Is(obj).not_xml, Is)

    def test_is_not_xml_fail(self):
        obj = """<Agenda></Agenda>"""
        with self.assertRaises(CheckError):
            Is(obj).not_xml

