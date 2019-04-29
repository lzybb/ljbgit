import ftplib
import os

host = 'ftp.acc.umu.se'
dir = 'Public/EFLIB'
file = "README"

try:
    f = ftplib.FTP()
    f.set_debuglevel(2)
    f.connect(host)
except Exception as e:
    print(e)
    exit()

try:
    f.login()
except Exception as e:
    print(e)
    exit()

try:
    f.cwd(dir)
except Exception as e:
    print(e)
    exit()

try:
    f.retrbinary('RETR {0}'.format(file), open(file, 'wb').write)
except Exception as e:
    print(e)
    exit()

f.quit()





