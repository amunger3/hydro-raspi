import os
# import glob
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/28-012063cb3e94'
# device_folder = glob.glob(base_dir + '28*')[0]
device_file = base_dir + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    equals_pos = lines[1].find('t=')
    temp_raw = lines[1][equals_pos + 2:]
    temp_c = int(temp_raw) / 1000
    temp_f = (temp_c * (9 / 5)) + 32
    print('Temperature: {0} deg. C --- {1} deg. F'.format(temp_c, temp_f))
    return lines


while True:
    read_temp_raw()
    time.sleep(1)
