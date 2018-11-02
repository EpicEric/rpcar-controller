import RPi.GPIO as GPIO
from signal import *

import gpio_mapping
from teardown import teardown

DEFAULT_FREQ = 100


def setup():
    GPIO.setmode(GPIO.BCM)
    initialize_pin_mapping()
    for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
        signal(sig, teardown)


def initialize_pin_mapping():
    GPIO.setup(gpio_mapping.GPIOMapping.LEFT_DIRECTION.value, GPIO.OUT)
    GPIO.setup(gpio_mapping.GPIOMapping.RIGHT_DIRECTION.value, GPIO.OUT)
    GPIO.setup(gpio_mapping.GPIOMapping.LEFT_INTENSITY.value, GPIO.OUT)
    GPIO.setup(gpio_mapping.GPIOMapping.RIGHT_INTENSITY.value, GPIO.OUT)
    pwm_left = GPIO.PWM(gpio_mapping.GPIOMapping.LEFT_INTENSITY.value, DEFAULT_FREQ)
    pwm_right = GPIO.PWM(gpio_mapping.GPIOMapping.RIGHT_INTENSITY.value, DEFAULT_FREQ)
    initialize_pwm(pwm_left, pwm_right)


def initialize_pwm(pwm_left, pwm_right):
    gpio_mapping.PWM_LEFT = pwm_left
    gpio_mapping.PWM_RIGHT = pwm_right
