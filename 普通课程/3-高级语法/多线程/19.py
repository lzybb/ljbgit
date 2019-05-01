import multiprocessing
from time import sleep, ctime

def clock(i):
    while True:
        print('The time is %s' % ctime())
        sleep(i)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()
    # 做一个死循环，防止主进程结束
    while True:
        print('sleeping......')
        sleep(3)

