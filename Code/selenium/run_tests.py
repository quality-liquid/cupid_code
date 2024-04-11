import unittest

import utils
import test_login
import test_cupid



if __name__ == '__main__':
    utils.db_backup()
    suite = unittest.TestSuite()
    tests = [test_login.LoginTestCases, test_cupid.CupidTestCases, ]

    for test in tests:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))
    unittest.TextTestRunner(verbosity=2).run(suite)
    utils.db_restore()
