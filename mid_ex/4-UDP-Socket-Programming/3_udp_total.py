import argparse, socket, random
from ast import arg
from datetime import datetime

BUFFSIZE = 1024

def Server(ipaddr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipaddr, port))
    print('Waiting in {}...'.format(sock.getsockname()))
    while True:
        data, addr = sock.recvfrom(BUFFSIZE)
        if random.random() < prob:
            print('Message from {} is lost.'.format(addr))
            continue
        print('{} client message {!r}'.format(addr, data.decode()))
        text = 'The length is {} bytes.'.format(len(data))
        sock.sendto(text.encode(), addr)

def Client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    index = 1
    time = 0.1
    while True:
        data = str(datetime.now())
        sock.sendto(data.encode(), (hostname, port))
        print('({}) Waiting for {} sec'.format(index, time))
        sock.settimeout(time)
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except socket.timeout:
            time *= 2
            if time > 2.0:
                print('{}th packet is lost'.format(index))
                if index >= sending_counts:
                    break
                index += 1
                time = 0.1
        else:
            print('Server reply: {!r}'.format(data.decode()))
            if index >= sending_counts:
                break
            index += 1
            time = 0.1

if __name__ == '__main__':
    mode = {'c': Client, 's': Server}
    parser = argparse.ArgumentParser(description='Send and receive UDP packets with setting drop probability')
    parser.add_argument('role', choices=mode, help='which role to take between server and client')
    parser.add_argument('-s', default='localhost', help='server that client sends to')
    parser.add_argument('-p', type=int, default=2500, help='UDP port (default:2500)')
    parser.add_argument('-pr', type=float, default=0, help='dropping probability (0~1)')
    parser.add_argument('-cnt', type=int, default=10, help='number of sending packets')
    args = parser.parse_args()
    prob = args.pr
    sending_counts = args.cnt
    if args.role == 'c':
        mode[args.role](args.s, args.p)
    else:
        mode[args.role]('', args.p)
