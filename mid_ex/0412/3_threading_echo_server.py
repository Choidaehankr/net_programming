# 기존에 만든 echo 프로그램은 한 서버에 여러 개의 클라이언트 연결을 못함.
# 기존에 만든 echo_client로 실행

# 멀티스레드 에코 서버: threading.Thread 클래스


from socket import *
import threading

port = 2500
BUFSIZE = 1024

def echoTask(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        print('Received message:', data.decode())
        sock.send(data)
    sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    th = threading.Trhead(target=echoTask, args=(conn,))
    th.start()