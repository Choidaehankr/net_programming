import requests

API_URL_1 = 'https://dapi.kakao.com/v2/translation/translate'
API_URL_2 = 'https://dapi.kakao.com/v3/translation/language/detect'
REST_API_KEY = '665a8daf77a1fb743d8533e833f23547'



def detect_language_get(text):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'query': text}
    rsp = requests.get(API_URL_2, headers=headers, params=data)
    return rsp.json()

def detect_language_post(text):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'query': text}
    rsp = requests.post(API_URL_2, headers=headers, data=data)
    return rsp.json()

def translate_get(text, src_lang):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'src_lang': src_lang, 'target_lang': 'fr', 'query': text}
    rsp = requests.get(API_URL_1, headers=headers, params=data)
    return rsp.json()


def translate_post(text, src_lang):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'src_lang': src_lang, 'target_lang': 'fr', 'query': text}
    rsp = requests.post(API_URL_1, headers=headers, data=data)
    return rsp.json()


if __name__ == "__main__":
    while True:
        text = input('Enter the sentence to translate: ')
        if text != 'q':
            # detect_output = detect_language_get(text)
            detect_output = detect_language_post(text)
            print('detect_output:', detect_output)
            detect_lang = detect_output['language_info'][0]['code']
            translated_text = translate_post(text, detect_lang)
            # translated_text = translate_get(text, detect_lang)
            print(translated_text)
            print('[POST]', translated_text['translated_text'][0][0], '\n')
        else:
            break