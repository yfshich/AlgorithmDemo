#!/user/bin/env python
#-*- coding:utf-8 -*-
from numpy import *
import operator
##给出训练数据及对应的类别
def creatDataSet():
    group = array([[1.0 ,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    lables = ['a','a','b','b']
    return group,lables
##通过KNN进行分类
def classify(input,dataset,label,k):
    ##它的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度。
    # 它的输入参数可以使一个整数表示维度，也可以是一个矩阵。
    datasize = dataset.shape[0]
    ###计算欧式距离
    #函数形式： tile(A，rep)
    #功能：重复A的各个维度
    #参数类型：
    #- A: Array类的都可以
    #- rep：A沿着各个维度重复的次数
    diff = tile(input,(datasize, 1)) - dataset
    print(diff)
    sqdiff = diff**2
    print(sqdiff)
    squareDist = sum(sqdiff,axis=1)##行向量分别相加得到新的行向量
    print(squareDist)
    dist = squareDist ** 0.5
    print(dist)
    ##对距离进行排序
    sorteDistIndex = argsort(dist)#argsort()根据元素进行从大到小排序，返回下标
    print(sorteDistIndex)
    classCount = {}
    for i in range(k):
        voteLable = label[sorteDistIndex[i]]#对选取的k个样本所属类别个数进行统计
        classCount[voteLable] = classCount.get(voteLable,0) + 1
    #选取出现类别次数最多的类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes
