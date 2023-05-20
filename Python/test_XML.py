import xml.etree.ElementTree as ET
symbol1 = "Idly"
adjust1 = "2.5"
price1 = "10"
timestamp = 2019
timestamp = "'{t}'".format(t=timestamp)
data='''<?xml version="1.0" encoding="UTF-8"?>
<message sent={time}>
<stock>
    <name>{symbol}</name>
    <adjustment>{adjust}</adjustment>
    <adjustedPrice>{price}</adjustedPrice>
</stock>
</message>
'''.format(time=timestamp, symbol=symbol1, adjust=adjust1, price=price1)


xml_data = data
# print(xml_data)
myroot = ET.fromstring(xml_data)
# print(myroot)
print(myroot.tag)
time = myroot.attrib['sent']
print("timestamp:", time)
print(myroot[0].tag)  # <stock>
for i in range(len(myroot[0])):
     print(myroot[0][i].tag, myroot[0][i].text)