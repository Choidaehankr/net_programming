from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_IP = 'localhost'
PORT = 8080

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, IoT!')

httpd = HTTPServer((HOST_IP, PORT), http_handler)
print('Serving HTTP on {}:{}'.format(HOST_IP, PORT))
httpd.serve_forever()