import boot from boot
import setup from setup

if __name__ is "__main__":
  boot()
  setup()
  listen_to_events_loop()
else:
  print("You should not use this file as a lib")
  exit()
