import socket

def tcp_clt():
    #  1. 建立通信socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 链接对方，请求根对方建立通路
    addr = ('127.0.0.1', 9876)
    sock.connect(addr)
    # 3.发送内容到对方服务器
    msg = "测试tcp通信"
    sock.send(msg.encode())

    rst = sock.recv(500)
    print(rst.decode())
    sock.close()

if __name__ == '__main__':
    tcp_clt()