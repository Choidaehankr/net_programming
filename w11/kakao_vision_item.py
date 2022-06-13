import requests
from PIL import Image, ImageDraw
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/product/detect'
REST_API_KEY = '665a8daf77a1fb743d8533e833f23547'

def detect_product(image_url):
    headers = {'Authorization' : 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'image_url' : image_url}
    resp = requests.post(API_URL, headers=headers, data=data)
    return resp.json()

def show_products(image_url, detection_result):
    image_rsp = requests.get(image_url)
    file_jpadata = BytesIO(image_rsp.content)
    image = Image.open(file_jpadata)

    draw = ImageDraw.Draw(image)
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1'] * image.width)
        y1 = int(obj['y1'] * image.height)
        x2 = int(obj['x2'] * image.width)
        y2 = int(obj['y2'] * image.height)

        draw.rectangle([(x1, y1), (x2, y2)], fill=None, outline = 'red', width = 2)
        draw.text((x1+5, y1+5), obj['class'], (255, 255, 0))
    del draw

    return image

if __name__ == "__main__":
    IMAGE_URL = 'https://p.kakaocdn.net/th/talkp/wmbOXVOIV9/aKtMoWYi4P4NrK5nrCodk0/s2rwz0_640x640_s.jpg'
    detection_result = detect_product(IMAGE_URL)
    image = show_products(IMAGE_URL, detection_result)
    image.show()