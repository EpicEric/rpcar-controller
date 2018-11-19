from gpiozero import LED, PWMLED
import enum


class GPIOMapping(enum.Enum):
    LEFT_DIRECTION = 25
    LEFT_INTENSITY = 12
    RIGHT_DIRECTION = 24
    RIGHT_INTENSITY = 13


def gpios():
    left_direction = LED(GPIOMapping.LEFT_DIRECTION.value)
    right_direction = LED(GPIOMapping.RIGHT_DIRECTION.value)
    left_intensity = PWMLED(GPIOMapping.LEFT_INTENSITY.value)
    right_intensity = PWMLED(GPIOMapping.RIGHT_INTENSITY.value)

    def __send_to_gpio(gpio, direction):
        if direction.value:
            gpio.on()
        else:
            gpio.off()

    def __send_to_pwm(pwm, direction, value):
        if direction.value:
            pwm.value = 1.0 - value
        else:
            pwm.value = value

    def to_gpio_signal(engine_event):
        left = engine_event.left_engine_input
        right = engine_event.right_engine_input
        __send_to_gpio(left_direction, left[1])
        __send_to_pwm(left_intensity, left[1], left[0])
        __send_to_gpio(right_direction, right[1])
        __send_to_pwm(right_intensity, right[1], right[0])

    return to_gpio_signal
