import ipaddress as ipaddr

# addr4 = ipaddr.ip_address('192.0.2.1')  # IP 주소 객체를 생성하는 함수
# print(addr4)

# addr6 = ipaddr.ip_address('2001:A8::1')
# print(addr6)

# print(addr4.version)
# print(addr6.version)

net = ipaddr.ip_network('114.71.220.0/24')  # 네트워크 주소 객체를 생성
# print(net.with_netmask)
# print(net.num_addresses)
# print(net.netmask)
# print(net.hostmask)

# for x in net.hosts():  # 네트워크에서 사용 가능한 호스트 주소 알아보기
#     print(x)

# addr = ipaddr.ip_address('114.71.220.95') # True
# addr = ipaddr.ip_address('192.169.0.1')  # False
# print(addr in net)
