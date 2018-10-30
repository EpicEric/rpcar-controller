import RPi.GPIO as GPIO
import .gpio_mapping

class MotorInterface:

  def __send_to_gpio(gpio_number, value):
      GPIO.output(gpio_number, value)

  def __send_to_pwm(pwm, value):
      pwm.stop()
      pwm.start(value)

  def to_gpio_signal(engine_inputs):
      left, right = engine_inputs
      __send_to_gpio(GPIOMapping.LEFT_DIRECTION, left[1])
      __send_to_pwm(gpio_mapping.PWM_LEFT, left[0]*100)
      __send_to_gpio(GPIOMapping.RIGHT_DIRECTION, right[1])
      __send_to_pwm(gpio_mapping.PWM_RIGHT, right[0]*100)
