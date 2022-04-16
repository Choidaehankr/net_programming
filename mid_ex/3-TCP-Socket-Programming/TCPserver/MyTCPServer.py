class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)

    def Accepting(self):
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr

if __name__ == '__main__':
    sock = TCPServer(8888)
    c, addr = sock.Accepting()
    print('connected by ', addr)
    c.send(b'Hello Client')
    c.close()