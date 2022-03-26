from http import client
from socket import *

def calc(x, y, type):
    if type == '+':
        return x + y
    elif type == '-':
        return x - y
    elif type == '/':
        return round(x / y, 1)
    elif type == '*':
        return x * y

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')
while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        temp = data.decode()
        if temp == 'q':
            print('Program quit...')
            client.close()
            exit()
        else:
            temp = data.decode().split()
            first = int(temp[0])
            second = int(temp[2])
            type = temp[1]
            result = calc(first, second, type)
        client.send(str(result).encode())
                
                