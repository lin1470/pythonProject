import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
print root
for child in root:
    print child.tag,child.attrib
print len(root)  # this mean that there is three countries.
print root[0]  # this mean that the 0 element is the first data.
print root.tag
# for neighbor in root.iter('neighbor'):
#     print neighbor,neighbor.attrib
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print rank,name
