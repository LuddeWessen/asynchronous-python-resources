import multiprocessing
import time

def hello_world(delay):
    print(f'Hello ...{delay}')
    time.sleep(delay)
    return f'...{delay} sec delayed world!'

t1 = time.time()

p1 = multiprocessing.Process(target=hello_world, args=[1.0])
p2 = multiprocessing.Process(target=hello_world, args=[1.0])

p1.start()
p2.start()

t2 = time.time()
# Note that this print comes _long_ before the threads
print("This prints after %s" % (t2-t1))

p1.join()
p2.join()

t2 = time.time()
# Note that this print comes _long_ before the threads
print("Actually done after %s" % (t2-t1))


t1 = time.time()


# New
p1 = multiprocessing.Process(target=hello_world, args=[1.0])
p2 = multiprocessing.Process(target=hello_world, args=[1.0])

p1.start()
p2.start()

p1.join()
p2.join()

t2 = time.time()
# Note that this print comes _long_ before the threads
print("Correctly done after %s" % (t2-t1))
