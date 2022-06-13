from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()

    def do_POST(self):
        self.route()

    def route(self):
        parsed_path = parse.urlparse(self.path)
        real_path = parsed_path.path
        if real_path == '/':
            self.send_html()
        elif real_path == '/button':
            self.proc_query()
        elif real_path == '/form_get':
            self.proc_query()
        elif real_path == '/form_post':
            self.proc_form_post()
        else:
            self.response(404, '<h1>Not Found!!!!!!!!</h1>')
    
    def send_html(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # with open('index_button.html', 'r', encoding='utf-8') as f:
        # with open('index_get.html', 'r', encoding='utf-8') as f:
        with open('index_post.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def proc_query(self):
        parsed_path = parse.urlparse(self.path)
        query = parsed_path.query
        print('query:', query)
        parsed_query = parse.parse_qs(query)
        print('parsed_query:', parsed_query)
        status = parsed_query['status'][0]
        if status == 'on':
            message = '<h1>GET</h1> <h2>LED in IoT Device is not turned on</h2>'
        elif status == 'off':
            message = '<h1>GET</h1> <h2>LED in IoT Device is now turned off</h2>'
        else:
            message = '<h2>Wrong Status</h2>'
        self.response(200, message)

    def proc_form_post(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode()
        print('body:', body)
        parsed_body = body.split('=')
        print('parsed_body:', parsed_body)
        status = parsed_body[1]
        if status == 'on':
            message = '<h1>POST</h1> <h2>LED in IoT Device is now turned on</h2>'
        elif status == 'off':
            message = '<h1>POST</h1> <h2>LED in IoT Device is not turend off</h2>'
        else:
            message = '<h2>Wrong Status</h2>'
        self.response(200, message)

    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body.encode())

httpd = HTTPServer(('localhost', 8080), http_handler)
print('Serving HTTP on {}:{}'.format('localhost', 8080))
httpd.serve_forever()