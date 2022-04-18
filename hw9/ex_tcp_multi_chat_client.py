from socket import *
import threading

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 2500))

my_id = input('ID를 입력하세요: ')
sock.send(('['+my_id+']').encode())

while True:
    txt = '[' + my_id + ']' + input()
    sock.send(txt.encode())
    