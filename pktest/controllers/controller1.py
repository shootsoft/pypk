__author__ = 'yinjun'

from base_controller import BaseController
from pktest.libs.lib1 import Lib1

class Controller1(BaseController):

    def __init__(self, app):
        super(Controller1, self).__init__(app)
        self.lib = Lib1()

    def get_upper(self):
        return self.lib.upper(self.app.name)