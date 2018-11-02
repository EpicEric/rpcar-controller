#!/usr/bin/env python3
from setup import setup
from listen import listen


if __name__ == "__main__":
    setup()
    listen()

else:
    print("You should not use this file as a lib")
    exit()
