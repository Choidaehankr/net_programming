from urllib import parse

url = 'https://home.sch.ac.kr/sch/06/090000.jsp?mode=view&article_no=20220421103054467019&board_wrapper=%2Fsch%2F06%2F090000.jsp&pager.offset=0&board_no=20200302132057325672'

parsed_url = parse.urlsplit(url)
print(parsed_url)
print('scheme:', parsed_url.scheme)
print('netlock:', parsed_url.netloc)
print('path:', parsed_url.path)
print('query:', parsed_url.query)
print('fragment:', parsed_url.fragment)