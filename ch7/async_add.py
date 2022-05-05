import asyncio

async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1)
    return a + b

async def print_add(a, b):
    result = await add(a, b)
    print('print_add: {0} + {1} = {2}'.format(a, b, result))

asyncio.run(print_add(1, 2))