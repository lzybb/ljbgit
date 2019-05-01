import multiprocessing
from time import sleep, ctime

class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1. init构造函数
    2. run (一般不放入参数，会有点麻烦)
    '''
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print('The time is %s' % ctime())
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()

    # 做一个死循环，防止主进程结束
    while True:
        print('sleeping......')
        sleep(3)