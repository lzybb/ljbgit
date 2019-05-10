# XPath
- 在XML文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp
# XPath 开发工具
- 开源的XPath工具表达式编辑工具：XMLQuire
- Chrome插件: XPath Helper
- Firefox插件：XPath Checker

# 选取节点
- nodename: 选取此节点的所有子节点
- /: 从根节点开始选取
            /Student:没有结果
            /School：选取School节点
- //: 选取节点，不考虑位置
            //age: 选取出三个节点，一般组成列表返回
- .: 选取当前节点
- ..：选取节点的父节点
- @: 选取属性
- xpath中查找一般按照路径方法查找，以下是路径表示方法
            School/Teacher:返回Teacher节点
            School/Student：返回两个Student节点(列表形式)
            //Student：选取所有Student的节点，不考虑位置
            School//Age：选取School后代中所有Age节点
            //@Other：选取Other属性
            //Age[@Detail]：选取带有属性Detail的Age元素
            
# 谓语-Predicates
- /School/Student[1]：选取School下面的第一个Student子节点
- /School/Student[last()]：选取School下面的最后一个Student子节点
- /School/Student[last()-1]:
- /School/Student[position()<3]：选取School下面的前两个Student节点
- //Student[@score]：选取带有属性Score的Student节点
- //Student[@score=‘99’]：选取带有属性Score并且值为99的Student节点
- - //Student[@score]/Age：选取带有属性Score的Student节点