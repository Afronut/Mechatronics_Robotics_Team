import RPi.GPIO as GPIO
import time
import socket
import barcode_reader as br

HOST = '10.0.0.215'  # Enter IP or Hostname of your server
# Pick 345an open Port (1000+ recommended), must match the server port
PORT = 12397  # new comment
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Import required modules


def forward():
    GPIO.setwarnings(False)

    # Declare the GPIO settings
    GPIO.setmode(GPIO.BCM)

    # set up GPIO pins
    GPIO.setup(5, GPIO.OUT)  # Connected to AIN2
    GPIO.setup(6, GPIO.OUT)  # Connected to AIN1
    GPIO.setup(13, GPIO.OUT)  # Connected to STBY
    GPIO.setup(18, GPIO.OUT)  # Connected to PWMA
    # Thread(target=run_server).start()
    pwm = GPIO.PWM(18, 1000)
    # Drive the motor clockwise
    GPIO.output(6, GPIO.HIGH)  # Set AIN1
    GPIO.output(5, GPIO.LOW)  # Set AIN2

    # Set the motor speed
    # GPIO.output(18, GPIO.HIGH) # Set PWMA
    pwm.start(50)

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(22)
    # GPIO.output(18, GPIO.LOW) # Set PWMA
    # time.sleep(2.5)
    # # pwm = GPIO.PWM(18, 1000)
    # pwm.start(50)
    pwm.stop()
    GPIO.output(6, GPIO.LOW)  # Set AIN1
    GPIO.output(5, GPIO.LOW)  # Set AIN2
    pwm.stop()
    GPIO.output(13, GPIO.LOW)  # Set STBY
    GPIO.cleanup()


def backward():
    GPIO.setwarnings(False)

    # Declare the GPIO settings
    GPIO.setmode(GPIO.BCM)

    # set up GPIO pins
    GPIO.setup(5, GPIO.OUT)  # Connected to AIN2
    GPIO.setup(6, GPIO.OUT)  # Connected to AIN1
    GPIO.setup(13, GPIO.OUT)  # Connected to STBY
    GPIO.setup(18, GPIO.OUT)  # Connected to PWMA
    # Thread(target=run_server).start()
    pwm = GPIO.PWM(18, 1000)
    # Drive the motor counterclockwise
    GPIO.output(6, GPIO.LOW)  # Set AIN1
    GPIO.output(5, GPIO.HIGH)  # Set AIN2
    pwm.start(50)

    # Wait 5 seconds
    time.sleep(25)

    # Reset all the GPIO pins by setting them to LOW
    GPIO.output(6, GPIO.LOW)  # Set AIN1
    GPIO.output(5, GPIO.LOW)  # Set AIN2
    pwm.stop()
    GPIO.output(13, GPIO.LOW)  # Set STBY
    GPIO.cleanup()


# Lets loop awaiting for your input
while True:
    # command = 'Client ready'
    # s.send(command)
    msg = s.recv(1024)
    if msg:
        if msg == 'forward':
            forward()
            s.send('Done forward')
        elif msg == 'backward':
            backward()
            s.send('Done backward')
