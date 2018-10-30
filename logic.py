import math

from models.event import *

HALT_ENGINE_INPUT = (0, EngineDirection.FORWARD)
HALT_ENGINE_EVENT = EngineInput(HALT_ENGINE_INPUT, HALT_ENGINE_INPUT)


def get_quadrant(x, y):
  if x > 0 and y > 0:
    return 1
  elif x < 0 and y > 0:
    return 2
  elif x < 0 and y < 0:
    return 3
  elif x > 0 and y < 0:
    return 4

def get_magnitude(x, y):
  return (x**2 + y**2) ** 0.5

def is_on_right_half(x, y):
  return x > 0

def is_on_left_half(x, y):
  return x < 0

def is_on_upper_half(x, y):
  return y > 0

def is_on_bottom_half(x, y):
  return y > 0

def to_engine_inputs(left, right, intensity):
  left_direction = EngineDirection.BACKWARD if left < 0 else EngineDirection.FORWARD
  right_direction = EngineDirection.BACKWARD if right < 0 else EngineDirection.FORWARD
  left_input = (math.abs(left * intensity), left_direction)
  right_input = (math.abs(right * intensity), right_direction)

  return (left_input, right_input)

def direction_event_to_engine_input(event: DirectionEvent) -> (float, EngineDirection):
  (x, y) = event.get_coordinates()
  intensity = get_magnitude(x, y)

  if is_on_right_half(x, y):
    l = 1
    r = 1 - 2*x
  else:
    l = 1 - 2*x
    r = 1

  if is_on_bottom_half(x, y):
    l *= -1
    r *= -1

  return EngineInputEvent(*to_engine_inputs(l, r, intensity))


def _is_halt_event(event):
  return type(event) is HaltEvent

def _is_direction_event(event):
  return type(event) is DirectionEvent

def handle_event(event: InputEvent) -> OutputEvent:
  if _is_halt_event(event):
    return HALT_ENGINE_EVENT

  elif _is_direction_event(event):
    (left_engine, right_engine) = direction_event_to_engine_input(event)
    return left_engine, right_engine

  else:
    raise ValueError("Could not understand event type " +
                     type(event).__name__)
