#!/usr/bin/python
# coding=utf-8
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 加载数据

# 计算欧几里得距离,其中的一个计算方法。
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) # 求两个向量之间的距离，这样子计算的话，不管是几维的都是可以进行的。

# # 构建聚簇中心，取k个(此例中为4)随机质心
# def randCent(dataSet, k):
#     n = shape(dataSet)[1] # 实际上指明是几维的。
#     centroids = mat(zeros((k,n)))   # 每个质心有n个坐标值，总共要k个质心
#     for j in range(n):
#         minJ = min(dataSet[:,j])  # 每一列最小
#         maxJ = max(dataSet[:,j])  # 每一列最大
#         rangeJ = float(maxJ - minJ)  # 范围
#         centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
#     return centroids


def read_data(fileName):
    colNames = ['class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                'Flavanoids',
                'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'diluted wines', 'Proline']
    return pd.read_csv(fileName,header=None,names=colNames)


def z_score(data):
    means = data.mean()
    stds = data.std()
    return (data-means)/stds


def randCent(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        centroids[i, :] = dataSet[index, :]
    return centroids

# k-means 聚类算法
# 这个算法dataset是默认的函数，k是指定有多少类，distMeans是指定默认的计算距离的方法，createCent产生质心的方法。

def kMeans(dataSet, k, distMeans =distEclud, createCent = randCent):
    m = shape(dataSet)[0] # m代表的是这个数据集中数据的个数
    clusterAssment = mat(zeros((m,2)))    # 用于存放该样本属于哪类及质心距离
    # clusterAssment第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    centroids = createCent(dataSet, k) # 随机产生质心。
    clusterChanged = True   # 用来判断聚类是否已经收敛
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # 把每一个数据点划分到离它最近的中心点
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j  # 如果第i个数据点到第j个中心点更近，则将i归属为j
            if clusterAssment[i,0] != minIndex: # 如果分配发生变化，则需要继续迭代
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2   # 并将第i个数据点的分配情况存入字典
        # print centroids
        for cent in range(k):   # 重新计算中心点
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]   # 去第一列等于cent的所有列
            centroids[cent,:] = mean(ptsInClust, axis = 0)  # 算出这些数据的中心点
    return centroids, clusterAssment

#  明显这个显示只能选取的是二维的数据。
def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large! please contact Zouxy"
        return 1

        # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.show()
# 误差分析，根据分类来获取这个分类的大体个数

def error_analysis(clustAssing,wine_class):
    # result = pd.DataFrame(np.zeros((1, 3)))
    c = np.array(map(lambda x: int(x)+1, clustAssing[:, 0]))
    print c
    c_dum = pd.get_dummies(c)
    wine_c = np.array(wine_class)
    print wine_c
    # print map(lambda x,y : x==y, c,wine_c)

    result = c==wine_c
    print "聚类的结果为："
    print sum(c_dum)
    print "正确聚类的结果数：", sum(result)
    print "正确率为：",float(sum(result)*1.0/len(c))
# --------------------测试----------------------------------------------------
# 用测试数据及测试kmeans算法
# datMat = mat(loadDataSet('testSet.txt')) # 转换为矩阵的形式。

if __name__ == "__main__":
    wine_data = read_data('wine.data')
    wine_class = wine_data['class']
    wine_data = wine_data.drop('class',axis=1) # 先去掉第一行的数据。
    wine_data = mat(z_score(wine_data))

    print wine_data
    myCentroids,clustAssing = kMeans(wine_data,3)
    # print "各个分类的质心是",myCentroids
    # print clustAssing
    error_analysis(clustAssing,wine_class)
