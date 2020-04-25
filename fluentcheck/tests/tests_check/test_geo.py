import unittest

from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestStringsAssertions(unittest.TestCase):

    def test_is_latitude(self):
        res = Check(20).is_latitude()
        self.assertIsInstance(res, Check)
        try:
            Check(120).is_latitude()
            self.fail()
        except CheckError:
            pass

    def test_is_negative_latitude(self):
        res = Check(-20).is_latitude()
        self.assertIsInstance(res, Check)
        try:
            Check(-120).is_latitude()
            self.fail()
        except CheckError:
            pass

    def test_is_longitude(self):
        res = Check(20).is_longitude()
        self.assertIsInstance(res, Check)
        try:
            Check(181).is_longitude()
            self.fail()
        except CheckError:
            pass

    def test_is_negative_longitude(self):
        res = Check(-30).is_longitude()
        self.assertIsInstance(res, Check)
        try:
            Check(-300).is_longitude()
            self.fail()
        except CheckError:
            pass

    def test_is_azimuth(self):
        res = Check(10).is_azimuth()
        self.assertIsInstance(res, Check)
        try:
            Check(-360).is_azimuth()
            self.fail()
        except CheckError:
            pass

    def test_is_geopoint(self):
        res = Check((120, 70)).is_geopoint()
        self.assertIsInstance(res, Check)
        try:
            Check((-360, -120)).is_geopoint()
            self.fail()
        except CheckError:
            pass
