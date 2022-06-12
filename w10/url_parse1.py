from urllib import parse

url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=iot'

parsed_url = parse.urlparse(url)

print(parsed_url)
print('scheme:', parsed_url.scheme)
print('netlock:', parsed_url.netloc)
print('path:', parsed_url.path)
print('params:', parsed_url.params)
print('query:', parsed_url.query)
print('fragment:', parsed_url.fragment)