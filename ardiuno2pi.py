from serial import Serial
ser = Serial('/dev/ttyUSB0', 9600)

line = ser.write('up')
print(line)
