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
    # task1 = asyncio.create_task(add(1, 2))
    # task2 = asyncio.create_task(mul(3, 4))
    # await task1
    # await task2
    1
    # 동일한 작업 1
    # await asyncio.gather(task1, task2)

    # 동일한 작업 2
    await asyncio.gather(add(1, 2), mul(3, 4))

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())