import socket

name = 'Daehan Choi'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.send(name.encode())
# tmp = sock.recv(1024)
code = int.from_bytes(sock.recv(1024), 'big')
print(code)
sock.close()