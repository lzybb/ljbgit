import xml.etree.ElementTree as et

etree = et.ElementTree()

e = et.Element('Student')

etree._setroot(e)

e_name = et.SubElement(e, 'Name')
e_name.text = 'hahaha'

etree.write('v06.xml', encoding='utf-8')
