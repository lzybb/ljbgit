import xml.etree.ElementTree as et

stu = et.Element("Student01")

name = et.SubElement(stu,"Name")
name.attrib = {"lang", "en"}
name.text = "ljb"

age = et.SubElement(stu, "Age")
age.text = 18

et.dump(stu)
