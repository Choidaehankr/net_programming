from socket import *
import random
import time

s = socket()
s.bind(('', 8888))
s.listen(5)
print('8888 포트에서 연결 대기 중..')

def getData(client):
    while True:
        temp = str(random.randint(0, 40))
        humid = str(random.randint(0, 100))
        illum = str(random.randint(70, 150))
        client.send((temp + ' ' + humid + ' ' + illum).encode())
        time.sleep(3)

client, addr = s.accept()
print('connected from', addr)

while True:
    msg = client.recv(1024)
    if msg.decode() == 'Start':
        getData(client)

