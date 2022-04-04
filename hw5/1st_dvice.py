from socket import *
import random

def getData():
    temp = str(random.randint(0, 40))
    humid = str(random.randint(0, 100))
    illum = str(random.randint(70, 150))
    return temp + ' ' + humid + ' ' + illum

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, args = sock.accept()
    data = conn.recv(BUFSIZE).decode()
    
    if data == 'Request':
        conn.send(getData().encode())
    elif data == 'quit':
        break
    conn.close()

conn.close()
sock.close()