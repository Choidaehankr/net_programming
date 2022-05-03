from socket import *
import threading

# def sender(sock):
#     while True:
#         txt = '[' + my_id + ']' + input()
#         sock.send(txt.encode())

def handler(sock):
    while True:
        msg = sock.recv(1024)
        print(':', msg.decode())

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 2500))

my_id = input('ID를 입력하세요.')
sock.send(('['+my_id+']').encode())

th = threading.Thread(target=handler, args=(sock,))
# th.daemon = True  # error
th.start()

# th1 = threading.Thread(target=sender, args=(sock,))
# th1.daemon = True  # error
# th1.start()

while True:
    txt = '[' + my_id + ']' + input()
    sock.send(txt.encode())