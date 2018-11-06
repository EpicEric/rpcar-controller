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
    

    def __send_to_gpio(gpio, value):
        if value:    
            gpio.on()
        else:
            gpio.off()
    
    def __send_to_pwm(pwm, value):
        pwm.value = value
    
    def to_gpio_signal(engine_event):
        left = engine_event.left_engine_input
        right = engine_event.right_engine_input
        __send_to_gpio(left_direction, left[1].value)
        __send_to_pwm(left_intensity, left[0])
        __send_to_gpio(right_direction, right[1].value)
        __send_to_pwm(right_intensity, right[0])

    return to_gpio_signal
