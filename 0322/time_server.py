from http import client
from pydoc import cli
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(5)

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    client.send(time.ctime(time.time()).encode())
    client.close()