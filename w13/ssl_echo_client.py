import socket, ssl

port = int(input("Port No:"))
address = ("localhost", port)
BUFSIZE = 1024

context = ssl.create_default_context(cafile='root.pem')
#context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#context.load_verify_locations('root.pem')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_conn = context.wrap_socket(sock, server_hostname='iot.co.kr')
ssl_conn.connect(address)

while True:
    msg = input("Message to send: ")
    ssl_conn.send(msg.encode())
    data = ssl_conn.recv(BUFSIZE)
    print("Received message: %s"%data.decode())