import threading
import time

def hello(delay):
    time.sleep(delay)
    print('Hello ...')

def world(delay):
    time.sleep(delay)
    print('... World!')

def hellos(no_loops, delay=0.5):
    for _ in range(no_loops):
        hello(delay)

def worlds(no_loops, delay=0.4):
    for _ in range(no_loops):
        world(delay)


# Python 3.7+
print("Loop:")

t1 = time.time()

th1 = threading.Thread(target=hellos, args=[10])
th2 = threading.Thread(target=worlds, args=[10])

th1.start()
th2.start()

t2 = time.time()
# Note that this print comes _long_ before the threads
print("This prints after %s" % (t2-t1))


th1.join()
th2.join()

t2 = time.time()
# Note that this print comes _long_ before the threads
print("Actually done after %s" % (t2-t1))


t1 = time.time()


# New
th1 = threading.Thread(target=hellos, args=[10])
th2 = threading.Thread(target=worlds, args=[10])

th1.start()
th2.start()

th1.join()
th2.join()

t2 = time.time()
# Note that this print comes _long_ before the threads
print("Correctly done after %s" % (t2-t1))
