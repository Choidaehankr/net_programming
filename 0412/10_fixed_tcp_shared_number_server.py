from socket import *
import threading

port = 2500
BUFSIZE = 1024

sharedData = 0

def thread_handler(sock):
    global sharedData, lock
    lock.acquire()
    for _ in range(10000000):
        sharedData += 1
    lock.release()
    print(sharedData)
    sock.send(str(sharedData).encode())
    sock.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

lock = threading.Lock()

while True:
    client, addr = s.accept()
    print('connected by', addr)
    th = threading.Thread(target=thread_handler, args=(client,))
    th.start()

s.close()