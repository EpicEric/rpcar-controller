import RPi.GPIO as GPIO
import sys


def teardown():
    print("Shutting down...")
    GPIO.cleanup()
    sys.exit(0)

