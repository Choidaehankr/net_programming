import getpass
import paramiko

PORT = 22

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input('Username: ')
pwd = getpass.getpass('Password: ')

cli.connect('114.71.220.5', port=22, username=user, password=pwd)
stdin, stdout, stderr = cli.exec_command('cat /proc/cpuinfo')
lines = stdout.readlines()
print(''.join(lines))

stdin, stdout, stderr = cli.exec_command('cat /proc/meminfo')
lines = stdout.readlines()
print(''.join(lines))

cli.close()