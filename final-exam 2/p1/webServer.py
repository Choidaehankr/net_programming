# -*- coding: utf8 -*- 
from socket import *
import io
import asyncio

BUFSIZE = 1024
errorMsg =  'HTTP/1.1 404 Not Found\r\n' + '\r\n' + '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' +'<BODY>Not Found</BODY></HTML>'

async def handler(reader, writer):
    while True:
        print("waiting...")
        data = await reader.read(BUFSIZE)
        addr = writer.get_extra_info('peername')
        print(f'Received {data.decode()!r} from {addr!r}')
        msg = data.decode()
        print('msg:', msg)
        req = msg.split('\r\n')
        print('req:', req)
        fileName = req[0].split()[1][1:]
        
        if fileName == 'index.html':
            htmlFile = io.open(fileName, 'r', encoding='utf-8')
            minType = 'text/html'
            resMsg = ('HTTP/1.1 200 OK\r\n' + "'Content-Type: " + minType + '\r\n' + '\r\n')
            writer.write(resMsg.encode())
            await writer.drain()
            recvMsg = htmlFile.read()
            writer.write(recvMsg.encode('euc-kr'))
            await writer.drain()
        elif fileName == 'iot.png':
            pngFile = open(fileName, 'rb')
            minType = 'image/png'
            resMsg = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: ' + minType + '\r\n' + '\r\n')
            writer.write(resMsg.encode())
            await writer.drain()
            recvMsg = pngFile.read()
            writer.write(recvMsg)
            await writer.drain()
        elif fileName == 'favicon.ico':
            icoFile = open(fileName, 'rb')
            minType = 'image/x-icon'
            resMsg = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: ' + minType + '\r\n' + '\r\n')
            writer.write(resMsg.encode())
            await writer.drain()
            recvMsg = icoFile.read()
            writer.write(recvMsg)
            await writer.drain()
        else:
            writer.write(errorMsg.encode())
            await writer.drain()
        writer.close()
        await writer.wait_closed()
        print('connection was closed')

async def main():
    server = await asyncio.start_server(handler, '', 80)
    addr = server.sockets[0].getsockname()

    await server.serve_forever()

asyncio.run(main())