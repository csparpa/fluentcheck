import unittest
from fluentcheck.classes import Check
from fluentcheck.exceptions import CheckError


class BooleanObject:
    def __init__(self, is_true):
        self.is_true = is_true
    def __bool__(self):
        return self.is_true


class BooleanByLengthObject:

	def __init__(self, items = None):
		self.items = [] if items is None else items
	def __len__(self):
		return len(self.items)


class TestBooleansAssertions(unittest.TestCase):

    def setUp(self):
        self.falsy_values = ([], (), {}, set(), "", '',
                             range(0), 0, 0.0, 0j, None, False,
                             BooleanObject(False), BooleanByLengthObject())
        self.truthy_values = ([1,], ('a',), {1:'one'}, {1,1,}, "1", '2',
                             range(1), 1, 1.0, 1j, not None, True,
                             BooleanObject(True), BooleanByLengthObject([1,2]))

    def test_is_boolean(self):
        res = Check(1 == 2).is_boolean()
        self.assertIsInstance(res, Check)
        try:
            Check(1).is_boolean()
            self.fail()
        except CheckError:
            pass

    def test_is_not_boolean(self):
        res = Check(1).is_not_boolean()
        self.assertIsInstance(res, Check)
        try:
            Check(1 == 2).is_not_boolean()
            self.fail()
        except CheckError:
            pass

    def test_is_true(self):
        res = Check(1 == 1).is_true()
        self.assertIsInstance(res, Check)
        try:
            Check(1 == 2).is_true()
            self.fail()
        except CheckError:
            pass

    def test_is_not_true(self):
        res = Check(1 == 2).is_not_true()
        self.assertIsInstance(res, Check)
        try:
            Check(1 == 1).is_not_true()
            self.fail()
        except CheckError:
            pass

    def test_is_false(self):
        res = Check(1 == 2).is_false()
        self.assertIsInstance(res, Check)
        try:
            Check(1 == 1).is_false()
            self.fail()
        except CheckError:
            pass

    def test_is_not_false(self):
        res = Check(1 == 1).is_not_false()
        self.assertIsInstance(res, Check)
        try:
            Check(1 == 2).is_not_false()
            self.fail()
        except CheckError:
            pass

    def test_is_falsy(self):
        for item in self.falsy_values:
            res = Check(item).is_falsy()
            self.assertIsInstance(res, Check)
            try:
                Check(not item).is_falsy()
                self.fail()
            except CheckError:
                pass

    def test_is_not_falsy(self):
        for item in self.falsy_values:
            res = Check(not item).is_not_falsy()
            self.assertIsInstance(res, Check)
            try:
                Check(item).is_not_falsy()
                self.fail()
            except CheckError:
                pass

    def test_is_truthy(self):
        for item in self.truthy_values:
            res = Check(item).is_truthy()
            self.assertIsInstance(res, Check)
            try:
                Check(not item).is_truthy()
                self.fail()
            except CheckError:
                pass

    def test_is_not_truthy(self):
        for item in self.truthy_values:
            res = Check(not item).is_not_truthy()
            self.assertIsInstance(res, Check)
            try:
                Check(item).is_not_truthy()
                self.fail()
            except CheckError:
                pass
    
    def test_has_same_truth_of(self):
        res = Check(BooleanObject(True)).has_same_truth_of(BooleanByLengthObject([1,2]))
        self.assertIsInstance(res, Check)
        try:
            Check(BooleanObject(False)).has_same_truth_of(BooleanByLengthObject([1,2]))
            self.fail()
        except CheckError:
            pass

    def test_has_opposite_truth_of(self):
        res = Check(BooleanObject(False)).has_opposite_truth_of(BooleanByLengthObject([1,]))
        self.assertIsInstance(res, Check)
        try:
            Check(BooleanObject(False)).has_opposite_truth_of(BooleanByLengthObject())
            self.fail()
        except CheckError:
            pass
