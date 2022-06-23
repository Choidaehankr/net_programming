# error: module 'asyncio' has no attribute 'to_thread'

import asyncio, time

async def get_user(name):
    print('사용자 {!r} 정보 조회중...'.format(name))
    await asyncio.to_thread(time.sleep, 1)
    print('사용자 {!r} 정보 조회 완료!'.format(name))


async def main():
    start = time.time()
    await asyncio.gather(get_user('Jeon'),
        get_user('Yun'),
        get_user('Kim'),
        get_user('Song'))
    end = time.time()
    print(f'총 소요시간: {end - start}')

asyncio.run(main())