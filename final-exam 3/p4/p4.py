from turtle import ht
from urllib import request
import re
import requests

url = 'https://home.sch.ac.kr/iot/'
rsp = requests.get(url)
html = rsp.text
results = re.findall(r'(<div id="footer">)([\s\S]+?)(</div)', html)
index = results[0]
temp = index[1]
index_list = re.findall(r'(<span>)([\s\S]+?)(</span>)', temp)

answer = []

for index in index_list:
    # print(index[1])
    s = re.findall(r'\d{3}-\d{3,4}-\d{4}', index[1])
    t = re.findall(r'([\w.]+)(@)(.+)(\.[a-z]{2,3})', index[1])
    # print(type(index[1]))
    if len(s) != 0:
        # print('s:', s)
        print(''.join(s))
    elif len(t) != 0:
        # print('t:', t)
        print(''.join(t[0]))