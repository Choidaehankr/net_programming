import ssl
import socket

hostname = 'home.sch.ac.kr'

context = ssl.create_default_context()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(sock, server_hostname=hostname)
conn.connect((hostname, 443))

conn.send(b'HEAD /sch/index.jsp HTTP/1.1\r\nHost: home.sch.ac.kr\r\n\r\n')

msg = conn.recv(4096)
print(msg.decode())