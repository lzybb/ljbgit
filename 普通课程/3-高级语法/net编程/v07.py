# 导入相应的包
import smtplib
from email.mime.text import  MIMEText
# MIMRText三个主要参数
# 1. 邮件内容
# 2. MIME子类型，在此案例中我们用plain表示text类型
# 3. 邮件编码格式

msg = MIMEText("Hello, i am xxx", "plain", "utf-8")

# 发件人的email地址和密码
from_addr = "ljb5768@126.com"
from_pwd = "ljb1234567"

# 收件人信息
to_addr = "ljb5768@126.com"

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，需要开启授权选项
# 126邮箱的smtp地址是：smtp.126.com  端口号：25

smtp_srv = "smtp.126.com"

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) #SMTP协议默认端口25
    # 465端口为默认的安全访问的端口（发件端）
    # 登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1.发送地址
    # 2. 接受地址，必须是list形式
    # 3. 发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)

