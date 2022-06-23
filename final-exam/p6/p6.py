from urllib import parse
import requests

url = 'https://search.naver.com/search.naver?query=iot'
parsed_url = parse.urlparse(url)
print(parsed_url)

tmp = parse.urljoin('https://search.naver.com/search.naver', '')
print(tmp)

payload = {'query': 'iot'}
rsp = requests.get(tmp, params=payload)
print(rsp.headers)
