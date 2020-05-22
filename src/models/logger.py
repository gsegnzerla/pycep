import json
import os


class Logger(object):
    PATH = os.environ["HOME"] + '/.config/pycep/'
    FILEPATH = PATH + 'pycep.log'

    def create(self):
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)
            with open(self.FILEPATH, 'w'):
                ...

    def clear(self):
        if os.path.exists(self.FILEPATH):
            os.remove(self.FILEPATH)
