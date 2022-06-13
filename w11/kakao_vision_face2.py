import requests
from PIL import Image, ImageFilter

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'
REST_API_KEY = '665a8daf77a1fb743d8533e833f23547'

def detect_face(filename):
    headers = {'Authorization' : 'KakaoAK {}'.format(REST_API_KEY)}
    files = {'image' : open(filename, 'rb')}
    rsp = requests.post(API_URL, headers=headers, files=files)
    return rsp.json()


def mosaic(filename, detection_result):
    image = Image.open(filename)

    for face in detection_result['result']['faces']:
        x = int(face['x'] * image.width)
        y = int(face['y'] * image.height)
        w = int(face['w'] * image.width)
        h = int(face['h'] * image.height)
        box = image.crop((x, y, x + w, y + h))
        # 모자이크 처리
        box = box.resize((20, 20), Image.Resampling.NEAREST).resize((w, h), Image.Resampling.NEAREST)
        image.paste(box, (x, y, x + w, y + h))
    return image

if __name__ == "__main__":
    IMAGE = 'myimage.jpg'
    detection_result = detect_face(IMAGE)
    image = mosaic(IMAGE, detection_result)
    image.show()