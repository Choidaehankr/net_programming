from socket import *
import random
import time

s = socket()
s.bind(('', 9999))
s.listen(5)
print('9999 포트에서 연결 대기 중..')

def getData(client):
    while True:
        heartbeat = str(random.randint(40, 140))
        steps = str(random.randint(2000, 6000))
        cal = str(random.randint(1000, 4000))
        client.send((heartbeat + ' ' + steps + ' ' + cal).encode())
        time.sleep(5)

client, addr = s.accept()
print('connected from', addr)

while True:
    msg = client.recv(1024)
    if msg.decode() == 'Start':
        getData(client)

