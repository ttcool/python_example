#encoding=utf-8

import xml.etree.ElementTree as et
import pprint
from xml.etree.ElementTree import (Element,SubElement,Comment,tostring)

with open('menu.xml','rt') as f:
	tree = et.parse(f)

#遍历整个树
for node in tree.iter('item'):
	price = node.attrib.get('price')
	text = node.text
	if price and text:
		print "%s:%s" %(text,price)
		 
#findall()方法
for node in tree.findall('.//breakfast/item'):
	price = node.attrib.get('price')
	text = node.text
	
	print "%s:%s" %(text,price)



	