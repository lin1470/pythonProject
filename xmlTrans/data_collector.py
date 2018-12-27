#!u
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from util import *

class Collector():
    def __init__(self):
        self.json_data = None
        self.number = 1

    def import_data(self):
        with open('data/data.json', 'rb') as f:
            json_data = json.load(f)
            self.json_data = json_data
            print(len(json_data))


    def deal_data(self):
        for item in self.json_data:
            root = ET.Element('dc')
            item_details = None
            for key,value in item.items():
                if key != 'link' and key != 'image':
                    subele = ET.SubElement(root, key)
                    subele.text = value
                else:
                    if key == 'link':
                        item_details = scrach_data(value.replace("'",''))
                        for detail_key,detail_value in item_details.items():
                            subele = ET.SubElement(root,detail_key)
                            subele.text = detail_value
                    elif key == 'image':
                        img = getImg(value)
                        with open('data/'+str(self.number)+'.jpg','wb') as f:
                            f.write(img)
                        pass

            # tree = ET.ElementTree(root)
            xml_string =ET.tostring(root)
            tree = minidom.parseString(xml_string)
            xml_string = tree.toprettyxml(encoding='utf-8')

            # print(self.number)
            # tree.write('data/'+str(self.number)+'.xml', encoding='utf-8',xml_declaration=True, method="xml")
            with open('data/'+str(self.number)+'.xml','wb') as f:
                f.write(xml_string)
            self.number += 1


    def process(self):
        self.import_data()
        self.deal_data()


if __name__ == '__main__':
    collector = Collector()
    collector.process()
