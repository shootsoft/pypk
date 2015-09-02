__author__ = 'yinjun'

class BaseController(object):

    def __init__(self, app):
        super(BaseController, self).__init__()
        self.app = app

