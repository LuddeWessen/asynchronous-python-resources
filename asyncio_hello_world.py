import asyncio

# Adapted from: https://docs.python.org/3/library/asyncio.html , 2021-10-04

async def hello_world():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
print("Event loop:")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
hello_world(),
hello_world(),
hello_world(),
hello_world(),
hello_world(),
))
loop.close()
