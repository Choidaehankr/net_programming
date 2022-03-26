import socket
from sys import excepthook

port = int(input("PORT No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send: ")
    try:
        bytesSent = s.send(msg.encode())
    except:
        print('connection closed')
        break
    else:
        print("{} bytes send".format(bytesSent))

    try:
        data = s.recv(BUFSIZE)
    except:
        print('connection closed')
        break
    else:
        if not data:
            break
        print("Received messsage: %s" % data.decode())
        
s.close()