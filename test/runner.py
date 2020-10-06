"""
    Run all unit test in sequence.
"""

import unittest

# import your test modules
import test_color
import test_card
import test_cards
import test_hand
import test_deck

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_color))
suite.addTests(loader.loadTestsFromModule(test_card))
suite.addTests(loader.loadTestsFromModule(test_cards))
suite.addTests(loader.loadTestsFromModule(test_hand))
suite.addTests(loader.loadTestsFromModule(test_deck))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
