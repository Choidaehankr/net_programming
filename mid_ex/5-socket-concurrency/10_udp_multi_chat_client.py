from socket import *
import threading

def handler(sock):
    while True:
        msg, addr = sock.recvfrom(1024)
        print(msg.decode())

svr_addr = ('localhost', 2500)
sock = socket(AF_INET, SOCK_DGRAM)

my_id = input('ID를 입력하세요: ')
sock.sendto(('['+my_id+']').encode(), svr_addr)

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + ']' + input()
    sock.sendto(msg.encode(), svr_addr)