# import ipaddress

# addr4 = ipaddress.ip_address('192.0.2.1')
# print(addr4)
# print(addr4.version)
# addr6 = ipaddress.ip_address('2001:A8::1')
# print(addr6)
# print(addr6.version)

import ipaddress
net = ipaddress.ip_network('114.71.220.0/24')
print(net)
print(net.with_netmask)
print(net.num_addresses)

# 네트워크에서 사용 가능한 호스트 주소 알아보기
for x in net.hosts():
    print(x)

