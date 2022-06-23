from base64 import encode
from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if(data.decode() == 'fail'):
            sock.sendto(b'nack', addr)
            break
        elif random.random() <= 0.7:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
    msg = input('-> ')
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    if reTx > 3:
        # print('time out!')
        sock.sendto(b'fail', addr)
        sock.settimeout(None)
        while True:
            try:
                tmpD, tmpA = sock.recvfrom(BUFF_SIZE)
            except timeout:
                break
            if tmpD.decode() == 'nack':
                print('I received a NACK!')
                break