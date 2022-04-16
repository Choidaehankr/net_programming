import socket
import struct
import binascii
from turtle import st

class Iphdr:
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45
        self.tos = 0
        self.tot_len = tot_len
        self.id = 0
        self.frag_off = 0
        self.ttl = 127
        self.protocol = protocol
        self.check = 0
        self.saddr = socket.inet_aton(saddr)
        self.daddr = socket.inet_aton(daddr)
    
    def pack_Iphdr(self):
        packed = b''
        packed += struct.pack('!BBH', self.ver_len, self.tos, self.tot_len)
        packed += struct.pack('!HH', self.id, self.frag_off)
        packed += struct.pack('!BBH', self.ttl, self.protocol, self.check)
        packed += struct.pack('!8s', self.saddr + self.daddr)
            # same code
        # packed += struct.pack('!4s4s', self.saddr, self.daddr)
            # same code
        # packed += struct.pack('!4s', self.saddr)
        # packed += struct.pack('!4s', self.daddr)
        return packed

ip = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')
packed_iphdr = ip.pack_Iphdr()
print(binascii.b2a_hex(packed_iphdr))