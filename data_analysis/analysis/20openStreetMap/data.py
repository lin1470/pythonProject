#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from pymongo import MongoClient

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
not_number = re.compile(r'\D')

CREATED = ["version", "changeset", "timestamp", "user", "uid"]
postcode = []

def shape_element(element):
    # node = {}
    # # 探索数据发现了，其实这个地图的文件里面是没有一个way的标签的，只有node的标签
    # if element.tag == "node":
    #     # YOUR CODE HERE
    #     # print element.attrib
    #     # print len(element.attrib)
    #     element_len = len(element.attrib)
    #     element_keys = element.attrib.keys()
    #     created = {}
    #     pos = {}
    #     node['type'] = element.tag
    #     for i in range(element_len):
    #         if element_keys[i] in CREATED:
    #             created[element_keys[i]] = element.attrib[element_keys[i]]
    #         elif element_keys[i] == 'lon' or element_keys[i] == 'lat':
    #             # pos.append(float(element.attrib[element_keys[i]]))
    #             pos[element_keys[i]] = float(element.attrib[element_keys[i]])
    #         else:
    #             node[element_keys[i]] = element.attrib[element_keys[i]]
    #     # 以下需要把tag里面的数据进行整理。
    #     if element.findall('tag'):
    #         address = {}
    #         tags = element.findall('tag')
    #         for tag in tags:
    #             if re.search(problemchars,tag.attrib['k']):
    #                 continue
    #             else:
    #                 key = tag.attrib['k']
    #                 # if re.compile(u'addr:').match(tag.attrib['k']):
    #                 if key.find(r'addr:') ==0 and key.replace(r'addr:','').find(':') == -1:
    #                     key = tag.attrib['k'].split(':')[1]
    #                     value = tag.attrib['v']
    #                     address[key]  = value
    #                 pass
    #         if len(address) != 0:
    #             node['address'] = address
    #     if element.findall('nd'):
    #         nds = element.findall('nd')
    #         node_refs = []
    #         for nd in nds:
    #             node_refs.append(nd.attrib['ref'])
    #         if len(node_refs) != 0:
    #             node['node_refs'] = node_refs
    #         # 处理pos的顺序
    #     if len(pos) != 0:
    #         pos_list = []
    #         pos_list.append(pos['lat'])
    #         pos_list.append(pos['lon'])
    #         node['pos'] = pos_list
    #         # print pos_list
    #         # print node_refs
    #
    #         # elif element_keys[i] == 'k':
    #         #     value = element.get('k')
    #         #     address = {}
    #         #     if problemchars.search(value):
    #         #         pass
    #         #     else:
    #         #         pass
    #
    #     if len(created) != 0:
    #         node['created'] = created
    #     # pprint.pprint(node)
    #     return node
    # else:
    #     return None

    node = {}
    node['type'] = element.tag # 自动添加这个type这个类型的数据
    # 这个if是处理Node节点的。
    if element.tag == 'node' or element.tag == 'relation' or element.tag == 'way':
        element_len = len(element.attrib)
        element_keys = element.attrib.keys()
        created = {}
        pos = {}
        node['type'] = element.tag
        for i in range(element_len):
            if element_keys[i] in CREATED:
                created[element_keys[i]] = element.attrib[element_keys[i]]
            elif element_keys[i] == 'lon' or element_keys[i] == 'lat':
                pos[element_keys[i]] = float(element.attrib[element_keys[i]])
            else:
                node[element_keys[i]] = element.attrib[element_keys[i]]
        if len(pos) != 0:
            pos_list = []
            pos_list.append(pos['lat'])
            pos_list.append(pos['lon'])
            node['pos'] = pos_list
        pass
        if len(created) != 0:
            node['created'] = created
        # 处理node之中的tags
        # if element.tag == 'node':
        #     # tags = {}
        #     if element.iter():
        #         for it in element.iter('tag'):
        #             tags[it.attrib['k']] = it.attrib['v']
        #             pass
        #     # if len(tags) != 0:
        #     #     node['tags'] = tags

        # 一起处理tags标签,将名字提取出来。

        if element.iter('tag'):
            name = {} # 把名字都放在一起
            tags = {}
            for it in element.iter('tag'):
                if 'name:' in it.attrib['k']:
                    key = it.attrib['k'].split(':')[1]
                    value = it.attrib['v']
                    name[key] = value
                elif 'addr:postcode' in it.attrib['k']: # 只检查addr:postcode这个属性
                    if not_number.search(it.attrib['v']):
                        tags['addr:postcode'] = '430000'
                        pass
                    postcode.append(it.attrib['v'])
                else:
                    tags[it.attrib['k']] = it.attrib['v']
                    pass
            if len(name) != 0:
                node['name'] = name
            if len(tags) != 0:
                node['tags'] = tags

        # 处理way之中的tags和nd标签
        if element.tag == 'way':
            nd_refs = []
            # tags = {}
            if element.iter():
                for it in element.iter('nd'):
                    nd_refs.append(it.attrib['ref']) # 将所有的ref的属性都添加到这个里面
                # if element.iter("tag"):
                #     for it in element.iter("tags"):
                #         tags[it.attrib['k']] = it.attrib['v']
            if len(nd_refs) != 0:
                node['nd_refs'] = nd_refs
            # if len(tags) != 0:
            #     node['tags'] = tags
        # 处理relation标签中的
        if element.tag == 'relation':
            members = []
            # tags = {}
            if element.iter('member'):
                for it in element.iter('member'):
                    members.append([it.attrib['ref']])
            # if element.iter("tags"):
            #     for it in element.iter("tags"):
            #         tags[it.attrib['k']] = it.attrib['v']
            if len(members) != 0:
                node['members'] = members
            # if len(tags) != 0:
            #     node['tags'] = tags

            pass
        return node

    else:
        return None

    pass

