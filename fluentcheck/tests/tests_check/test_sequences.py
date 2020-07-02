import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestSequencesAssertions(unittest.TestCase):
    def test_is_empty(self):
        res = Check('').is_empty()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_empty()
            self.fail()
        except CheckError:
            pass

    def test_is_not_empty(self):
        res = Check('123').is_not_empty()
        self.assertIsInstance(res, Check)
        try:
            Check([]).is_not_empty()
            self.fail()
        except CheckError:
            pass

    def test_is_iterable(self):
        res = Check(range(6)).is_iterable()
        self.assertIsInstance(res, Check)
        res2 = Check([1, 2, 3]).is_iterable()
        self.assertIsInstance(res2, Check)
        try:
            Check(8).is_iterable()
            self.fail()
        except CheckError:
            pass

    def test_is_not_iterable(self):
        res = Check(1).is_not_iterable()
        self.assertIsInstance(res, Check)
        try:
            Check([1, 2, 3]).is_not_iterable()
            self.fail()
        except CheckError:
            pass

    def test_is_couple(self):
        res = Check([1, 2]).is_couple()
        self.assertIsInstance(res, Check)
        res2 = Check(('1', '2')).is_couple()
        self.assertIsInstance(res2, Check)
        try:
            Check([1, 2, 3]).is_couple()
            self.fail()
        except CheckError:
            pass

        try:
            Check(10).is_couple()
            self.fail()
        except CheckError:
            pass

    def test_is_triplet(self):
        res = Check([1, 2, 3]).is_triplet()
        self.assertIsInstance(res, Check)
        res2 = Check({'a': 1, 'b': 2, 'c': 3}).is_triplet()
        self.assertIsInstance(res, Check)
        try:
            Check([1, 2]).is_triplet()
            self.fail()
        except CheckError:
            pass

        try:
            Check({'a': 1, 'b': 2, 'c': 3, 'd': 4}).is_triplet()
            self.fail()
        except CheckError:
            pass

    def test_is_nuple(self):
        obj = 1, 2, 3, 4, 5
        res = Check(obj).is_nuple(5)
        self.assertIsInstance(res, Check)
        try:
            Check((1, 2)).is_nuple(3)
            self.fail()
        except CheckError:
            pass

    def test_has_demensionality(self):
        obj = [[1, 2], [3, 4]]
        res = Check(obj).has_demensionality(2)
        self.assertIsInstance(res, Check)
        obj = [1, 2, 3]
        try:
            Check(obj).has_demensionality(3)
            self.fail()
        except CheckError:
            pass

    def test_is_tuple(self):
        res = Check(('a', 'b', 'c')).is_tuple()
        self.assertIsInstance(res, Check)
        res2 = Check((1, (1, 2), 2)).is_tuple()
        self.assertIsInstance(res2, Check)
        try:
            Check([1, 2, 3]).is_tuple()
            self.fail()
        except CheckError:
            pass

    def test_is_list(self):
        res = Check([10, 9, 8]).is_list()
        self.assertIsInstance(res, Check)
        res2 = Check([]).is_list()
        res2.assertIsInstance(res2, Check)
        try:
            Check((1, 2, 3)).is_list()
            self.fail()
        except CheckError:
            pass

        try:
            Check('not list').is_list()
            self.fail()
        except CheckError:
            pass

