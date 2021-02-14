import unittest
from coverage import Coverage
import sys
import os
import test

if __name__ == '__main__':
    # the directory change is done to ease the use of relative
    # paths in the unit tests
    os.chdir("./tests")
    sys.path.append(os.getcwd())

    suite = unittest.TestSuite()
    cov = Coverage()
    cov.start()

    for test in unittest.TestLoader().discover("test"):
        suite.addTest(test)
    unittest.TextTestRunner(verbosity=2).run(suite)

    cov.stop()
    cov.save()
    cov.report(show_missing=True, omit=['test_*.py', '*/__init__.py'])
