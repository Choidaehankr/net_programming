from socket import *
BUFFSIZE = 1024
port = 2500
while True:
    sock = socket(AF_INET, SOCK_DGRAM)
    msg = input('Enter the message("sned mboxId message" or "receive mboxId"): ')
    sock.sendto(msg.encode(), ('localhost', port))
    if msg == 'quit':
        sock.close()
        break
    else:
        data, addr = sock.recvfrom(BUFFSIZE)
        print(data.decode())
    sock.close()