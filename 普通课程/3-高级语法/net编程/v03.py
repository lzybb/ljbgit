import socket
def serverFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('127.0.0.1', 7852)
    sock.bind(addr)

    data, addr = sock.recvfrom(500)

    print(data)
    print(type(data))

    text = data.decode()
    print(type(text))
    print(text)
    rsp = 'i am not hungry'

    data = rsp.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    while True:
        try:
            serverFunc()
        except Exception as e:
            print(e)
        time.sleep(1)