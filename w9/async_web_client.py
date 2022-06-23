import time, asyncio
import urllib.parse

urls = ['https://www.sch.ac.kr', 'https://www.google.co.kr', 'https://www.daum.net',
'https://www.naver.com']


async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(url.hostname, 80)
    http_req = f'HEAD / HTTP/1.1\r\nHost: {url.hostname}\r\n\r\n'

    writer.write(http_req.encode())
    await writer.drain()
    while True:
        resp = await reader.readline()
        if not resp or resp == '\r\n':
            break

        resp = resp.decode().rstrip()
        print(url.hostname, 'HTTP header>', resp)

    writer.close()
    await writer.wait_closed()

async def main():
    tasks = []

    for url in urls:
        tasks.append(asyncio.create_task(print_http_headers(url)))

    await asyncio.gather(*tasks)

asyncio.run(main())