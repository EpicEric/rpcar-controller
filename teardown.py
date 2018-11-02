import RPi.GPIO as GPIO


def teardown():
    print("Shutting down...")
    GPIO.cleanup()

