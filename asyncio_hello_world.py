import asyncio

# Copied from: https://docs.python.org/3/library/asyncio.html , 2021-10-04

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
