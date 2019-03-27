from ..check import Check
from ..exceptions import CheckError


def is_latitude(self):
    self.is_real()
    try:
        self.is_between(-90.0, 90.0)
        return self
    except AssertionError:
        raise CheckError('{} is not a valid latitude'.format(self._val))


def is_longitude(self):
    self.is_real()
    try:
        self.is_between(-180.0, 180.0)
        return self
    except AssertionError:
        raise CheckError('{} is not a valid longitude'.format(self._val))


def is_azimuth(self):
    try:
        self.is_number().is_positive()
    except:
        raise CheckError('{} is not a valid azimuth'.format(self._val))


def is_geopoint(self):
    self.is_couple()
    try:
        first = Check(self._val[0])
        first.is_long()
        second = Check(self._val[1])
        second.is_latitude()
    except AssertionError:
        raise CheckError('{} is not a valid geographic point'.format(self._val))
