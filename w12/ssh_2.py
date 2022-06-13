import getpass
import paramiko
import time

BUFF_SIZE = 65535

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy) 

user = input('Username: ')
pwd = getpass.getpass('Password: ') 

cli.connect('114.71.220.5', username=user, password=pwd)
channel = cli.invoke_shell()

# 채널을 통해 명령어 전송 
channel.send('cat /proc/cpuinfo\n')
time.sleep(0.5)
channel.send('cat /proc/meminfo\n') 
time.sleep(0.5)
channel.send('mkdir test2\n') 
time.sleep(0.5)
channel.send('cd test2\n') 
time.sleep(0.5)
channel.send('echo iot > iot.txt\n') 
time.sleep(0.5)
channel.send('cat iot.txt\n') 
time.sleep(0.5)

# 새로운 셸 세션(channel) 생성
output = channel.recv(BUFF_SIZE).decode() # 명령어 실행결과를 수신 print(output)
print('output:', output)
cli.close()