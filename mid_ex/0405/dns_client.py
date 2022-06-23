import socket
import struct
import sys

class DnsClient:
    def __init__(self, domainName):
        self.domainName = domainName

        # DNS Query Header