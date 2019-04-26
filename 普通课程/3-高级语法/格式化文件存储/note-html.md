
# XML访问

## 读取
- XML读取分两个主要技术，SAX， DOM
- SAX(simple API for XML):
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点：
        - 快
        - 流式读取
        
- DOM
    - 是W3C规定的XML编程接口
    - 一个XML文件在缓存中以树形结构保存，读取
    - 用途
        - 定位浏览XML任何一个节点信息
        - 添加删除相应内容
    - minidom
        - minidom.parse(filename):加载读取的xml文件，filename也可以是xml代码
        - doc.documentElement:获取xml文档对象，一个xml文件只有一个对应的文档对象
        - node.getAttribute(attr_name)：获取xml节点的属性值
        - node.getElementByTagName(tage_name):得到一个节点对象集合
        - node.childNodes:得到所有孩子节点
        - node.childNodes[index].nodeValue:获取单个节点值
        - node.firstNode:得到第一个节点，等同于node.childNodes[0]
        - node.attributes[tage_name]
        - 案例v01
    
    - etree
        - 以树形结构来表示xml
        - root.getiterator:得到相应的可迭代的node集合
        - root.iter 效果同上
        - find(node_name):查找指定node_name的节点，返回一个node
        - root.findall(node_name):返回多个node_name的节点
        - node.tag: node对应的tagename
        - node.text: node的文本值
        - node.attrib: 是node的属性的字典类型的内容
        - 案例v02