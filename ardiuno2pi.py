from serial import Serial
from time import sleep
ser = Serial('/dev/ttyUSB0', 9600)

line = ser.write(b'up')
sleep(1)
while True:
 ser.write(b'down')
  line= ser.readline()
  print(line)
  sleep(2)
