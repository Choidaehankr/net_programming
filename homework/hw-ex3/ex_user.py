from select import select
from socket import *
import selectors
import time

sel = selectors.DefaultSelector()

dev1 = socket(AF_INET, SOCK_DGRAM)
# dev2 = socket(AF_INET, SOCK_DGRAM)

# dev1.connect(('localhost', 8888))
# dev2.connect(('localhost', 9999))

f = open('./data,txt', 'a')


def collector1(conn, mask):

    data, addr = conn.recvfrom(1024)
    data = data.decode().split(' ')
    # print('data: ', data.decode())
    # print('addr: ', addr)
    temp = data[0]
    humid = data[1]
    illum = data[2]
    # print('temp:', temp)
    msg = time.asctime() + ':' + 'Device1:' + ' Temp=' + temp + ' Humid=' + humid + ' Illum=' + illum + '\n'
    print(msg)
    f.write(msg)

# def collector2(conn, mask):
#     data = conn.recvfrom(1024).decode().split(' ')
#     hb = data[0]
#     steps = data[1]
#     cal = data[2]
#     msg = time.asctime() + ':' + 'Device2:' + ' Heartbeat=' + hb + ' Steps=' + steps + ' Cal=' + cal + '\n'
#     print(msg)
#     f.write(msg)

sel.register(dev1, selectors.EVENT_READ, collector1)
# sel.register(dev2, selectors.EVENT_READ, collector2)

dev1.sendto(b'Start', ('localhost', 8888))
# dev2.send(b'Start')

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

