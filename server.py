from bluedot import BlueDot

from gpio import MotorInterface
from logic import handle_event
from models.event import *


def _direction_event(pos):
    input_event = DirectionEvent(pos.x, pos.y)
    output_event = handle_event(input_event)
    MotorInterface.to_gpio_signal(output_event)


def _halt_event():
    input_event = HaltEvent()
    output_event = handle_event(input_event)
    MotorInterface.to_gpio_signal(output_event)


class Server:
    def __init__(self):
        self._bd = BlueDot()

        self._bd.when_pressed = _direction_event
        self._bd.when_moved = _direction_event
        self._bd.when_released = _halt_event

        _halt_event()
