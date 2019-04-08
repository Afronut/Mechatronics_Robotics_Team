#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO
dc = 100
GPIO.setwarnings(False)

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(18, GPIO.OUT)  # Connected to PWMA
GPIO.setup(5, GPIO.OUT)  # Connected to AIN2
GPIO.setup(6, GPIO.OUT)  # Connected to AIN1
GPIO.setup(13, GPIO.OUT)  # Connected to STBY


def ballScrewForward():
    # Drive the motor forward
    GPIO.output(6, GPIO.HIGH)  # Set AIN1
    GPIO.output(5, GPIO.LOW)  # Set AIN2

    # Set the motor speed
    pwm = GPIO.PWM(18, 50)  # Set PWMA
    pwm.start(dc)

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(2.5)
    pwm.stop()  # Set PWMA
    time.sleep(2.5)
    pwm.start(dc)


def ballScrewBackward():
    # Drive the motor counterclockwise
    print("Counterclock")
    GPIO.output(6, GPIO.LOW)  # Set AIN1
    GPIO.output(5, GPIO.HIGH)  # Set AIN2

    # Wait 5 seconds
    time.sleep(5)


def resetPins()


# Reset all the GPIO pins by setting them to LOW
GPIO.output(6, GPIO.LOW)  # Set AIN1
GPIO.output(5, GPIO.LOW)  # Set AIN2
pwm.stop()  # Set PWMA
GPIO.output(13, GPIO.LOW)  # Set STBY
