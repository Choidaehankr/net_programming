import smtplib
from email.message import EmailMessage
from openpyxl import load_workbook

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'mnnm0417@gmail.com'
password = 'hecgdcywiqqpsdnv'

load_wb = load_workbook('email_list.xlsx')

load_ws = load_wb['Sheet1']
for row in load_ws.rows:
    recipient = row[0].value

    msg = EmailMessage()
    msg['Subject'] = '대한 공지'
    msg['From'] = sender
    msg.set_content('A쁠 맞고싶다..힝')
    msg['To'] = recipient

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.send_message(msg)
    s.quit()
