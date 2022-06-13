import paramiko
import getpass

filename = 'test.zip'
dirname = '/home/net_pro/test'
CMD = 'zip -r ' + filename + ' ' + dirname

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)

stdin, stdout, stderr = ssh.exec_command(CMD)

sftp = ssh.open_sftp()

sftp.get(filename, filename)

sftp.close()
ssh.close()