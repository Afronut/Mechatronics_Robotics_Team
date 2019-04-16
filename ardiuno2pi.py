from serial import Serial
import time
ser = Serial('/dev/ttyUSB0', 9600)

line = ser.write('up')
sleep(1)
line= ser.readline()
print(line)
