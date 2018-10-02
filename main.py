def listen_to_events_loop():
  while True:
    event = fetch_event()
    command_to_take = handle_event(event)
    dispatch_event(command_to_take)
