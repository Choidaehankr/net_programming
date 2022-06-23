import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))
print("Time: ", sock.recv(1024).decode())
sock.close()