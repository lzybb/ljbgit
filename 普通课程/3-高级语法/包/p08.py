'''
import pkg01.b01

pkg01.b01.sayHello()
# b01.sayHello() 此处必须要写全名称来源

s1 = pkg01.b01.Student('lzy',6)
s1.say()
'''

'''
import pkg01.b01 as b
s1= b.Student('zjy',2)
s1.say()

'''

'''
import pkg01

# s1=pkg01.b01.Student()
# s1.say()
# pkg01.__init__.inInit()
pkg01.inInit()
# 只导入包名，只能导入到默认的__init__的模块中；
# 并且此模块名不能表示出来，不然会报错
'''

'''
from pkg01 import b01

b01.sayHello()
# 此种导入方式不执行__init__的内容
# 此种导入方式不需要写全模块名的来源
'''