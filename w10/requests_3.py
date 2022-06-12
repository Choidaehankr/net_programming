import requests

url = 'https://httpbin.org/put'
data = {'IoT': '2017'}
rsp = requests.put(url, data=data)
print(rsp.text)

rsp = requests.put(url, json=data)
print(rsp.text)

files = {'file': open('iot.png', 'rb')}
rsp = requests.put(url, files=files)
print(rsp.text)