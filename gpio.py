import RPi.GPIO as GPIO

import gpio_mapping


class MotorInterface:

    @staticmethod
    def __send_to_gpio(gpio_number, value):
        GPIO.output(gpio_number, value)

    @staticmethod
    def __send_to_pwm(pwm, value):
        pwm.stop()
        pwm.start(value)

    @staticmethod
    def to_gpio_signal(engine_event):
        left = engine_event.left_engine_input
        right = engine_event.right_engine_input
        MotorInterface.__send_to_gpio(gpio_mapping.GPIOMapping.LEFT_DIRECTION.value, left[1].value)
        MotorInterface.__send_to_pwm(gpio_mapping.PWM_LEFT, left[0] * 100)
        MotorInterface.__send_to_gpio(gpio_mapping.GPIOMapping.RIGHT_DIRECTION.value, right[1].value)
        MotorInterface.__send_to_pwm(gpio_mapping.PWM_RIGHT, right[0] * 100)
