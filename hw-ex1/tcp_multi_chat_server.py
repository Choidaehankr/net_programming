from socket import *
import threading
import time

clients = []
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2500))
s.listen(5)
print('Server started')

def task(client):
    while True:
        # data = client.recv(1024)
        data = client.recv(1024).decode()
        # print(data)
        # if 'quit' in data.decode():
        if 'quit' in data:
            print(addr, 'exited')
            clients.remove(addr)
            continue
        # print(time.asctime() + str(addr) + ':' + data.decode())
        print(time.asctime() + str(addr) + ':' + data)

        for c in clients:
            if c != client:
                # c.send(data)
                c.send(data.encode())
    client.close()


while True:
    client, addr = s.accept()
    if client not in clients:
        print('new client', addr)
        clients.append(client)
    th = threading.Thread(target=task, args=(client,))
    th.start()