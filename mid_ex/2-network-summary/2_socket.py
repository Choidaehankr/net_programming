import socket

socket.gethostname()  # 실행 중인 호스트 이름을 반환
# socket.gethostbyname(hostnam) # hostname을 IPv4 주소로 반환


# 18p. 여러 사이트의 IP 주소를 확인

# HOSTS = [
#     'www.google.com',
#     'www.sch.ac.kr',
#     'www.naver.com',
#     'www.daum.net'
# ]

# for host in HOSTS:
#     try:
#         print('{} : {}'. format(host, socket.gethostbyname(host)))
#     except socket.error as msg:
#         print('{} : {}'. format(host, msg))

# 19p. 인터넷 서비스 정보 알아내기

# print(socket.getservbyport(80))
# print(socket.getservbyport(25))

# for port in [80, 443, 21, 25, 143, 993, 110, 995]:
#     url = '{}://excample.co.kr/'.format(socket.getservbyport(port))
#     print('{:4d}'.format(port), url)

    # 24p. 바이트  순서 변환 함수

a = 1234
print(hex(a))

b = socket.htons(a)  # 2바이트 양의 정수를 호스트 바이트 순서에서 네트워크 바이트 순서로 변환

print(hex(b))

c = socket.ntohs(b)  # 2바이트 양의 정수를 네트워크 바이트 순서에서 호스트 바이트 순서로 변환
print(hex(c))