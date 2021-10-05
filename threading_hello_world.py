import threading
import time

def hello(delay):
    time.sleep(delay)
    print('Hello ...')

def world(delay):
    time.sleep(delay)
    print('... World!')

def hellos(delay=0.9):
    while(True):
        hello(delay)

def worlds(delay=0.8):
    while(True):
        world(delay)


# Python 3.7+
print("Loop:")

threading.Thread(target=hellos).start()
threading.Thread(target=worlds).start()
