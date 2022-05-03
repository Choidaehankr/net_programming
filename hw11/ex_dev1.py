from socket import *
import random
import time

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 8888))
# s.listen(5)
print('8888 포트에서 연결 대기 중..')

def getData(addr):
    while True:
        temp = str(random.randint(0, 40))
        humid = str(random.randint(0, 100))
        illum = str(random.randint(70, 150))
        # client.send((temp + ' ' + humid + ' ' + illum).encode())
        s.sendto((temp + ' ' + humid + ' ' + illum).encode(), addr)
        time.sleep(3)

# client, addr = s.accept()
# print('connected from', addr)

while True:
    msg, addr = s.recvfrom(1024)
    print('Received: ', msg.decode())
    if msg.decode() == 'Start':
        getData(addr)

