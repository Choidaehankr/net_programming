import requests

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
REST_API_KEY = '665a8daf77a1fb743d8533e833f23547'

headers = {'Authorization' : 'KakaoAK {}'.format(REST_API_KEY)}
files = {'image' : open('myimage.jpg', 'rb')}
rsp = requests.post(API_URL, headers=headers, files=files)
print(rsp.json())