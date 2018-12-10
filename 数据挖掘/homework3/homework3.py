# coding:utf-8
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
dt = pd.read_excel('data.xlsx',header=None)
# get the data
target = dt[4]
train = dt.drop(4,1) # 1 indicates the axis
#%%

# 训练集划分
X_train,X_test,y_train,y_test = train_test_split(train,target,test_size=0.4)
#%%
# http://blog.csdn.net/gamer_gyt/article/details/51265347
clf_svm = SVC(kernel="rbf")
#高斯核
# http://blog.csdn.net/gamer_gyt/article/details/51232210
clf_KNN = KNeighborsClassifier(3)
#3近邻

clf_svm.fit(X_train,y_train)
clf_KNN.fit(X_train,y_train)

print("Gaussian kernel，3NN")
print("svm precision")
print(clf_svm.score(X_test,y_test))
print("3-NN prcision")
print(clf_KNN.score(X_test,y_test))
#%%
clf_svm = SVC(kernel="linear")
#线性核
clf_KNN = KNeighborsClassifier(4)
#4近邻

clf_svm.fit(X_train,y_train)
clf_KNN.fit(X_train,y_train)

print("linear kernel，4NN")
print("svm precision")
print(clf_svm.score(X_test,y_test))
print("3-NN precision")
print(clf_KNN.score(X_test,y_test))
#%%
clf_svm = SVC(kernel='poly',degree=3)
clf_KNN = KNeighborsClassifier(5)
clf_svm.fit(X_train,y_train)
clf_KNN.fit(X_train,y_train)