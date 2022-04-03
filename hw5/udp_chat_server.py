from contextlib import nullcontext
from re import U
from socket import *
from collections import defaultdict
port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

msgBox = defaultdict(list)

def addMsg(userId, msg):  
    msgBox[userId].append(msg)

def removeMsg(userId):
    return msgBox[userId].pop()  # pop이 맞나?

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print('data: ', data)
    req = data.decode()
    reqCmd = req.split[0]
    if(reqCmd == "quit"):
        break
    elif(reqCmd == 'send'):
        reqId = req.split(' ')[1]
        reqMsg = req.split(' ')[2:]  # 흠..
        addMsg(reqId, reqMsg)
        respMsg = 'OK'
        sock.sendto(respMsg.encode(), addr)
    elif(reqCmd == 'remove'):
        reqId = req.split(' ')[1]
        reqStr = removeMsg(reqId)
        if(reqStr): continue  # 비어있다면;
        
print('<- ', data.decode())
resp = input('-> ')
sock.sendto(resp.encode(), addr)