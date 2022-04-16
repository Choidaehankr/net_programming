import MyTCPServer as my

port = 2500
BUFSIZE = 1024
sock = my.TCPServer(port)
conn, addr = sock.Accepting()
print('connected by', addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print('Received message: ', data.decode())
    conn.send(data)
conn.close()