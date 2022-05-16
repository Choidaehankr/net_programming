from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse,request
import requests, json
import cv2

# REST_API_KEY = '0d31644dbd291f49ff894526df554d2d'
REST_API_KEY = '665a8daf77a1fb743d8533e833f23547'

class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()

    def route(self):
        parsed_path = parse.urlparse(self.path)
        real_path = parsed_path.path
        if real_path == '/':
            self.send_html()
        elif real_path == '/oauth':
            self.process_oauth()
        else:
            self.response(404, 'Not Found')

    def send_html(self):
        self.send_response(200)
        self.end_headers()
        with open('index_kakao.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def process_oauth(self):
        parsed_path = parse.urlparse(self.path)
        query = parsed_path.query
        parsed_query = parse.parse_qs(query)
        authorize_code = parsed_query['code']
        print(authorize_code)
        self.response(200, 'Kakao authentication is successful.')

        # access token과 refresh token 얻기
        token_api_url = 'https://kauth.kakao.com/oauth/token'
        data = {'grant_type': 'authorization_code',
                'client_id': REST_API_KEY,
                'redirect_uri': 'http://localhost:8888/oauth',
                'code': authorize_code}
        rsp = requests.post(token_api_url, data=data)
        rsp_json = json.loads(rsp.text)
        access_token = rsp_json['access_token']
        refresh_token = rsp_json['refresh_token']
        print('access_token:', access_token)
        print('refresh_token:', refresh_token)

        # 카카오톡 프로필 가져오기
        profile_url = 'https://kapi.kakao.com/v1/api/talk/profile'
        header = {'Authorization': 'Bearer ' + access_token}
        rsp = requests.get(profile_url, headers=header)
        json_profile = rsp.json()
        print(json_profile)
        image_path = 'profile.jpg'
        
        request.urlretrieve(json_profile['profileImageURL'], image_path)

        talk_url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
        header = {'Authorization': 'Bearer ' + access_token}
        template_object = {
                                "object_type": "text",
                                "text": "카카오 API 정말 쉽구나!",
                                "link":
                                {
                                    "web_url": "https://home.sch.ac.kr/iot",
                                    "mobile_web_url": "https://home.sch.ac.kr/iot"
                                }
                            }
        template_object_json = json.dumps(template_object)
        data = {'template_object': template_object_json}
        rsp = requests.post(talk_url, headers=header, data=data)
    
    def response(self, status_code, body): # 응답 메시지 전송 함수
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(body.encode())

httpd = HTTPServer(('localhost', 8888), http_handler)
print('Serving HTTP on {}:{}'.format('localhost', 8888))
httpd.serve_forever()