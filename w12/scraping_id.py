import re
import requests

url = 'http://goo.gl/U7mSQl'

rsp = requests.get(url)
html = rsp.text
# results = re.findall(r'[\w0-9]+\*\*\*', html)
# results = re.findall(r'[A-Za-z0-9]+\*\*\*', html)
# results = re.findall(r'[A-Z-a-z0-9]+\*\*\*', html)
results = re.findall(r'[\w0-9]+\*\*\*', html)

for id in results:
    print(id)