from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Input: ')
    if msg == 'q':
        s.send(msg.encode())
        break

    s.send(msg.encode())

    print('Result: ', s.recv(1024).decode())

s.close()