import requests
import sys


def try_request(func):
    def _inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:
            print(e)
            sys.exit(1)
            
    return _inner
