import threading
import time

def func():
    print('i am running....')
    time.sleep(4)
    print('i am done....')

if __name__ == '__main__':
    t = threading.Timer(6, func) # 指定多少秒后，执行参数函数
    t.start()

    i = 0
    while True:
        print('{0}******'.format(i))
        time.sleep(3)
        i += 1