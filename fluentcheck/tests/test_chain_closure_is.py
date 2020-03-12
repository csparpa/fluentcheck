import unittest

from fluentcheck import Is
from fluentcheck.check import CheckError


class TestIsChainClosure(unittest.TestCase):
    def test_chain_closure_with(self):
        # avoid linter issues like PyStatementEffect
        n = .5
        Is(n).not_none.number.truthy()

    def test_chain_closure_without(self):
        # Has linter issues like PyStatementEffect
        n = .5
        Is(n).not_none.number.truthy
