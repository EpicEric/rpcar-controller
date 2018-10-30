import enum

PWM_LEFT = None
PWM_RIGHT = None

class GPIOMapping(enum.Enum):
    LEFT_DIRECTION = 25
    LEFT_INTENSITY = 12
    RIGHT_DIRECTION = 24
    RIGHT_INTENSITY = 11
