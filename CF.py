#coding=utf-8
#_author_ = 'huoguang'

import math
from texttable import *
import sys


def getCosDist(user1, user2):
    sum_x = 0.0
    sum_y = 0.0
    sum_xy = 0.0
    for key1 in user1:
        for key2 in user2:
            if key1[0] == key2[0]:
                sum_x += key1[1]*key1[1]
                sum_y += key2[1]*key2[1]
                sum_xy += key1[1]*key2[1]
    if sum_xy == 0.0:
        return 0
    demo = math.sqrt(sum_x * sum_y)
    return sum_xy / demo


def readFile(filename):
    contents = []
    f = open(filename, 'r')
    contents = f.readlines()
    f.close()
    return contents

def getRatingInfo(ratings):
    rates = []
    for line in rates:
        rate = line.split('\t')
        rates.append([int(rate[0]), int(rate[1]), int(rate[2])])
    return rates

def getUserScoreDataStructure(rates):
    userDict = {}
    itemUser = {}
    for k in rates:
        user_rate = (k[1], k[2])
        if k[0] in userDict:
            userDict[k[0]].append(user_rate)
        else:
            userDict[k[0]] = [user_rate]

        if k[1] in itemUser:
            itemUser[k[1]].append(k[0])
        else:
            itemUser[k[1]] = [k[0]]
    return userDict, itemUser

def getNearestNeighbor(userId, userDict, itemUser):
    neighbors = []
    for item in userDict[userId]:
        for neighbor in itemUser[item[0]]:
            if neighbor != userId and neighbor not in neighbors:
                neighbors.append(neighbor)
    neighbors_dist = []
    for neighbor in neighbors:
        dist = getCosDist(userDict[userId], userDict[neighbor])
        neighbors_dist.append([dist, neighbor])
    neighbors_dist.sort()

def recommandByUserFC(filename, userID, k = 5):
    # 读取训练文件
    content = readFile(filename)
    # 向量化
    rates = getRatingInfo(content)

    #字典化数据
    userDict, itemUser = getUserScoreDataStructure(rates)

    # 寻找用户邻居
    neighbors = getNearestNeighbor(userID, userDict, itemUser)[:, 5]

    recommand_dict = {}
    for neighbor in neighbors:
        neighbor_user_id = neighbor[1]
        movies = userDict[neighbor_user_id]
        for movie in movies:
            if movie[0] not in recommand_dict:
                recommand_dict[movie[0]] = neighbor[0]
            else:
                recommand_dict[movie[0]] += neighbor[0]

    recommand_list = []
    for key in recommand_dict:
        recommand_list.append([recommand_dict[key], key])
    recommand_list.sort(reverse= True )
    user_movies = [k[0] for k in userDict[userID]]
    return [k[1] for k in recommand_list], user_movies, itemUser, neighbors

def getMoviesList(filename):
    contents = readFile(filename)
    movies_info = {}
    for movie in contents:
        single_info = movie.split("|")
        movies_info[int(single_info[0])] = single_info[1:]
    return movies_info


if __name__ == '__main__':

    reload(sys)
    sys.setdefaultencoding('utf-8')

    # 获取所有电影的列表
    movies = getMoviesList("u.item")
    recommend_list, user_movie, items_movie, neighbors = recommandByUserFC("u.data", 50, 80)
    neighbors_id = [i[1] for i in neighbors]
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t', 't', 't'])
    table.set_cols_align(["l", "l", "l"])
    rows = []
    rows.append([u"movie name", u"release", u"from userid"])
    for movie_id in recommend_list[:20]:
        from_user = []
        for user_id in items_movie[movie_id]:
            if user_id in neighbors_id:
                from_user.append(user_id)
        rows.append([movies[movie_id][0], movies[movie_id][1], ""])
    table.add_rows(rows)
    print table.draw()


