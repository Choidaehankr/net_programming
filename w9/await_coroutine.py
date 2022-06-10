import asyncio, time

async def add(a, b):
    print('In add() func')
    await asyncio.sleep(1)
    print(a + b)

async def mul(a, b):
    print('In mul() func')
    await asyncio.sleep(2)
    print(a * b)

async def main():
    print(f"started at {time.strftime('%X')}")
    await add(1, 2)
    await mul(3, 4)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
