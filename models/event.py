class InputEvent:
  pass

class DirectionEvent(InputEvent):
  def __init__(self, x, y):
    self.x = x
    self.y = y

class HaltEvent(InputEvent):
  pass
