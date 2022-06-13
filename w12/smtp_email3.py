import smtplib
from email.message import EmailMessage
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'mnnm0417@gmail.com'
password = 'hecgdcywiqqpsdnv'

msg = EmailMessage()
msg['Subject'] = 'HTML 메시지 전송'
msg['From'] = sender
msg['To'] = ('mnnm22@naver.com', 'rlaalstn3073a@gmail.com')

content_id = 'my_image1'
# msg.add_alternative('''\
# <html>
#     <head></head>
#     <body>
#         <p>안녕하세요.</p>
#         <p>순천향대학교 최대한이다!!!</p>
#         <p>아래 사이트 확인 부탁드립니다.</p>
#         <p>
#             <a href="https://home.sch.ac.kr/iot/>
#                 순대 사물과다!
#             </a>
#         </p>
#         <p>감사하다!!</p>
#         <img src="cid:{cid}" />
#     </body>
# </html>
# '''.format(cid=content_id), subtype='html')

msg.add_alternative('''\
<html>
  <head></head>
  <body>
<p>안녕하세요.</p>
<p>순천향대학교 김대희입니다.</p> <p>아래 사이트 확인 부탁 드립니다.</p> <p>
<a href=https://home.sch.ac.kr/iot/> 순천향대학교 사물인터넷학과
</a> </p>
<p>감사합니다.</p>
    <img src="cid:{cid}" />
  </body>
</html>
'''.format(cid=content_id), subtype='html')

with open('profile.jpg', 'rb') as img:
    msg.get_payload()[0].add_related(img.read(), maintype='image', subtype='jpg', cid=content_id)

with open('outgoing.msg', 'wb') as f:
    f.write(bytes(msg))

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
