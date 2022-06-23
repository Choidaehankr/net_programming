from socket import *
import random

def getData():
    heartbeat = str(random.randint(40, 140))
    steps = str(random.randint(2000, 6000))
    cal = str(random.randint(1000, 4000))
    return str(heartbeat + ' ' + steps + ' ' + cal)

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, etc = sock.accept()
    data = conn.recv(BUFSIZE).decode()
    
    if data == 'Request':
        conn.send(getData().encode())
    elif data == 'quit':
        break
    conn.close()

conn.close()
sock.close()