import unittest

import utils
import test_login
import test_cupid
import test_dater


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [test_login.LoginTestCases, test_cupid.CupidTestCases, test_dater.DaterTestCases]

    for test in tests:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))
    unittest.TextTestRunner(verbosity=2).run(suite)
