import unittest

from fluentcheck import Is
from fluentcheck.exceptions import CheckError


# noinspection PyStatementEffect
class TestIsGeoAssertions(unittest.TestCase):

    def test_is_latitude_pass(self):
        self.assertIsInstance(Is(20).latitude, Is)

    def test_is_latitude_fail(self):
        with self.assertRaises(CheckError):
            Is(120).latitude

    def test_is_negative_latitude_pass(self):
        self.assertIsInstance(Is(-20).latitude, Is)

    def test_is_negative_latitude_fail(self):
        with self.assertRaises(CheckError):
            Is(-120).latitude

    def test_is_longitude_pass(self):
        self.assertIsInstance(Is(20).longitude, Is)

    def test_is_longitude_fail(self):
        with self.assertRaises(CheckError):
            Is(181).longitude

    def test_is_negative_longitude_pass(self):
        self.assertIsInstance(Is(-30).longitude, Is)

    def test_is_negative_longitude_fail(self):
        with self.assertRaises(CheckError):
            Is(-300).longitude

    def test_is_azimuth_pass(self):
        self.assertIsInstance(Is(10).azimuth, Is)

    def test_is_azimuth_fail(self):
        with self.assertRaises(CheckError):
            Is(-360).azimuth

    def test_is_geopoint_pass(self):
        self.assertIsInstance(Is((120, 70)).geopoint, Is)

    def test_is_geopoint_fail(self):
        with self.assertRaises(CheckError):
            Is((-360, -120)).geopoint
