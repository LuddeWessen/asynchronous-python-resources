"""
 Example showing how waiting tasks can be done.
 Inspired by comment (May 7, 2018) by jian-en at
 https://gist.github.com/miguelgrinberg/f15bc03471f610cfebeba62438435508
"""

import asyncio
import time

def PrintTime(t1):
    t2 = time.time()
    print("Time passed: ", t2-t1)
    return t2


# The quick function
"""
async def QuickFunc(number):
    await asyncio.sleep(0.25)
    print("Ran QuickFunc no %s" % (number))
"""

async def QuickFunc(number):
    await asyncio.sleep(0.25)

    if slowf_complete[0]:
        print("Ran QuickFunc no %s" % (number))
    else:
        print("Waiting ", number)


"""
def QuickFunc(number):
    print("Ran QuickFunc no %s" % (number))
"""

async def SlowFunc(number, re_calc):
    if re_calc:
        slowf_complete[0] = False
        print("slowf_complete[0]: ", slowf_complete[0])
        await asyncio.sleep(1.01)
        print("Ran SlowFunc no %s" % (number))
        slowf_complete[0] = True
        print("slowf_complete[0]: ", slowf_complete[0])

    slowf_complete[0] = True

def get_sc():
    return slowf_complete[0]


async def OuterLoop(no_loops):

    no_sf = 0
    SlowFunc(no_sf, True)
    t1 = time.time()
    no_sf += 1
    for i in range(no_loops):
        await SlowFunc(no_sf, not slowf_complete[0] )
        no_sf += 1

        if i%10==0:
            slowf_complete[0] = False

        print(slowf_complete[0])

        await QuickFunc(i)

    t1 = PrintTime(t1)


"""
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
QuickFunc(1),
SlowFunc(2),
))
loop.close()
"""

slowf_complete = [False]

#loop = asyncio.get_event_loop()
asyncio.run(OuterLoop(30))
#loop.close()
