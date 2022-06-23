from socket import *
import time as t
BUFFSIZE = 1024

def getDataFromDev(data, port):
    ans = t.strftime('%c', t.localtime(t.time()))
    if port == 2500:
        ans += ': Device1: '
        ans += ('Temp=' + data[0])
        ans += (', Humid=' + data[1])
        ans += (', Temp=' + data[2] + '\n')
    elif port == 3333:
        ans += ': Device2: '
        ans += ('Heartbeat=' + data[0])
        ans += (', Steps=' + data[1])
        ans += (', Cal=' + data[2] + '\n')
    return ans

while True:
    cmd = input('input command line: ')

    if cmd == 'quit':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 2500))
        s.send(b'quit')
        s.close()

        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 3333))
        s.send(b'quit')
        s.close()
        break

    try:
        if cmd == '1':
            port = 2500
        elif cmd == '2':
            port = 3333
    except:
        print('Enter the number (1 or 2): ')
    
    if port == 2500 or port == 3333:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', port))
        print('port: ', port, ' connecting succesful')

        s.send(b'Request')
        data = s.recv(BUFFSIZE).decode().split(' ')
        respData = getDataFromDev(data, port)

        f= open('test.txt', 'a')
        f.write(respData)
        f.close()

        s.close()
