import os
import json


class Logger(object):

    PATH = os.environ["HOME"] + '/.config/pycep/'
    FILEPATH = PATH + 'pycep.log'

    def store(self, _dict):
        with open(self.FILEPATH, 'a') as file:
            json.dump(_dict, file, indent=4)

    def create(self):
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)
            with open(self.FILEPATH, 'w'):
                ...

    def clear(self):
        if os.path.exists(self.FILEPATH):
            os.remove(self.FILEPATH)
