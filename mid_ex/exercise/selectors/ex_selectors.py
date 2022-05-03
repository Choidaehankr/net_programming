import selectors
from socket import *
import time

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print('connected from', addr)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    if(data.decode() == '1'):
        print('Receive 1 !!!')
        sel.register(conn, selectors.EVENT_READ, sendDate)
        # sendDate(conn)
    elif(data.decode() == '2'):
        print('Receive 2 @@@@')
        sel.register(conn, selectors.EVENT_READ, sendThing)
        # sendThing(conn)

def sendDate(conn):
    conn.send(time.asctime().encode())

def sendThing(conn):
    conn.send('hi hello !!!!!!!!!!!!'.encode())

sock = socket()
sock.bind(('', 2500))
sock.listen(5)

sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)