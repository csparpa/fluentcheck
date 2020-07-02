import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class TestSequencesAssertions(unittest.TestCase):
    def test_is_empty(self):
        res = Check('').is_empty()
        self.assertIsInstance(res, Check)
        res2 = Check([]).is_empty()
        self.assertIsInstance(res2, Check)
        res3 = Check(()).is_empty()
        self.assertIsInstance(res3, Check)
        with self.assertRaises(CheckError):
            Check('abc').is_empty()

    def test_is_not_empty(self):
        res = Check('123').is_not_empty()
        self.assertIsInstance(res, Check)
        with self.assertRaises(CheckError):
            Check([]).is_not_empty()

    def test_is_iterable(self):
        res = Check(range(6)).is_iterable()
        self.assertIsInstance(res, Check)
        res2 = Check([1, 2, 3]).is_iterable()
        self.assertIsInstance(res2, Check)
        with self.assertRaises(CheckError):
            Check(8).is_iterable()

    def test_is_not_iterable(self):
        res = Check(1).is_not_iterable()
        self.assertIsInstance(res, Check)
        with self.assertRaises(CheckError):
            Check([1, 2, 3]).is_not_iterable()

    def test_is_couple(self):
        res = Check([1, 2]).is_couple()
        self.assertIsInstance(res, Check)
        res2 = Check(('1', '2')).is_couple()
        self.assertIsInstance(res2, Check)
        with self.assertRaises(CheckError):
            Check([1, 2, 3]).is_couple()

    def test_is_triplet(self):
        res = Check([1, 2, 3]).is_triplet()
        self.assertIsInstance(res, Check)
        res2 = Check({'a': 1, 'b': 2, 'c': 3}).is_triplet()
        self.assertIsInstance(res, Check)
        with self.assertRaises(CheckError):
            Check([1, 2]).is_triplet()

    def test_is_nuple(self):
        obj = 1, 2, 3, 4, 5
        res = Check(obj).is_nuple(5)
        self.assertIsInstance(res, Check)
        with self.assertRaises(CheckError):
            Check((1, 2)).is_nuple(4)

    def test_has_dimensionality(self):
        obj = [[1, 2], [3, 4]]
        res = Check(obj).has_dimensionality(2)
        self.assertIsInstance(res, Check)
        obj = [1, 2, 3]
        with self.assertRaises(CheckError):
            Check(obj).has_dimensionality(3)

    def test_is_tuple(self):
        res = Check(('a', 'b', 'c')).is_tuple()
        self.assertIsInstance(res, Check)
        res2 = Check((1, (1, 2), 2)).is_tuple()
        self.assertIsInstance(res2, Check)
        with self.assertRaises(CheckError):
            Check([]).is_tuple()

    def test_is_list(self):
        res = Check([10, 9, 8]).is_list()
        self.assertIsInstance(res, Check)
        res2 = Check([]).is_list()
        self.assertIsInstance(res2, Check)
        with self.assertRaises(CheckError):
            Check((1, 2)).is_list()

