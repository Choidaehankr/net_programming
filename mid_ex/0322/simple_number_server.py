from http import client
from socket import *

table = {'1': 'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six', 
        '7':'seven', '8':'eight', '9':'nine', '10':'ten'}

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if data == 'q':
            break
        try:
            rsp = table[data.decode()]
        except:
            client.send(b'Try again')
        else:
            client.send(rsp.encode())

client.close()