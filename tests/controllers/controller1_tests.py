__author__ = 'yinjun'

import unittest

from pktest.main import App
from pktest.libs.lib1 import Lib1
from pktest.controllers.controller1 import Controller1

class Controller1Tests(unittest.TestCase):

    def test_upper(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        app = App()
        control = Controller1(app)
        actual = control.get_upper()
        self.assertEqual(actual, 'TEST APP')


if __name__ == '__main__':
    unittest.main()