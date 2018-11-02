from signal import pause
from server import Server

SERVER = None


def listen():
    global SERVER
    if not SERVER:
        SERVER = Server()
        pause()
