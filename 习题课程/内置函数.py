# 数学模块
import math  # （F4 键查看源码）
# print(math)
'''
# celi() 向上取整操作
print(math.ceil(5.6))
print (math.ceil(3.1))

# floor() 向下取整操作
print(math.floor(4.2))
'''
'''
# 查看系统关键字
import keyword
print(keyword.kwlist)

# round 四舍五入  # python内置函数
print(round(3.6))
print(round(2.4))

# sqrt() 开平方 返回浮点数
print(math.sqrt(81))
print(math.sqrt(0.5))

# pow 与幂运算差不多，计算一个数的几次方
print(math.pow(3,2)) # 返回浮点型
print(3**2)  # 返回整数

# fabs() 获取绝对值 （|x|）,返回浮点数
print(math.fabs(-1)) # 返回浮点数
print(math.fabs(0))

# abs()获取绝对值，不是数学模块当中的，是python内置函数,返回值由参数决定
print(abs(-1))
print(abs(-1.2))


# fsum() 对整个序列求和（数学模块内）返回浮点数
print(math.fsum([1,2,3,4,5]))

# sum() python内置函数 返回值由参数决定
print(sum([1,2,3,4,5]))


# math.modf() 将一个浮点数拆分为整数和小数组成元组
print(math.modf(4.5))
print(math.modf(3))
print(math.modf(0))
# 小数部分在前，整数在后

help(math.modf)


# copysign() 将第二个数的符号（±号）传给第一个数
print(math.copysign(2,-2))
print(math.copysign(-2,2))
# 返回第一个值的浮点型

print(math.e)
print(math.pi)
'''
# 随机数模块
import  random
# random() 获取0-1之间的随机小数，包含0不包含1 [0,1)
'''
for i in range(10):
      print(random.random()) # 不需要参数
      print(random.randint(3,10))
      print(random.randrange(1,20,3))
'''
# random.randint(a,b) 随机获取【a-b】之间的整数值
      # int指整数

# random.randrange(a,b，c) 获取[a,b)之间的整数值，可以指定间隔c
'''
# choice() 随机获取列表中的值
print(random.choice([1,3,4,5,6,7,7,32,9,4]))

# shuffle() 随机打断序列,返回值是None
list1 = [1,2,3,4,5,6,7,8]
print(list1)
random.shuffle(list1)
print(list1)

# uniform() 随机获取指定范围内的值（可以包括小数）
for i in range(10):
    print(random.uniform(1,9))
'''
