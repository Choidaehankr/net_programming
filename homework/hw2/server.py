import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

code = 20171539

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    name = client.recv(1024)
    print(name.decode())
    # tmp = code.to_bytes(4, 'big')
    # client.send(tmp)
    client.send(code.to_bytes(4, 'big'))
    client.close()
    break