#这个处理数据函数的是不用修改的吧。
def process_map(file_in, pretty=False):
    # You do not need to change this file
    file_out = "/home/bruce/Desktop/{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo: # 注意了这句话是打开并写入一个文件里面的。
        fo.write(r'[')
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2) + ",\n")
                else:
                    fo.write(json.dumps(el) + "\n")
        fo.write(r']')
    return data

# 这个函数是计算tags种类的。因为这个函数如果单独运行的话是比较浪费时间的，所以在此注释掉
def count_tags_type(file_name):
    iterparse = ET.iterparse(file_name,events = ("start",))
    tag_types = {}
    tag_types['child_node'] = 0
    for event, elem in iterparse:
        if elem.tag not in tag_types.keys():
            tag_types[elem.tag] = 1
        else:
            tag_types[elem.tag] += 1
    return tag_types
    pass

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset,
    # call the process_map procedure with pretty=False. The pretty=True option adds
    # additional spaces to the output, making it significantly larger.
    file_name = "wuhan_china.osm"
    json_file = '/home/bruce/Desktop/wuhan_china.osm.json'
    data = process_map(file_name, True)
    # print postcode
    # pprint.pprint(data[0])
    # 显示这个tag的种类和数目有哪些的。
    # tags_type = count_tags_type(file_name)
    # print tags_type
    # import_data(json_file)


def import_data(file_name):
    with open(file_name) as f:
        data = json.loads(f.read())
        for item in data:
            db.item.insert(item)
    pass
def explore(db):
    print db.item.find().count()  # 查看所有的数据个数
    print db.item.find({"type": "node"}).count()  # 发现是和之前在统计标签的时候的数字是一样的。
    print db.item.find({"type": "way"}).count()  # 发现是和之前在统计标签的时候的数字是一样的。
    # 贡献度最大的用户
    print len(db.item.distinct("created.user"))
    agg = [doc for doc in db.item.aggregate([{"$group": {"_id": "$created.user", "count": {"$sum": 1}}},
                                             {"$sort": {"count": -1}}, {"$limit": 1}])]
    print agg[0]
    # 只出现一次的用户
    agg = [doc for doc in db.item.aggregate([{"$group": {"_id": "$created.user", "count": {"$sum": 1}}},
                                             {"$group": {"_id": "$count", "num_users": {"$sum": 1}}},
                                             {"$sort": {"_id": 1}},
                                             {"$limit": 1}])]
    print agg[0]

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.map
    test()