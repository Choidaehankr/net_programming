from socket import *
import threading
from turtle import st

port = 3333
BUFFSIZE = 1024

def recvTask(sock):
    while True:
        data = sock.recv(BUFFSIZE)
        print('<-', data.decode())
    

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

th = threading.Thread(target=recvTask, args=(sock,))
th.start()

while True:
    msg = input()
    print('->', msg)
    sock.send(msg.encode())