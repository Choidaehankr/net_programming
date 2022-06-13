import requests
import re

url = 'https://finance.naver.com/item/main.naver?code=005930'
rsp = requests.get(url)
html = rsp.text

stock_results = re.findall(r'(<dl class="blind">)([\s\S]+?)(</dl>)', html)
samsung_stock = stock_results[0]
print('samsung_stock:', samsung_stock)
samsung_index = samsung_stock[1]
print('samsung_index:', samsung_index)

index_list = re.findall(r'(<dd>)([\s\S]+?)(</dd>)', samsung_index)

for index in index_list:
    # print(index[0] + index[1])
    print(index[1])