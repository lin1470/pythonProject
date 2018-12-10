# coding:utf-8

from kmeans import *

if __name__ == "__main__":
    wine_data = read_data('wine.data')
    wine_class = wine_data['class']
    wine_data = wine_data.drop('class',axis=1) # 先去掉第一行的数据。
    wine_data = mat(z_score(wine_data))

    # print wine_data
    myCentroids,clustAssing = kMeans(wine_data,3)
    print "各个分类的质心是",myCentroids
    # print clustAssing
    error_analysis(clustAssing,wine_class)