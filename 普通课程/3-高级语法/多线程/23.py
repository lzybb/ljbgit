import multiprocessing
from time import ctime

# 设置哨兵问题
def consumer(input_q):
    print('into consumer:', ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print('pull', item, 'out of q')
    print('out of consumer:', ctime()) ## 此句执行完，再转入主程序

def producer(sequence, output_q):
    print('into producer:', ctime())
    for item in sequence:
        output_q.put(item)
        print('put', item, 'into q')
    print('out of producer:', ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    q.put(None)
    cons_p.join()
