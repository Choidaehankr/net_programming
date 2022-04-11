import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src, dst, len, check):  # 송신/수신/패킷/쳌섬
        self.tot_len = len
        self.protocol = 17
        self.checksum = check
        self.srcPort = src
        self.dstPort = dst

    def pack_udphdr(self):
        packed = b''
        packed += struct.pack('!2H', self.srcPort, self.dstPort)
        packed += struct.pack('!2H', self.tot_len, self.checksum)
        return packed

def unpack_udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:8])
    return unpacked
    
def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]
        

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_udphdr()

unpacked_udphdr = unpack_udphdr(packed_udphdr)

print(binascii.b2a_hex(packed_udphdr))
print(unpacked_udphdr)

print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))