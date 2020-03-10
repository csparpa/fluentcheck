import unittest

from fluentcheck import Is
from fluentcheck.check import Check, CheckError
from fluentcheck.tests.test_type_hierarchy import ParentA, Child, GrandChild, ParentB, ChildOfMultipleParents


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
