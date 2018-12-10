# -*- coding: utf-8 -*-

import ga

if __name__ == '__main__':
    generation = 100
    # 遗传代数
    # 引入Gas类，传入参数：种群大小，编码长度，变量范围
    mainGas = ga.Gas(100, 10, -1, 2)
    pop = mainGas.initialpop()  # 种群初始化
    pop_best = []  # 每代最优个体
    for i in xrange(generation):
        # 在遗传代数内进行迭代
        declist = mainGas.get_declist(pop)  # 解码
        fitvalue = mainGas.get_fitness(declist)  # 适应度函数
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
        #对变异之后的pop，求解最大适应度
        nextdeclist = mainGas.get_declist(pop)
        nextfitvalue = mainGas.get_fitness(nextdeclist)
        nextbestfit = max(nextfitvalue)
        ################################精英策略
        # 比较深复制的个体适应度和变异之后的适应度
        mainGas.elitism(pop, popbest, nextbestfit, fitbest)
