from socket import *
import select

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s_sock == s:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            data = s.recv(BUFFER)
            if not data:
                s.close()
                socks.remove(s)
                continue
            print('Received:', data.decode())
            s.send(data)