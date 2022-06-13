import smtplib
from email.message import EmailMessage
import filetype

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'mnnm0417@gmail.com'
reciptient = 'mnnm22@naver.com'
password = 'hecgdcywiqqpsdnv'
family = ['choikorea88@sch.ac.kr', 'mnnm22@naver.com', 'mnnm0417@gmail.com', 'rlaalstn3073a@gmail.com']

msg = EmailMessage()
msg['Subject'] = '대하니의 메일'
msg['From'] = sender
msg['To'] = ', '.join(family)
msg.set_content('시험 6시간 전 파멸적 벼락치기')
msg.preamble = 'You will not see this in a MINE-aware mail reader.\n'

with open('profile.jpg', 'rb') as f:
    img_data = f.read()

msg.add_attachment(img_data, maintype='image', subtype=filetype.guess_mime(img_data), filename='test.jpg')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
