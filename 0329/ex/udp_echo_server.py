import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    print('Received: ', msg.decode())

    sock.sendto(msg, addr)