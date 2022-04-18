from socket import *
import threading

port = 2500
BUFFSIZE = 1024

sharedData = 0

def thread_handler(sock, addr):
    global sharedData, lock
    lock.acquire()
    for _ in range(10000000):
        if(sharedData % 1000000 == 0):
            print('Now number: ', sharedData, ' addr: ', addr)
        sharedData += 1
    lock.release()
    print('DONE!, ', sharedData)
    sock.send(str(sharedData).encode())


s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

lock = threading.Lock()

while True:
    client, addr = s.accept()
    print('connected by', addr)
    th = threading.Thread(target=thread_handler, args=(client, addr))
    th.start()

s.close()