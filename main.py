from signal import pause
from .event import fetch_event
from .logic import handle_event

def listen_to_events_loop():
  while True:
    event = fetch_event()
    command_to_take = handle_event(event)
    dispatch_event(command_to_take)

if __name__ == '__main__':
    listen_to_events_loop()

