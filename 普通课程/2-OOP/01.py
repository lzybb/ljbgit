
'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class student():
    # 一个空类，pass代表直接跳过
    #此处pass必须有
    pass

# 定义一个对象
ljb = student()

# 再定义一个类，用来描述学Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 36
    course = 'Python'
    # 需要注意
    # 1，def doHomework的缩进层级
    # 2，系统默认有一个self参数
    def doHomework(self):
        print('学习中')
        # 函数末尾推荐使用return语句
        return None

# 实例化一个叫zj的学生，是一个具体的人
zj = PythonStudent()
print(zj.name)
print(zj.age)
# 注意成员函数的调用没有传递进入参数
zj.doHomework()
# 备注：检验 git 传送3.0


