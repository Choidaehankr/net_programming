from socket import *
port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    try:
        data = conn.recv(BUFSIZE)
    except:
        break
    else:
        if not data:
            break
        print("Received message: ", data.decode())
    try:
        conn.send(data)
    except:
        break

conn.close()