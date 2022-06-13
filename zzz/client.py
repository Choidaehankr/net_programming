import asyncio
from socket import *

port = 2500
BUFSIZE = 1024

async def send_task(sock):
    while True:
        msg = await asyncio.to_thread(input, '메세지를 입력하세요:')
        sock.send(msg.encode())

async def recv_task(sock):
    while True:
        data = await asyncio.to_thread(sock.recv, BUFSIZE)
        if not data:
            break
        print(f'받은 메세지: ', data.decode())

async def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', port))
    await asyncio.gather(
            send_task(sock),
            recv_task(sock)
    )

asyncio.run(main())