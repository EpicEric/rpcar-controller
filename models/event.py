from enum import Enum

class EngineDirection(Enum):
  FORWARD = 1
  BACKWARD = 2

class InputEvent:
  pass

class DirectionEvent(InputEvent):
  @staticmethod
  def is_coordinates_valid(x, y):
    assert x**2 + y**2 <= 1

  def __init__(self, x, y):
    assert DirectionEvent.is_coordinates_valid(x, y)

    self.x = x
    self.y = y

  def get_coordinates(self):
    return (self.x, self.y)

class HaltEvent(InputEvent):
  pass


class OutputEvent:
  pass

class EngineInput(OutputEvent):
  @staticmethod
  def is_valid_engine_input(engine_input):
    (magnitude, direction) = engine_input
    return -1. < magnitude < 1. and direction in EngineDirection

  def __init__(self, left_engine_input, right_engine_input):
    assert EngineInput.is_valid_engine_input(left_engine_input), "{} is not a valid input for left engine".format(left_engine_input)
    assert EngineInput.is_valid_engine_input(right_engine_input), "{} is not a valid input for right engine".format(right_engine_input)

    self.left_engine_input = left_engine_input
    self.right_engine_input = right_engine_input
