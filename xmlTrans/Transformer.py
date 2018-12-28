import xml.etree.ElementTree as ET
import sys
import os
import csv
from pretty_process import *
from util import *
import json


# 自定义一个转换的代码类
class Transformer():
    def __init__(self):
        self.outputPath = 'data/output_mods.xml'
        self.dcPath = 'data/dc_ok.xml'
        self.modsPath = 'data/mods_ok.xml'
        self.configList = None
        self.configPath = "config.csv"
        self.dcData = None
        self.modsData = None
        self.dcdirectory = None
        self.modstemplate = None
        self.loadInput()

    def setDcdir(self,path):
        self.dcdirectory = path

    def setModsTem(self,path):
        self.modstemplate = path

    def setOutputPath(self,path):
        self.outputPath = path

    def setDcPath(self,path):
        self.dcPath = path

    def setModsPath(self,path):
        self.modsPath = path

    def setConfigPath(self,path):
        self.configPath = path

    # 读取配置文件到这个类中
    def loadConfig(self):
        self.configList = list()
        with open(self.configPath,newline='') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader:
                self.configList.append(row)
        # print(self.configList)

    # 从文件中解析dcdata和modsdata
    def loadData(self):
        self.dcData = ET.parse(self.dcPath)
        self.modsData = ET.parse(self.modsPath)

# 判断输入的文件夹和mods的模板是否符合规范(后续继续添加判断数据)
    def checkPath(self):
        if not os.path.isdir(self.dcdirectory) or not os.path.exists(self.modstemplate):
            return False

        return True


    def transform(self):
        # 先检查文件路径
        if not self.checkPath():
            print("the wrong dc directory or modstemplate")
            return
        self.preProcess()
        self.loadConfig()
        self.loadData()
        dcroot = self.dcData.getroot()
        modsroot = self.modsData.getroot()
        print("the roots are:",dcroot.tag,modsroot.tag)
        print(self.configList)
        for wordList in self.configList:
            dcword = wordList[0]
            modsword = wordList[1]
            # print(dcword,modsword)
            # 设置mods 的文件
            dctext = None
            for item in dcroot.iter(dcword):
                dctext = item.text
                # 如果用的是xmlparser的话，是可以直接转换的。
                # 转换中文的html格式
                # if is_chinese(dctext):
                #     dctext = chinese2html(dctext)
                #     print(dctext)
            for item in modsroot.iter(modsword):
                item.text = dctext
        self.modsData.write(self.outputPath,xml_declaration=True)
        self.afterProcess()

    def preProcess(self):
        preprocess()

    def afterProcess(self):
        afterProcess()

# 先载入dc文件夹的路径和mods的模板
    def loadInput(self):
        inputdata = None
        with open("input.json",'rb') as f:
            inputdata = json.load(f)
        print(inputdata)
        self.setDcdir(inputdata['dcdirectory'])
        self.setModsTem(inputdata['modstemplate'])


if __name__ == '__main__':
    transformer = Transformer()
    transformer.transform()

