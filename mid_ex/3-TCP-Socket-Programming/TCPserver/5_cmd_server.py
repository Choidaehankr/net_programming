from socket import *
import sys

port = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, addr = sock.accept()
print('connected by', addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())
    conn.send(data)
conn.close()

