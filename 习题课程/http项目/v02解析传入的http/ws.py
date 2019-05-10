import socket


def getLine(skt):
    '''
    从socket读取某一行
    :param skt: object
    :return: 返回读取到的一行str格式内容
    '''
    '''
    前提：
    1. http协议传输内容是ascii编码 （utf-8兼容ascii）
    2. 真正传输的内容是通过网络流
    3. 回车换行：b'\r', b'\n',b表示一个bytes格式
    '''
    b1 = skt.recv(1)
    b2 = 0
    data = b''
    # 当没读到一行最后，也就是回车换行符号的时候，就执行循环
    while b2 != b'\r' and b1 != b'\n':
        b2 = b1
        b1 = skt.recv(1)
        data += bytes(b2)
    return data.strip(b'\r').decode()


def getHttpHead(skt):
    '''
    得到传入socket的http请求头
    :param skt: 通信的socket
    :return: 解析后的请求内容，字典形式
    '''
    # 读取某一行
    # 直到读取的行返回空行为止

    rst = {}

    line = getLine(skt)
    while line:
        '''
        判断得到的行是报头还是首部行，两个操作方法不一样
        算法是：
        1. 利用‘: ’作为分隔符，分割字符串
        '''
        r = line.split(r': ')

        if len(r) == 2:
            rst[r[0]] = r[1]
        else:
            r = line.split(r' ')
            rst['method'] = r[0]
            rst['url'] = r[1]
            rst['version'] = r[2]
        line =getLine(skt)
    return rst




# 理解两个参数的含义
# 理解创建一个socket的过程
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 注意addr的格式是tuple
# 以及tuple两个元素的含义
sock.bind(("127.0.0.1", 7852))
print('已经绑定端口....')

# 监听
sock.listen()
print("正在监听....")

# 接受一个传进来的socket
print("准备接受socket传入....")
skt, addr = sock.accept()
print("已经接受到传入socket:{0}".format(skt))

# 实际处理请求内容
a = getHttpHead(skt)
print(a)

# 读取传入的消息
# 需要注意读取的信息的长度一定要小于等于实际的信息的长度，否则会假死
msg = skt.recv(100)
print(type(msg))
print(msg.decode()) #默认utf-8

# 给对方一个反馈
msg_send = 'i am a student'
skt.send(msg_send.encode())

skt.close()
sock.close()



