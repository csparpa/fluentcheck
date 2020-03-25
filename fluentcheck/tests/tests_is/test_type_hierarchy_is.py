import unittest

from fluentcheck import Is
from fluentcheck.exceptions import CheckError
from fluentcheck.tests.tests_check.test_type_hierarchy import ParentA, Child, ParentB, ChildOfMultipleParents


class TestIsTypeHierarchy(unittest.TestCase):

    def test_is_subtype_of_pass(self):
        obj = Child()
        self.assertIsInstance(Is(obj).subtype_of(ParentA), Is)

    def test_is_subtype_of_fail(self):
        obj = ParentA()
        with self.assertRaises(CheckError):
            Is(obj).subtype_of(Child)

    def test_is_subtype_of_when_multiple_inheritance_pass(self):
        obj = ChildOfMultipleParents()
        self.assertIsInstance(Is(obj).subtype_of((ParentA, ParentB)), Is)

    def test_is_subtype_of_when_multiple_inheritance_fail(self):
        obj = ParentA()
        with self.assertRaises(CheckError):
            Is(obj).subtype_of((ChildOfMultipleParents, ParentB))

    def test_is_not_subtype_of_pass(self):
        obj = ParentA()
        self.assertIsInstance(Is(obj).not_subtype_of(ParentB), Is)

    def test_is_not_subtype_of_fail(self):
        obj = Child()
        with self.assertRaises(CheckError):
            Is(obj).not_subtype_of(ParentA)

    def test_is_not_subtype_of_itself_pass(self):
        obj = Child()
        self.assertIsInstance(Is(obj).subtype_of(Child), Is)

    def test_is_not_subtype_of_itself_fail(self):
        obj = Child()
        with self.assertRaises(CheckError):
            Is(obj).not_subtype_of(Child)

    def test_is_subtype_of_atleast_one_parent_pass(self):
        obj = Child()
        self.assertIsInstance(Is(obj).subtype_of((ParentA, ParentB)), Is)

    def test_is_subtype_of_atleast_one_parent_fail(self):
        obj = Child()
        with self.assertRaises(CheckError):
            Is(obj).not_subtype_of((ParentA, ParentB))

    def test_of_type(self):
        obj = 'string'
        self.assertIsInstance(Is(obj).of_type(str), Is)
        try:
            Is(obj).of_type(int)
            self.fail()
        except CheckError:
            pass

    def test_not_of_type(self):
        obj = 123
        self.assertIsInstance(Is(obj).not_of_type(str), Is)
        try:
            Is(obj).not_of_type(int)
            self.fail()
        except CheckError:
            pass

    def test_module(self):
        self.assertIsInstance(Is(unittest).module, Is)
        try:
            Is(123).module()
            self.fail()
        except CheckError:
            pass

    def test_not_module(self):
        self.assertIsInstance(Is(123).not_module, Is)
        try:
            self.assertIsInstance(Is(unittest).not_module, Is)
            self.fail()
        except CheckError:
            pass

    def test_runnable(self):
        obj = lambda x: x + 1
        self.assertIsInstance(Is(obj).runnable, Is)
        try:
            Is(123).runnable
            self.fail()
        except CheckError:
            pass

    def test_not_runnable(self):
        obj = lambda x: x + 1
        self.assertIsInstance(Is(123).not_runnable, Is)
        try:
            Is(obj).not_runnable
            self.fail()
        except CheckError:
            pass
