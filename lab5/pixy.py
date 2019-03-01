
#!/usr/bin/python

import smbus
import time

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x54


while True:
    word = bus.read_byte_data(DEVICE_ADDRESS, 0)
    print 'word2 is {}'.format(hex(word))
    word1 = bus.read_byte_data(DEVICE_ADDRESS, 1)
    print 'word1 is {}'.format(hex(word1))
    time.sleep(0.1)
    
