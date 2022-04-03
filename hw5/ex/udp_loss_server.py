from asyncio.windows_utils import BUFSIZE
from socket import *
import random

BUF_SIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening...')

while True:
    data, addr = s_sock.recvfrom(BUF_SIZE)
    if random.randint(1, 10) <= 3:
        print("Pakcet from {} lost!".format(addr))
        continue
    print("Packet is {} from {}".format(data.decode(), addr))

    s_sock.sendto('ack'.encode(), addr)
