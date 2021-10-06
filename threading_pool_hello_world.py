import concurrent.futures
import time

def hello_world(delay):
    print(f'Hello ...{delay}')
    time.sleep(delay)
    return f'...{delay} sec delayed world!'


t1 = time.time()
n = 5
print([i for i in range(n,0,-1) ])
with concurrent.futures.ThreadPoolExecutor() as executor:
    delays = [i for i in range(n,0,-1)]

    results = []
    # Submit method adds function to be executed, and returns a 'futures' object,
    # a future object ~encapsulates the execution of our function, and lets us "check on it"
    for dl in delays:
        results.append(executor.submit(hello_world, dl))

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

    # Similarly with "maps", the math object:
    results = executor.map(hello_world, delays)
    print("Type: ", type(results))

    for result in results:
        print(result)

    t2 = time.time()
    print("Correctly done after %s" % (t2-t1))
