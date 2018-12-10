
# coding: utf-8


import pandas as pd
import numpy as np

colNames = ['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids',
                'Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','diluted wines','Proline']
wine_data = pd.read_csv('wine.data',names=colNames)
from sklearn.cross_validation import train_test_split
# 划分训练集和测试集。
def get_data(wine_data):
    train_data, test_data = train_test_split(wine_data, test_size = 0.4)
    trainInput = train_data.iloc[:,1:14].values
    trainOutput = pd.get_dummies(train_data['class']).values
    testInput = test_data.loc[:,'Alcohol':'Proline'].values
    testOutput = pd.get_dummies(test_data['class']).values
    return trainInput,trainOutput,testInput,testOutput

# 定义激活函数是：sigmoid function
def nonlin(x,deriv=False):
# 使用S型函数求导
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# 获取最大值

def maxx(array):
    array = list(array)
    return array.index(max(array))

# n代表输入的节点数，输出节点数为3。

class neuralNetwork:
    def __init__(self,n,layer=2):
        self.n = n
        self.layer = layer
        np.random.seed(n)
        self.syn0 = 2*np.random.random((n,n+2)) - 1
        self.syn1 = 2*np.random.random((n+2,3)) - 1
      #神经网络的训练过程  
    def training(self,train_data,y):
        for j in range(30000):
            a = train_data
            b = nonlin(np.dot(a,self.syn0))
            c = nonlin(np.dot(b,self.syn1))
            c_error = y - c
            # 每5000次迭代计算一次误差。
            if (j% 5000== 0):
                print  '迭代',j,'次的误差是：',str(np.mean(np.abs(c_error)))
            c_delta = c_error*nonlin(c,deriv=True)
            b_error = c_delta.dot(self.syn1.T)
            b_delta = b_error * nonlin(b,deriv=True)
            self.syn1 += 0.1*b.T.dot(c_delta)
            self.syn0 += 0.1*a.T.dot(b_delta)
            
    def predict(self,pre_data):
        return nonlin(nonlin(pre_data.dot(self.syn0)).dot(self.syn1))

# z-score规范化数据。
y = wine_data['class']
x =wine_data.drop('class',axis=1)
means = x.mean()
stds = x.std()
x = (x-means)/stds
x.insert(0,'class',y)
data = x

# 返回训练集和测试集
trainInput,trainOutput,testInput,testOutput = get_data(data)
# 建立13个输入节点的神经网络
network = neuralNetwork(13)
# 进行训练
network.training(trainInput,trainOutput)
# 存储测试结果
result = network.predict(testInput)


# 计算准确率
count =0
for i in range(len(testOutput)):
    if maxx(testOutput[i]) == maxx(result[i]):
        count +=1
print "三层神经网络的准确率为：",count*1.0/len(result)

