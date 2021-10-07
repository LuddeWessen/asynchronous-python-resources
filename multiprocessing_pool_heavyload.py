import concurrent.futures
import time
import math

def hello_world(delay, named_par=2.0):
    print(f'Hello ...{delay}')
    time.sleep(delay)
    return f'...{delay} sec delayed world!'


def heavyload(looping_time, named_par=2.0):
    print(f'Hello ...{looping_time}')
    t1 = time.time()
    num = 1.99
    no_iter = 0
    while(time.time() - t1 < looping_time):
        for _ in range(1000):
            num = (num*num)
            num = num/0.25
            num = math.sqrt(num)
            num = num/2.0

        no_iter += 1000

    return f'...{time.time() - t1} sec computations!'
    #return no_iter

t1 = time.time()
n = 5
delays = [i for i in range(n,0,-1)]

num = heavyload(2.0)
t2 = time.time()
print("Heavyload running %s" % (t2-t1))


with concurrent.futures.ProcessPoolExecutor() as executor:


    results = []
    # Submit method adds function to be executed, and returns a 'futures' object,
    # a future object ~encapsulates the execution of our function, and lets us "check on it"

    # I do not know how to give named parameters using submit.. what to do if we have x, y=None, z=1 and I want to give x and z but not y ?
    for dl in delays:
        #results.append(executor.submit(hello_world, dl, 3.0))
        results.append(executor.submit(heavyload, dl, 3.0))

    # Or equally:
    #results = [executor.submit(hello_world, dl) for dl in range(n,0,-1)]

    print("Type: ", type(results[0]))

    # Print results, as they arrive
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    t2 = time.time()
    print("Correctly done after %s" % (t2-t1))


    # Let's compare to generator function 'map'
    t1 = time.time()

    namp = [3.0 for i in range(n,0,-1)]

    # Similarly with "maps", the math object:
    #results = executor.map(hello_world, delays, namp)
    results = executor.map(heavyload, delays, namp)
    print("Type: ", type(results))

    for result in results:
        print(result)

    t2 = time.time()
    print("Correctly done after %s" % (t2-t1))
