from email.mime.text import MIMEText # 构建附件使用
from email.mime.multipart import MIMEBase, MIMEMultipart
# 构建基础邮件使用

mail_mul = MIMEMultipart()
# 构建邮件正文
mail_text = MIMEText("hello, i am xxx", "plain", "utf-8")
# 把构建好的邮件正文附件加入邮件中
mail_mul.attach(mail_text)

# 构建附加
# 构建附件，需要从本读入附件
# 打开一个本地文件
# 以rb格式打开
with open("1.html", "rb") as f:
    s = f.read()
    # 设置附件的MIME和文件名
    m = MIMEText(s, "base64", "utf-8")
    m["Content-Type"] = "application/octet-stream"
    # 需要注意
    # 1. attachment 分号后为英文状态
    # 2. filename 后面需要用引号包裹，注意与外面引号错开
    m["Content-Disposition"] = "attachment; filename='1.html'"
    # 添加到MIMEMultipart
    mail_mul.attach(m)

from_addr = "ljb5768@126.com"
from_pwd = "ljb1234567"
to_addr = "ljb5768@126.com"
smtp_srv = "smtp.126.com"

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)

