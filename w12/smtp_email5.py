from fileinput import filename
import smtplib
from email.message import EmailMessage
import zipfile
import os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'mnnm0417@gmail.com'
recipient = 'mnnm22@naver.com'
password = 'hecgdcywiqqpsdnv'


zf_name = 'email.zip'  # 이 이름으로 생성됨
folder = 'test'


zf = zipfile.ZipFile(zf_name, 'w')
print('Zipping current dir', folder)
for dirs, subdirs, files in os.walk(folder):
    zf.write(dirs)
    for file in files:
        zf.write(os.path.join(dirs, file))
zf.close()


msg = EmailMessage()
msg['Subject'] = 'Source code'
msg['From'] = sender
msg['To'] = recipient

with open(zf_name, 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='zip', filename='e_mail.zip')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
