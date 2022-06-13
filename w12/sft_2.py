import paramiko
import getpass

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)

sftp = ssh.open_sftp()

src_file_path = 'index_get.html'
dst_file_path = 'test/' + src_file_path
sftp.put(src_file_path, dst_file_path)

src_file_path = dst_file_path
dst_file_path = 'index_get1.html'
sftp.get(src_file_path, dst_file_path)

sftp.close()
ssh.close()