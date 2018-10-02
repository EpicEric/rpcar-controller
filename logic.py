from models.event import *

def _is_halt_event(event):
  return type(event) is HaltEvent

def _is_direction_event(event):
  return type(event) is DirectionEvent

def handle_event(event: InputEvent):
  if _is_halt_event(event):
    return halt_command

  elif _is_direction_event(event):
    return direction_command

  else:
    raise ValueError("Could not understand event type " +
                     type(event).__name__)
