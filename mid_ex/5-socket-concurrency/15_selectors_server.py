from socket import *
import selectors

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print(' connected from', addr)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn)
        conn.close()
        return
    print('received data:', data.decode())
    conn.send(data)

sock = socket()
sock.bind(('', 2500))
sock.listen(5)

# 서버 소켓, 메시지 수신을 감시, 수신했을 때, 데이터로 accept를 받을 것,
sel.register(sock, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data  # key.data = accept값이 리턴됨.
        callback(key.fileobj, mask)