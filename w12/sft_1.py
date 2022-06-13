import paramiko
import getpass

transport = paramiko.Transport(('114.71.220.5', 22))

user = input('Username: ')
pwd = getpass.getpass('Passowrd: ')
transport.connect(username=user, password=pwd)

sftp = paramiko.SFTPClient.from_transport(transport)

src_file_path = 'test/iot.txt'
dst_file_path = src_file_path.split('/')[1]
sftp.get(src_file_path, dst_file_path)  # 원격에 있는걸 로컬로

src_file_path = 'index.html'
dst_file_path = src_file_path
sftp.put(src_file_path, dst_file_path)  # 로컬을 원격으로

sftp.close()
transport.close()