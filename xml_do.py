#encoding=utf-8

import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print root.tag

for child in root:
    print('tag:',child.tag,'attributes:',child.attrib)
    for grandchild in child:
        print('\ttag:',grandchild.tag,'attributes:',grandchild.attrib,'text:',grandchild.text)
print len(root)
print root[0]


#在root下新建两个子节点
sina = et.SubElement(root,'sina')
chinabyte = et.SubElement(root, "chinabyte")
tree.write("menu.xm")