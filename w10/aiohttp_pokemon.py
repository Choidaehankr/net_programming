import aiohttp
import asyncio
import time

async def get_pokemon(session, url):
    async with session.get(url) as rsp:
        pokemon = await rsp.json()
        return pokemon['name']

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 11):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

start_time = time.time()
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))