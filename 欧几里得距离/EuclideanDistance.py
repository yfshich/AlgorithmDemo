#!/user/bin/env python
#-*- coding:utf-8 -*-
#数据集
critics={
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0
    }
}
from math import sqrt
#欧几里得距离
def sim_distance_ou(prefs,person1,person2):
    #创建一个集合用来存储用户1和用户2都有的电影的评分
    si = {}
    # 使用用户1里评分的电影名去遍历检索用户2的评分的电影名，如果同时存在，往si集合中加上这个电影名并且赋值为1
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    # 如果两个用户没有同时存在的电影的评分，则跳出循环
    # si数据结构：{'Superman Returns': 1, 'Snakes on a Plane': 1}
    if len(si) == 0: return 0
    #计算所有差值的平方和
    sum_of_squares = sum([pow(prefs[person1][item]- prefs[person2][item], 2) for item in si])
    # 对加和的结果进行开根，加1是为了避免被0整除
    return 1 / (1 + sqrt(sum_of_squares))
redult = sim_distance_ou(critics,"Gene Seymour","Mick LaSalle")
print(redult)