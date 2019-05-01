import time
import threading


def loop1(in1):
    print('start loop 1 at:',time.ctime())
    print('我是参数',in1)
    time.sleep(4)
    print('end loop 1 at',time.ctime())

def loop2(in1,in2):
    print('start loop 2 at :',time.ctime())
    print('我是参数',in1, '和参数',in2)
    time.sleep(2)
    print('end loop 2 at:',time.ctime())

def main():
    print('starting at:', time.ctime())
    t1 = threading.Thread(target=loop1, args=('ljb',))
    t2 = threading.Thread(target=loop2, args=('lzy','zjy'))
    t1.start()
    t2.start()
    print('all done at:', time.ctime())

if __name__ == '__main__':
    main()
