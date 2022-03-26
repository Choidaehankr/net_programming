from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Number to send (1~10): ')
    if msg == 'q':
        break

    s.send(msg.encode())

    print('Received message: ', s.recv(1024).decode())

s.close()