from concurrent.futures import thread
from socket import *
import threading

port = 2500
BUFFSIZE = 1024

class ClientThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    
    def run(self):
        while True:
            data = self.sock.recv(BUFFSIZE)
            if not data:
                break
            print('Received message:', data.decode())
            self.sock.send(data)
        self.sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('Connected by', remotehost, remoteport)
    th = ClientThread(conn)
    th.start()