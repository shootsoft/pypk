__author__ = 'yinjun'

import sys

from controllers.base_controller import BaseController
from controllers.controller1 import Controller1

class App(object):

    def __init__(self):
        super(App, self).__init__()
        self.name = 'Test app'

    def run(self):
        print 'App start'

        print 'Arguments are', sys.argv
        control = Controller1(self)
        print control.get_upper()
        print 'App end'

