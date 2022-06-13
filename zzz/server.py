import asyncio
from socket import *

port = 2500
BUFSIZE = 1024

async def send_task(conn, addr):
    while True:
        msg = await asyncio.to_thread(input, '메세지를 입력하세요:')
        conn.send(msg.encode())

async def recv_task(conn, addr):
    while True:
        data = await asyncio.to_thread(conn.recv, BUFSIZE)
        if not data:
            break
        print(f'받은 메세지: ', data.decode())

async def main():
    sock = socket()
    sock.bind(('', port))
    sock.listen(5)

    while True:
        client, addr = await asyncio.to_thread(sock.accept)
        print(addr, 'accepted')
        await asyncio.gather(
            send_task(client, addr),
            recv_task(client, addr)
        )

asyncio.run(main())