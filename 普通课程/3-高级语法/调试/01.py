def sayHello(name):
    print('我想和你说:hello,{} '.format(name))
    print('hello, {}'.format(name))
    print('done......')

if __name__ == '__main__':
    print('*'*30)
    name = input('请输入你的名字：')
    print(sayHello(name=name))
    print('@'*30)