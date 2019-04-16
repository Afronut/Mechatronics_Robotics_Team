from serial import Serial
from time import sleep
ser = Serial('/dev/ttyUSB0', 9600)

line = ser.write(b'up')
sleep(1)
while True:
  line = ser.write(b'up')
  line= ser.readline()
  print(line)
  sleep(2)
