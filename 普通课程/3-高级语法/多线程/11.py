import threading

sum = 0
loopSum = 10000000

def myAdd():
    global sum, loopSum
    for i in range(1,loopSum):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ == '__main__':

    '''
    myAdd()
    print(sum)
    myMinu()
    print(sum)
    '''
    print('starting ...{0}'.format(sum))
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu(), args=())

    t1.start()
    t2.start()

    t1.join()
    print(sum)
    t2.join()
    print('done....{0}'.format(sum))
