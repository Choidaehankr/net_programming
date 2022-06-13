import json
import cv2
import requests

LIMIT_PX = 1024
LIMIT_BYTE = 1024*1024
LIMIT_BOX = 40

# pixel 제약사항 체크 함수. 초과할 경우 resize 수행
def kakao_ocr_resize(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        cv2.imwrite(image_path, image)

        return image_path
    return None

def kakao_ocr(image_path, rest_api_key): # OCR 수행 함수
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

    headers = {'Authorization': 'KakaoAK {}'.format(rest_api_key)}

    return requests.post(API_URL, headers=headers, files={"image": open(image_path, 'rb')})


def main():
    image_path = 'myimage.jpg'
    REST_API_KEY = '665a8daf77a1fb743d8533e833f23547'

    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        print('원본 대신 리사이즈된 이미지를 사용합니다.')

    output = kakao_ocr(image_path, REST_API_KEY).json()
    print("[OCR] output:\n{}\n".format(output))

if __name__ == "__main__":
    main()