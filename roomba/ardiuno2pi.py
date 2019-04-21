from time import sleep
from serial import Serial
port = Serial('/dev/ttyUSB0', 9600)


def send_arduino_message(msg):
    port.write(b'{}'.format(msg))
    sleep(5)
    Serial.flush()
    line = port.readline()
    print(line)
    sleep(2)
