import xml.dom.minidom
# 负责解析xml文件
from xml.dom.minidom import parse

# 使用minidom打开xml文件
domtree = xml.dom.minidom.parse("student.xml")
# 得到文档对象
doc = domtree.documentElement

# 显示子元素
for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("-----Node:{0}-----".format(ele.nodeName))
        childs = ele.childNodes
        for i in childs:
            if i.nodeName == "Name":
                # date是文本节点的一个属性，表示他的值
                print("Name:{0}".format(i.chidNodes[0].data))
            if i.nodeName == "Mobile":
                print("Mobile:{0}".format(i.childNodes[0].data))
            if i.nodeName == "age":
                print("Age:{0}".format(i.childNodes[0].data))
                if i.hasAttribute("detail"):
                    print("Age-detail:{0}".format(i.getAttribute("detail")))

