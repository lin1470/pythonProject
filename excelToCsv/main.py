#coding:utf-8
import xlrd
import os
import sys
# 把excel文件转化为csv文件
def transformFile(fileName):
    outName = fileName.split('.')[0]+".csv" # 转换名字
    # print(outName)
    eFile = xlrd.open_workbook(fileName) # 打开excel文件
    table = eFile.sheets()[0] # 第一个页面
    nrows = table.nrows
    ncols = table.ncols
    # print (nrows,ncols)
    toFile = open(outName,"w")
    for i in range(nrows):
        rowValues = table.row_values(i)
        for i in range(ncols):
            # print(type(rowValues[i]))
            if(isinstance(rowValues[i],float)):
                rowValues[i] = str(int(rowValues[i])) # 读进来的是浮点型的,有毛病,需要做调整.
            toFile.write(str(rowValues[i]))
            if(i!=ncols-1):
                toFile.write(',')
        toFile.write('\n')
    toFile.close()

if __name__ == '__main__':
    if(len(sys.argv)!=1):
        dir = sys.argv[1]
    else:
        dir = os.getcwd() # 获取当前路径
    # print(dir)
    # print(dir)
    dirList = os.listdir(dir) # 获取当前目录文件列表
    for item in dirList:
        profix = item.split('.')[1]
        if(profix == 'xlsx' or profix == 'xls'):
            transformFile(item)