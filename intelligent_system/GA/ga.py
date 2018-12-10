# -*- coding: utf-8 -*-
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin
import copy
from itertools import combinations,permutations

class Gas():

    # 初始化这个算法，然后确定了种群大小，染色体大小，和最大值最小值
    def __init__(self, popSize, chroSize, xrangeMin, xrangeMax, j=2):
        self.popSize = popSize
        self.chroSize = chroSize
        self.xrangeMin = xrangeMin
        self.xrangeMax = xrangeMax
        self.crossRate = 0.7  # 默认初始化的交叉率是0.7
        self.mutationRate = 0.01  # 变异率是0.01
        self.fit = lambda x: sin(j * x) ** 2

    # 初始化种群。
    def initialPop(self):

        pop = random.randint(0, 2, size=(self.popSize, self.chroSize))
        return pop

    # 将十进制进行转换到求解空间中的数值
    def get_declist(self, chroms):
        step = (self.xrangeMax - self.xrangeMin) / float(2 ** self.chroSize - 1)
        chroms_declist = []
        for i in xrange(self.popSize):
            chrom_dec = self.xrangeMin + step * self.chromToDec(chroms[i])
            chroms_declist.append(chrom_dec)
        return chroms_declist

    def chromToDec(self, chrom):
        m = 1
        r = 0
        for i in xrange(self.chroSize - 1, -1, -1):
            r = r + m * chrom[i]
            m = m * 2
        return r

    #     def get_solution_room(self,chroms):
    #         # 获得染色体的十进制表示
    #         chroms_declist = self.get_declist(chroms)
    #         return list(combinations(chroms_declist,self.j))

    # 获得各个基因的适应值。
    def get_fitness(self, chroms):

        chroms_declist = self.get_declist(chroms)
        #         room = self.get_solution_room(chroms)
        fitness_list = []
        for i in xrange(len(chroms_declist)):
            fitness_list.append(self.fit(chroms_declist[i]))
        return fitness_list

    # 输入参数为上一代的种群，和上一代种群适应度列表。
    # 还没有完全测试完成
    def selection(self, popSel, fitValue):
        newFitValue = []
        totalFitValue = sum(fitValue)
        accumulator = 0.0
        for val in fitValue:
            # 利用累加适应度来确定后面的算法
            newVal = val * 1.0 / totalFitValue
            accumulator += newVal
            newFitValue.append(accumulator)
        #         print "newFitValue",newFitValue
        ms = []
        for i in xrange(self.popSize):
            # 随机生成0,1之间的随机数
            ms.append(random.random())
        ms.sort()  # 由小到大的排列
        #         print "ms",ms
        # 利用双指针变量来进行选择，一次的扫描就能完成
        # 算是比较优化的算法了。
        fit_in = 0
        new_in = 0
        newPop = popSel
        while new_in < self.popSize:
            if (ms[new_in] < newFitValue[fit_in]):
                newPop[new_in] = popSel[fit_in]
                #                 print fit_in
                new_in += 1
            else:
                fit_in += 1
        pop = newPop
        # 返回的是适应度大的个体会被选择的概率较大
        # 使得新种群中，会有重复的较优个体。
        return pop

    # 交叉的过程貌似不是很理解
    def crossover(self, pop):
        for i in xrange(self.popSize - 1):
            # 近邻个体交叉，若随机数小于交叉率
            if (random.random() < self.crossRate):
                # 随机选择交叉点
                singPoint = random.randint(0, self.chroSize)
                temp1 = []
                temp2 = []
                # 对个体进行切片和重组
                temp1.extend(pop[i][0:singPoint])
                temp1.extend(pop[i + 1][singPoint:self.chroSize])
                temp2.extend(pop[i + 1][0:singPoint])
                temp2.extend(pop[i][singPoint:self.chroSize])
                pop[i] = temp1
                pop[i + 1] = temp2
        return pop

    # 变异的过程。
    def mutation(self, pop):
        for i in xrange(self.popSize):
            # 反转变异，随机数小于变异率，进行变异
            if (random.random() < self.mutationRate):
                mpoint = random.randint(0, self.chroSize - 1)
                # 将随机点上的基因进行反转。
                if (pop[i][mpoint] == 1):
                    pop[i][mpoint] = 0
                else:
                    pop[mpoint] = 1

        return pop

    def elitism(self, pop, popBest, nextBestFit, fitBest):
        # 输入上一代中的最优个体，变异之后的种群
        # 上一代的最有适应度，本代中最优适应度，这些变量都是在主函数中生成的。
        if nextBestFit- fitBest < 0:
            # 满足精英策略后，找到最差个体的索引，进行替换。
            pop_worst = nextfitvalue.index(min(nextfitvalue))  # 并没有在函数中说明的变量，非常之不妥。
            pop[pop_worst] = popbest
        return pop


if __name__ == '__main__':
    generation = 100  # 遗传代数
    # 引入Gas类，传入参数：种群大小，编码长度，变量范围
    mainGas = Gas(50, 23, 0, 6)
    pop = mainGas.initialPop()  # 种群初始化
    pop_best = []  # 每代最优个体
    for i in xrange(generation):
        # 在遗传代数内进行迭代
        declist = mainGas.get_declist(pop)  # 解码
        fitvalue = mainGas.get_fitness(pop)  # 适应度函数
        # 选择适应度函数最高个体
        popbest = pop[fitvalue.index(max(fitvalue))]
        # 对popbest进行深复制，以为后面精英选择做准备
        popbest = copy.deepcopy(popbest)
        # 最高适应度
        fitbest = max(fitvalue)
        # 保存每代最高适应度值
        pop_best.append(fitbest)
        ################################进行算子操作，并不断更新pop
        mainGas.selection(pop, fitvalue)  # 选择
        mainGas.crossover(pop)  # 交叉
        mainGas.mutation(pop)  # 变异
        ################################精英策略前的准备
        # 对变异之后的pop，求解最大适应度
        nextdeclist = mainGas.get_declist(pop)
        nextfitvalue = mainGas.get_fitness(nextdeclist)
        nextbestfit = max(nextfitvalue)
        ################################精英策略
        # 比较深复制的个体适应度和变异之后的适应度
        mainGas.elitism(pop, popbest, nextbestfit, fitbest)