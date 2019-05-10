from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("hello wold", "plain", "utf-8")

header_from = Header("李金邦<ljb5768@126.com>", "utf-8")
msg["From"] = header_from

header_to = Header("李金邦<ljb5768@126.com>", "utf-8")
msg["To"] = header_to

header_sub = Header("代码测试用", "utf-8")
msg["Subject"] = header_sub

from_addr = "ljb5768@126.com"
from_pwd = "ljb1234567"

to_addr = "ljb5768@126.com"
smtp_srv = "smtp.126.com"

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)

