__author__ = 'yinjun'

import unittest

from pktest.main import App
from pktest.libs.lib1 import Lib1

class Lib1Tests(unittest.TestCase):

    def test_upper(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        #app = App()
        lib1 = Lib1()
        actual = lib1.upper('foo')
        self.assertEqual(actual, 'FOO')


if __name__ == '__main__':
    unittest.main()