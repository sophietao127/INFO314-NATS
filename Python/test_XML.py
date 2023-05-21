import xml.etree.ElementTree as ET
import xml.dom.minidom
import os

tree = ET.parse('portfolio-Mary.xml')
#calling the root element
root = tree.getroot()
# print("Root is",root)

new_num = '80'
for x in root.iter('stock'):
    # print(x.attrib, x.text)
    if x.attrib['symbol'] == 'MSFT':
        print(x.text)
        x.text = new_num
    if x.attrib['symbol'] == 'GE':
        root.remove(x)

# remove file
if os.path.exists("portfolio-Mary.xml"):
    os.remove("portfolio-Mary.xml")
# write a new file
tree.write('portfolio-Mary.xml')

# create a new XML file with the results
# tree.write('newitems4.xml')


# symbol1 = "Idly"
# adjust1 = "2.5"
# price1 = "10"
# timestamp = 2019
# timestamp = "'{t}'".format(t=timestamp)
# data='''<?xml version="1.0" encoding="UTF-8"?>
# <message sent={time}>
# <stock>
#     <name>{symbol}</name>
#     <adjustment>{adjust}</adjustment>
#     <adjustedPrice>{price}</adjustedPrice>
# </stock>
# </message>
# '''.format(time=timestamp, symbol=symbol1, adjust=adjust1, price=price1)


# xml_data = data
# # print(xml_data)
# myroot = ET.fromstring(xml_data)
# # print(myroot)
# print(myroot.tag)
# time = myroot.attrib['sent']
# print("timestamp:", time)
# print(myroot[0].tag)  # <stock>
# for i in range(len(myroot[0])):
#      print(myroot[0][i].tag, myroot[0][i].text)