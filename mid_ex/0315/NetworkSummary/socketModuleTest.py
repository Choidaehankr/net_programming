import socket
from struct import pack

name = socket.gethostname()  # 실행 중인 호스트 이름을 반환
# print(name)
# print(socket.gethostbyname(name))  # hostname을 IP4 주소로 변환
# print(socket.gethostbyname('homepage.sch.ac.kr'))
# print(socket.gethostbyname_ex('220.69.189.98'))
# print(socket.gethostbyaddr('220.69.189.98'))
# print(socket.getfqdn('220.69.189.98'))
# print(socket.getfqdn('www.daum.net'))
# print(socket.getfqdn('wwww.google.com'))

# 여러 사이트의 IP 주소 확인
# HOSTS = [
#     'www.sch.ac.kr',
#     'homepage.sch.ac.kr',
#     'www.daum.net',
#     'www.google.com',
#     'iot'
# ]
# for host in HOSTS:
#     try:
#         print('{} : {}'.format(host, socket.gethostbyname(host)))
#     except socket.error as msg:
#         print('{} : {}'.format(host, msg))

# 인터넷 서비스 이름에 대한 포트번호 반환
# print(socket.getservbyname('http'))
# print(socket.getservbyname('ftp'))
# print(socket.getservbyname('ssh'))
# print(socket.getservbyname('https'))

# 포트번호에 대한 인터넷 서비스 이름 반환
# print(socket.getservbyport(80))
# print(socket.getservbyport(25))
# for port in [80, 443, 21, 25, 143, 993, 110, 995]:
#     url = '{}://example.co.kr/'.format(socket.getservbyport(port))
#     print('{:4d}'.format(port), url)

# IP 주소 변환
# import binascii
# import socket
# import sys
# for string_address in ['114.71.220.95']:
#     packed = socket.inet_aton(string_address)
#     print('Original:', string_address)
#     print('Packed:', binascii.hexlify(packed))
#     print('Unpakced: ', socket.inet_ntoa(packed))

# 바이트 순서 변환

a = 1234
print(hex(a))

b = socket.htons(a)  # 호스트 바이트 순서 -> 네트워크 바이트 순서
print(hex(b))

c = socket.ntohs(b)  # 네트워크 바이트 순서 -> 호스트 바이트  순서
print(hex(c))