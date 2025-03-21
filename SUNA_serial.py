# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 16:01:24 2025

@author: jeff

Current issues - for unclear reasons the output isn't parsed correctly.  This
code executes a workaround, but would be good to have EOL correctly recognized.

"""

## run as python3 SUNA_serial.py COMX
## set output directory (to Dropbox) before running

dir_out = './'

import serial
import time
from datetime import datetime
import sys

if len(sys.argv) == 1:
    com = 'COM7'
else:
    com = sys.argv[1]

#### working block

ser = serial.Serial(port=com, baudrate=57600, xonxoff=True, timeout = 10)

ser.write('status'.encode('utf-8'))
time.sleep(1)
ser.write('measure 5'.encode('utf-8'))
time.sleep(30)
data = ser.readlines()
    
ser.close()

data = list(map(str, data))

## where does data start?

for i,j in enumerate(data):
    if 'SATSDF1921' in j:
        print(i)
        start_i = i
        
## split data on EOL

clean_data = []

now = datetime.now()
now = now.strftime("%Y%m%d_%H%M%S")

with open(dir_out + now + '_SUNA.txt', 'w') as data_out:
    for i in range(start_i, (start_i + 6)):
        item = data[i]
        item = item.strip('b\'CMD?measure')
        item = item.strip()
        item = item.rstrip()
        item = item.strip('\\r\\n')
        item = item.strip('\r\n')
        item = item.replace('5SATSDF', 'SATSDF')
        item = item + '\n'
        #item = item.split(',')
        clean_data.append(item)
        data_out.writelines(item)
    
