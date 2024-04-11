import unittest
import test_login


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [test_login.LoginTestCases]

    for test in tests:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))
    unittest.main(verbosity=2).run(suite)
