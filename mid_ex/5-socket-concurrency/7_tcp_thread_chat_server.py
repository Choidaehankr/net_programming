from socket import *
import threading

port = 3333
BUFFSIZE = 1024

def sendTask(sock):
    while True:
        resp = input()
        print('->', resp)
        sock.send(resp.encode())

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(1)
conn, addr = s.accept()

th = threading.Thread(target=sendTask, args=(conn,))
th.start()

while True:
    data = conn.recv(BUFFSIZE)
    print('<-', data.decode())