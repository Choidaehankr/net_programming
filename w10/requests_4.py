import requests

rsp = requests.delete('https://httpbin.org/delete')
print(rsp.text)
rsp = requests.head('https://httpbin.org/get')
print(rsp.headers)
print(rsp.text)