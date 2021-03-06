import socket

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
