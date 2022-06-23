import requests
import json

url = 'https://httpbin.org/post'

data = {'ID': '20171539', 'Name': 'Daehan Choi', 'Department': 'IoT'}
rsp = requests.post(url, json=data)
print(rsp.text)
json_data = json.loads(rsp.text)
print(json_data['json'])