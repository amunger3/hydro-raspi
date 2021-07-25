# main.py

'''This module provides access to the main sensor functions.'''

import time

from temp import Temperature


if __name__ == '__main__':
    t = Temperature()
    while True:
        t.write()
        time.sleep(10)