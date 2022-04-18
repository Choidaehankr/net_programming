from socket import *
import threading

port = 2500
BUFFSIZE = 1024

def echoTask(sock):
    while True:
        data = sock.recv(BUFFSIZE)
        if not data:
            break
        print('Received message: ', data.decode())
        sock.send(data)
    sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    th = threading.Thread(target=echoTask, args=(conn,))
    th.start()