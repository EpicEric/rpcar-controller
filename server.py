from bluedot import BlueDot

from gpio import *
from logic import handle_event
from models.event import *


def _direction_event(to_gpio_signal, pos):
    input_event = DirectionEvent(pos.x, pos.y)
    output_event = handle_event(input_event)
    to_gpio_signal(output_event)


def _halt_event(to_gpio_signal):
    input_event = HaltEvent()
    output_event = handle_event(input_event)
    to_gpio_signal(output_event)


class Server:
    def __init__(self):
        self._bd = BlueDot()

        to_gpio_signal = gpios()

        self._bd.when_pressed = (lambda x: _direction_event(to_gpio_signal, x))
        self._bd.when_moved = (lambda x: _direction_event(to_gpio_signal, x))
        self._bd.when_released = (lambda: _halt_event(to_gpio_signal))

        _halt_event(to_gpio_signal)

