#!/user/bin/env python
#-*- coding:utf-8 -*-
from numpy import *

import scipy.spatial.distance as dist  # 导入scipy距离公式

matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])

print("dist.jaccard:", dist.pdist(matV,'jaccard'))
