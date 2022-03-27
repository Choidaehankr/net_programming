# 127.0.0.1/index.html

# bind(('', 80))
# listen.

# while True:
    # accept()
    # accept하면 소켓이 생긴다.
    # 그 소켓으로 부터 revc해서 클라이언트가 보내는 http request 첫번째 라인만 읽는다.
#공백으로 파싱하면 두번째가 /indext.html이고, 앞에 / 를 빼면 index.html이라는 파일이름을 얻음


# 연결을 기다렸다가 연결이 맺어지면,  recv()
# 받은 메시지의 첫번째 줄에서 가운데에 경로정보 (파일정보: index.html) 그 파일이 존재하는 경우에는 (iot.png, favicon.ico)
# recv를 한 다음에는 파싱해서 3개중 하난인지 확인을 해야함 (index, iot, favicon)
# 맞다면 그 파일들을 열어서 전송해줘야함.

from genericpath import exists
from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    print("waiting...")
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    fileName = req[0].split()[1][1:]  # fileName = index.html
    if not exists(fileName):
        print("no file")
        exit()
    print("파일 읽기 시작")
    htmlFile = open('index.html', 'r', encoding='utf-8')
    htmlType = 'text/html'
    pngFile = open('iot.png', 'rb')
    pngType = 'image/png'
    # icoFile = open('favicon.ico', 'rb')
    # icoType = 'image/x-icon'
    htmlResp = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: ${htmlType} \r\n' + '\r\n'
    htmlData = htmlFile.read()
    # pngResp = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: ${pngType} \r\n' + '\r\n'
    pngData = pngFile.read()
    # icoData = icoFile.read()
    c.send(htmlResp.encode())
    # c.send(htmlData.encode('euc-kr'))  # 여까진 됨
    c.send(htmlData.encode('euc-kr'))
    # c.send(pngResp.encode())
    # c.send(pngData)
    # c.send(icoData)
    c.close()
    exit()

