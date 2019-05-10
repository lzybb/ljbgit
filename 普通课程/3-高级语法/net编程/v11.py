from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart("alternative")

html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            <h1> 测试使用的HTML格式邮件</h1>
            </body>
            </html>
        """
msg_html = MIMEText(html_content, "html", "utf-8")
msg.attach(msg_html)

msg_text = MIMEText("测试...", "plain", "utf-8")
msg.attach(msg_text)

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

