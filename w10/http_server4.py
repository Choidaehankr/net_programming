from http.server import HTTPServer, BaseHTTPRequestHandler

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()
    
    def route(self):
        if self.path == '/':
            self.send_html()
        elif self.path == '/iot.png':
            self.send_image()
        else:
            self.response(404, 'Not Found')
    
    def send_html(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('index.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def send_image(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        with open('iot.png', 'rb') as f:
            msg = f.read()
            self.wfile.write(msg)
            
    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(body.encode())

httpd = HTTPServer(('localhost', 8080), http_handler)
print('Serving HTTP on {}:{}'.format('localhost', 8080))
httpd.serve_forever()