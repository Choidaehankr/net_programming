from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_IP = 'localhost'
PORT = 8080

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        with open('index.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode())
            
httpd = HTTPServer((HOST_IP, PORT), http_handler)
print('Serving HTTP on {}:{}'.format(HOST_IP, PORT))
httpd.serve_forever()