# temp.py

'''This module provides logging mechanisms for the temperature sensor.'''

import csv
from datetime import datetime
import os
import time


class Temperature:

    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        self.base_dir = '/sys/bus/w1/devices/28-012063cb3e94'
        self.device_file = self.base_dir + '/w1_slave'

    def read_temp(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        equals_pos = lines[1].find('t=')
        temp_raw = lines[1][equals_pos + 2:]
        return int(temp_raw)

    def convert_temp(self, temp_raw):
        temp_c = int(temp_raw) / 1000
        temp_f = (temp_c * (9 / 5)) + 32
        return {'T': time.time(), 'C': temp_c, 'F': temp_f}

    def write(self):
        temp_raw = self.read_temp()
        temps = self.convert_temp(temp_raw)
        print(temps)
        with open('temps-hot.csv', 'a') as f:
            fieldnames = ['T', 'C', 'F']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(temps)
