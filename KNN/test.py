#!/user/bin/env python
#-*- coding:utf-8 -*-
import knn
from numpy import *
dataset,labels = knn.creatDataSet()
input = array([1.1,0.3])
K = 3
output = knn.classify(input,dataset,labels,K)
print("测试数据为:",input,"分类结果为：",output)