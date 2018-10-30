import RPI.GPIO as GPIO

import .gpio_mapping
import .pwm

DEFAULT_FREQ = 100

def setup():
    GPIO.setmode(GPIO.BCM)
    initialize_pin_mapping()

def initialize_pin_mapping():
    GPIO.setup(GPIOMapping.LEFT_DIRECTION, GPIO.OUT)
    GPIO.setup(GPIOMapping.RIGHT_DIRECTION, GPIO.OUT)
    GPIO.setup(GPIOMapping.LEFT_INTENSITY, GPIO.OUT)
    GPIO.setup(GPIOMapping.RIGHT_INTENSITY, GPIO.OUT)
    pwm_left = GPIO.PWM(GPIOMapping.LEFT_INTENSITY, DEFAULT_FREQ)
    pwm_right = GPIO.PWM(GPIOMapping.RIGHT_INTENSITY, DEFAULT_FREQ)
    initialize_pwm(pwm_left, pwm_right)

def initialize_pwm(pwm_left, pwm_right):
    global gpio_mapping.PWM_LEFT, gpio_mapping.PWM_RIGHT
    gpio_mapping.PWM_LEFT = pwm_left
    gpio_mapping.PWM_RIGHT = pwm_right
