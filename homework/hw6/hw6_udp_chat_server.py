from socket import *
from collections import defaultdict, deque

def addMsg(userId, msg):  
    msgBox[userId].append(msg)
    return 'OK'

def removeMsg(userId):
    try:
        if len(msgBox[userId]) == 0:
            return 'No messages'
    except:
        return 'No messages'
    return msgBox[userId].popleft()

BUFFSIZE = 1024
port = 2500
msgBox = defaultdict(deque)

while True:
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('', port))

    s, addr = sock.recvfrom(BUFFSIZE)
    data = s.decode().split(' ')
    reqCmd = data[0]
    if(reqCmd == 'quit'):
        sock.close()
        break
    try:
        reqId = data[1]
        reqMsg = ""
        if reqCmd == 'send':
            for x in data[2:]:
                reqMsg += (x + ' ')
            reqMsg = addMsg(reqId, reqMsg)
        elif reqCmd == 'receive':
            reqMsg = removeMsg(reqId)
        else:
            reqMsg = 'input error. try again'
        sock.sendto(reqMsg.encode(), addr)
    except Exception as e:
        sock.sendto('message error'.encode(), addr)
    sock.close()

sock.close()