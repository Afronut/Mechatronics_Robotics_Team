#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(18, GPIO.OUT) # Connected to PWMA
GPIO.setup(5, GPIO.OUT) # Connected to AIN2
GPIO.setup(6, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY
def forward():
  # Drive the motor clockwise
  GPIO.output(6, GPIO.HIGH) # Set AIN1
  GPIO.output(5, GPIO.LOW) # Set AIN2

  # Set the motor speed
  # GPIO.output(18, GPIO.HIGH) # Set PWMA
  pwm = GPIO.PWM(18, 1000)
  pwm.start(50)

  # Disable STBY (standby)
  GPIO.output(13, GPIO.HIGH)

  # Wait 5 seconds
  time.sleep(25)
# GPIO.output(18, GPIO.LOW) # Set PWMA
# time.sleep(2.5)
# # pwm = GPIO.PWM(18, 1000)
# pwm.start(50)
  pwm.stop()
  GPIO.output(6, GPIO.LOW) # Set AIN1
  GPIO.output(5, GPIO.LOW) # Set AIN2
  pwm.stop()
  GPIO.output(13, GPIO.LOW) # Set STBY
  
def backward():
  time.sleep(2)
  # Drive the motor counterclockwise
  print "Counterclock"
  GPIO.output(6, GPIO.LOW) # Set AIN1
  GPIO.output(5, GPIO.HIGH) # Set AIN2
  pwm.start(50)


  # Wait 5 seconds
  time.sleep(25)

  # Reset all the GPIO pins by setting them to LOW
  GPIO.output(6, GPIO.LOW) # Set AIN1
  GPIO.output(5, GPIO.LOW) # Set AIN2
  pwm.stop()
  GPIO.output(13, GPIO.LOW) # Set STBY
