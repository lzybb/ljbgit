import threading
from time import sleep, ctime

loop = [4,2]

class ThreadFunc():
    def __init__(self, name):
        self.name = name
    def loop(self, nloop, nsec):
        '''
        :param nloop: loop函数的名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print('start loop ', nloop, ' at ', ctime() )
        sleep(nsec)
        print('done loop ', nloop, ' at ', ctime())

def main():
    print('starting at: ', ctime())
    t = ThreadFunc('loop')
    t1 = threading.Thread(target=t.loop, args=('loop1', 4))
    # 下面这种写法更西方化，工业一点
    t2 = threading.Thread(target=ThreadFunc('loop').loop, args=('loop2', 2))

    # 常见错误写法
    #t1 = threading.Thread(target=ThreadFunc('loop').loop(100,4))
    #t1 = threading.Thread(target=ThreadFunc('loop').loop(200,2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('all done at:',ctime())

if __name__ == '__main__':
    main()

