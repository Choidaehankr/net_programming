import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'mnnm0417@gmail.com'
recipient = 'rlaalstn3073a@gmail.com'
password = 'hecgdcywiqqpsdnv'

msg = EmailMessage()
msg['Subject'] = 'This is fortune mail.. from Europe 1661'
msg['From'] = sender
msg['To'] = recipient
text = 'qt'
msg.set_content(text)

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
