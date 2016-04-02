# -*- coding: utf-8 -*-

from .context import challenge

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        challenge.hmm()


if __name__ == '__main__':
    unittest.main()