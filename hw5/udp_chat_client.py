from socket import *
from collections import defaultdict
port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"): ')
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())