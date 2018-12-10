#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:07:55 2017

@author: bruce
"""

#apriori算法实现

##构建初始候选项集列表
##大小为1的项集集合(大小为1的频繁项集)
def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1

##判断新生成的项集是否满足条件
##由初始候选项集向后生成项集所需
def is_apriori(Ck_item, Lksub1):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True

##由初始候选项集的集合Lk生成新的候选项集
##K表示新项集中含有的元素个数
def aprioriGen(Lksub1, k):
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                # pruning
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck

##计算Ck中的项集在数据集合D中的支持度
##返回满足最小支持度的项集的集合，和所有项集支持度的信息的字典
def scanD(data_set, Ck, min_support, support_data):
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


##核心算法
##将新的项集支持度数据加入原来的总支持度字典中
##将符合最小支持度要求的项集加入
##返回满足条件的频繁项集的列表以及所有候选项集的支持度信息
def apriori(data_set, k, min_support):
    
    support_data = {}
    C1 = create_C1(data_set)
    L1 = scanD(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k+1):
        Ci = aprioriGen(Lksub1, i)
        Li = scanD(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data

##生成强关联规则
##L(list)存储频繁项集
##supportData(dict)存储所有项集的支持度
##minConf(float)最小可信度
##过程1计算规则的可信度
##过程2对频繁项集中元素超过2的项集进行合并
def generateRules(L, supportData, minConf):
    bigRuleList = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = supportData[freq_set] / supportData[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= minConf and big_rule not in bigRuleList:
                        bigRuleList.append(big_rule)
            sub_set_list.append(freq_set)
    return bigRuleList
