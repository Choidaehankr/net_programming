from socket import *
import time

clients = []

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 2500))

print('Server Started')

while True:
    data, addr = s.recvfrom(1024)
    if 'quit' in data.decode():
        if addr in clients:
            print(addr, 'exited')
            clients.remove(addr)
            s.close()
            continue

    if addr not in clients:
        print('new client', addr)
        clients.append(addr)

    print(time.asctime() + str(addr) + ':' + data.decode())

    for client in clients:
        if client != addr:
            s.sendto(data, client)