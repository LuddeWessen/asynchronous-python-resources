"""
 Example showing how waiting tasks can be done.
 Copied from comment (May 7, 2018) by jian-en at
 https://gist.github.com/miguelgrinberg/f15bc03471f610cfebeba62438435508
"""

import asyncio
import time

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Finished Task %s: factorial(%s) = %s" % (name, number, f))


async def floop(no_loops):
    for i in range(no_loops):
        await factorial("A" + str(i), i)


t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
factorial("A", 0),
factorial("A", 1),
factorial("B", 2),
factorial("C", 3),
factorial("C", 4),
))
loop.close()

t2 = time.time()
print("Event loop took % s \n" % (t2-t1))
t1 = time.time()


asyncio.run(floop(5))
t2 = time.time()
print("Manual loop took % s \n" % (t2-t1))


def non_async_factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        time.sleep(1)
        f *= i
    print("Finished Task %s: factorial(%s) = %s " % (name, number, f))


def non_async_floop(no_loops):
    for i in range(no_loops):
        non_async_factorial("A" + str(i), i)

t1 = time.time()
non_async_floop(5)
t2 = time.time()
print("Non-asyncio loop took % s" % (t2-t1))



def SlowFunc(completed):
    print("Ran SlowFunc")
    completed[0] = True
