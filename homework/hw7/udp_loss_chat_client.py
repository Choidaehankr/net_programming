from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), ('localhost', port))
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
        sock.sendto(b'fail', ('localhost', port))
        sock.settimeout(None)
        while True:
            try:
                tmpD, tmpA = sock.recvfrom(BUFF_SIZE)
            except timeout:
                break
            if(tmpD.decode() == 'nack'):
                print('I received a NACK!')
                break

    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if data.decode() == 'fail':
            sock.sendto(b'nack', ('localhost', port))
            break
        elif random.random() <= 0.7:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break