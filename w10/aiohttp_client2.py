import aiohttp
import asyncio

async def main():
    async with aiohttp.request('GET', 'http://python.org/') as rsp:
        print(rsp.status)
        print(rsp.headers)
        print(await rsp.text())

asyncio.run(main()) 