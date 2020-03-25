import unittest

from fluentcheck import Is


class TestIsChainClosure(unittest.TestCase):
    def test_chain_closure_with(self):
        # avoid linter issues like PyStatementEffect
        Is(.5).not_none.number.truthy()

    def test_chain_closure_without(self):
        # Has linter issues like PyStatementEffect
        Is(.5).not_none.number.truthy
