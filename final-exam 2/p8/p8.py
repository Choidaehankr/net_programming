import requests
from PIL import Image, ImageFilter
from io import BytesIO
API_URL = 'https://dapi.kakao.com/v2/vision/thumbnail/crop'
REST_API_KEY = '665a8daf77a1fb743d8533e833f23547'

def detect_face():
    headers = {'Authorization' : 'KakaoAK {}'.format(REST_API_KEY)}
    files = {'image_url' : 'https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/07.jpg', 'width': 200, 'height': 200}

    rsp = requests.post(API_URL, headers=headers, data=files)
    result = rsp.json()
    rsp_url = result['thumbnail_image_url']
    image_rsp = requests.get(rsp_url)
    file_jpgdata = BytesIO(image_rsp.content)
    image = Image.open(file_jpgdata)
    image.show()


if __name__ == "__main__":
    detection_result = detect_face()