# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self,name='Nome',age=18):
        self.name=name
        self.age=age

    def say(self):
        print('我的名字叫{}'.format(self.name))

def sayHello():
    print('Hi,欢迎来学习！')