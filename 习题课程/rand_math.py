import random
import math
import string

'''
# 输入函数
num = input("请输入一个三位数：")
# 检测输入是否是纯数字
if num.isdigit():
    # 输入函数输入的是字符类型，不强制转换会报错
    if 100 <= int(num) <= 999:  # int()转换成整数，str()转换成字符
        print("在里面")
    else:
        print("超出范围了")

else:
    print("请按规定输入整数")
'''

'''
输入一个三位数与程序随机数比较大小
1.如果大于程序随机数，则分别输出这个三位数的个位\十位\百位
2.如果等于程序随机数，则提示中奖，记100分
3.如果小于程序随机数，则将120个字符输入到文本文件中
    （规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后8个是数字）
'''
# 以下为自编
'''
def fun():
    num = input("请输入一个三位数：")
    if num.isdigit() and 99 <= int(num) <= 999:
        n1 = random.randrange(100,1000)
        num = int(num)
        if num > n1:
            print(num % 10, end = ' ')
            print((num//10)%10, end = ' ')
            print(num//100)
        if num == n1:
            print("哇！！！中大奖啦！记100分")
        else:
            file_sy = open('E://xx//PycharmProjects//others//wj1.txt', 'w')
            s = string.ascii_letters
            for i in range(10):
                for k in range(12):
                    if k < 4:
                        v = random.choice(s)
                        file_sy.write(v)
                    else:
                        v = str(random.randrange(1,10))
                        file_sy.write(v)

                file_sy.write('\n')
            file_sy.close()
            print("文件已创建")
    else:
        print("请按规定输入")

fun()
'''

def num_game(cs,df):
    while 1:
        # 以下为讲课程序
        def line():
            str_num = ''
            for i in range(4):
                num = random.randrange(97,123)
                # 将ascii值转换成对应的字母
                str_s = chr(num)
                str_num = str_s + str_num
            for i in range(8):
                num = random.randrange(0,10)
                str_num = str_num + str(num)
            return str_num
        num = input("请输入一个三位数，输入-1结束：")
        random_num = random.randrange(100,1000)
        if num == '-1':
            break
        if num.isdigit() and 100<= int(num)<=999:
            cs += 1
            print('目前已抽奖{}次'.format(cs))
            num = int(num)
            if num > random_num:
                bai = num//100
                shi = (num%100)//10
                ge = num%10
                print('运气不错，随机数为{0}'.format(random_num))
                print('这个三位数的个位是{0},十位是{1},百位是{2}'.format(ge,shi,bai))

            if num == random_num:
                df += 1

                print("你中奖了，目前得分是{}".format(df*100))
                print("目前中奖的概率为：{}".format(df/cs))
            if num < random_num:
                f = open('str_num.txt', 'w')
                for i in range(10):
                    str_line = line()
                    f.write(str_line+'\n')
                f.close()

                print('运气不行，比随机数{}小'.format(random_num))
                print('已经抄写10遍')
        else:
            print("请按规定输入")
# 程序入口
if __name__ == '__main__': # 调试代码
    print('自己调用')
    df = 0
    cs = 0
    num_game(cs,df)
# 在本身模块中__name__ == __main__，当第三方导入的时候__name__ == 文件名


