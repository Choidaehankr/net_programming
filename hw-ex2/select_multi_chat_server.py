import socket, select

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            data = s.recv(BUFFER)
            print(data.decode())
            if not data:
                s.close()
                socks.remove(s)
                continue
            for c in socks:
                if c != s_sock and c != s:
                    c.send(data)
