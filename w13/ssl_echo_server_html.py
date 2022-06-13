from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

HOST_IP = 'localhost'
PORT = 8080

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<H1>Hello, IoT!</H1>')

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.pem', keyfile='server.key')

httpd = HTTPServer((HOST_IP, PORT), http_handler)
print('Serving HTTP on {}:{}'.format(HOST_IP, PORT))
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

httpd.serve_forever()