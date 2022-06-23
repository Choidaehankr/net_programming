# -*- coding: utf8 -*- 
from socket import *
import io
s = socket()
s.bind(('', 80))
s.listen(10)

errorMsg =  'HTTP/1.1 404 Not Found\r\n' + '\r\n' + '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>' +'<BODY>Not Found</BODY></HTML>'
while True:
    print("waiting...")
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    fileName = req[0].split()[1][1:]  # fileName = index.html
    print("파일 읽기 시작")
    if fileName == 'index.html':
        htmlFile = io.open(fileName, 'r', encoding='utf-8')
        minType = 'text/html'
        resMsg = ('HTTP/1.1 200 OK\r\n' + "'Content-Type: " + minType + '\r\n' + '\r\n')
        c.send(resMsg.encode())
        recvMsg = htmlFile.read()
        c.send(recvMsg.encode('euc-kr'))
    elif fileName == 'iot.png':
        pngFile = open(fileName, 'rb')
        minType = 'image/png'
        resMsg = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: ' + minType + '\r\n' + '\r\n')
        c.send(resMsg.encode())
        recvMsg = pngFile.read()
        c.send(recvMsg)
    elif fileName == 'favicon.ico':
        icoFile = open(fileName, 'rb')
        minType = 'image/x-icon'
        resMsg = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: ' + minType + '\r\n' + '\r\n')
        c.send(resMsg.encode())
        recvMsg = icoFile.read()
        c.send(recvMsg)
    else:
        c.send(errorMsg.encode())
    c.close()
    #exit()

