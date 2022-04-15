from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('google.com', 80))
# sock.send(b'GET / HTTP/1.1\r\n\r\n')
sock.send(b'GET / HTTP/1.1\r\n\r\n')
data = sock.recv(100000)
print(data.decode())
sock.close()