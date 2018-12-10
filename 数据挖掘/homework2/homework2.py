#coding utf-8

import csv
import pandas as pd
import apriori

data = pd.read_csv('data.csv')
##discretization of birthyear
def dataDiscretizeBirthyear(data):
    return pd.qcut(data['birth_year'],5).astype(str)+""

##discretization of weight
def dataDiscretizeWeight(data):
    return pd.qcut(data["weight"],5).astype(str)+""

##discretization of height     
def dataDiscretizeHeight(data):
    return pd.qcut(data["height"],5).astype(str)+""

##replace the processed data into the raw data
def mumerizeData(data):
    data_birth_year = dataDiscretizeBirthyear(data)
    data_weight = dataDiscretizeWeight(data)
    data_height = dataDiscretizeHeight(data)
    data.drop("birth_year",inplace = True ,axis = 1)
    data.drop("weight",inplace = True ,axis = 1)
    data.drop("height",inplace = True ,axis = 1)
    data = pd.concat([data,data_birth_year,data_weight,data_height],axis=1)
    return data

if __name__ == '__main__':

    myDat = mumerizeData(data)
    #%%
    print myDat['weight']
    print myDat['birth_year']
    print myDat['height']
    #%%
    #频繁项集与支持度
    sets,sp = apriori.apriori(myDat.values,4,0.6)
    rules = apriori.generateRules(sets,sp,0.8)
    print ("层级:频繁项集:支持度")
    for Lk in sets:
        for freq_set in Lk:
            print(str(len(list(Lk)[0])),':',freq_set,' : ',sp[freq_set])
    print("强关联规则:置信度")
    for item in rules:
            print (item[0], "-->>", item[1], " : ", item[2])
#%%
