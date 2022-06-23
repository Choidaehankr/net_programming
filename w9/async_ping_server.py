import asyncio

async def handle_asyncclient(reader, writer):
    print('client :', writer.get_extra_info('peername'))
    while True:
        data = await reader.read(8)
        if data == b'ping':
            writer.write(b'pong')
            await writer.drain()
            print('recv: ping -> send: pong')
        elif data == b'done':
            print('recv: done')
            break
        elif len(data) == 0:
            break

    writer.close()
    await writer.wait_closed()
    print('connection was closed')

async def server_asyncmain():
    server = await asyncio.start_server(handle_asyncclient,'localhost',8000)
    print('server started')
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(server_asyncmain()) 