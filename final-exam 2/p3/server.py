import asyncio
import random

port = 2500
BUFSIZE = 1024


def get_temp():
    temp = random.randint(0, 50)
    return int(temp)

def get_humid():
    humid = random.randint(0, 100)
    return int(humid)

def get_illum():
    illum = random.randint(1, 150)
    return int(illum)

async def handle_echo(reader, writer):
    while True:
        data = await reader.read(BUFSIZE)
        addr = writer.get_extra_info('peername')
        value = data.decode()
        msg = ''
        if value == '1':
            num = get_temp()
            msg = num.to_bytes(4, 'big') + (0).to_bytes(4, 'big')  + (0).to_bytes(4, 'big')
            # print(msg)
            writer.write(msg)
            await writer.drain()
        elif value == '2':
            num = get_humid()
            msg = (0).to_bytes(4, 'big') + num.to_bytes(4, 'big') + (0).to_bytes(4, 'big')
            # print(msg)
            writer.write(msg)
            await writer.drain()
        elif value == '3':
            num = get_illum()
            msg = (0).to_bytes(4, 'big') + (0).to_bytes(4, 'big') + num.to_bytes(4, 'big')
            # print(msg)
            writer.write(msg)
            await writer.drain()
        else:
            msg = (0).to_bytes(4, 'big') + (0).to_bytes(4, 'big') + (0).to_bytes(4, 'big')
            writer.write(msg)
            await writer.drain()
        # print(f"Received {data.decode()!r} from {addr!r}")
        # writer.write(msg)
        # await writer.drain()
        # print(f"Send: {data.decode()!r}")

async def main():
    server = await asyncio.start_server(handle_echo, '', port)

    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    await server.serve_forever()

asyncio.run(main())