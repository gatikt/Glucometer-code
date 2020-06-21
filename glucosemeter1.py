from __future__ import print_function

import serial
import time

ser=serial.Serial(

port='COM4',
baudrate=115200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS
)

def fix_byte(byte):
    byte = float(byte)
    return (byte / 255.) * 5.

def gluco(byte):
    return 66.896 * fix_byte(byte) ** 1.223

period = 100
try:
    while True:
        avg = ord(ser.read())
        for _ in range(period-1):
            byte = ord(ser.read())
            avg = (avg + byte) / 2
            print(end="\rvolt: {0:09.5f} rvalue: {1:09.5f} avg: {2:09.5f}".format(fix_byte(byte),gluco(byte), gluco(avg)))
        print()
except KeyboardInterrupt:
    ser.close()
    
