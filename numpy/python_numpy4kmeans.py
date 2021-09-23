### 随机找k个点作为中心点
### 计算数据到k个中心的距离
### 让数据加入距离最小的簇
### 更新簇中心
### 迭代

### Kmeans算法效率不高，且非常依赖初始的k个点的选取

import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def cal_distance(a, b):
    return np.sum((a-b)**2)**0.5

def cal_cluster_center(cluster):
    return np.mean(cluster, axis=0)


# 数据, k值，最大迭代次数
def kmeans(data, k, max_iter):

    # 生成index
    r_indexes = [i for i in range(len(data))]
    random.shuffle(r_indexes)

    # 随机抽取k个
    centers = []
    for i in range(k):
        centers.append(data[r_indexes[i]])

    iter_ = 0
    while iter_ < max_iter:
        
        clusters = {}
        for x in data:
            dist_list = []
            for idx in range(len(centers)):
                dist = cal_distance(x, centers[idx])
                dist_list.append((idx, dist))

            # 找到距离最近的中心
            min_idx, min_dist = min(dist_list, key=lambda x: x[1])
            
            # 加入相应的簇
            if min_idx not in clusters:
                clusters[min_idx] = []
            clusters[min_idx].append(x)
        
        # 早停
        pre_centers = centers[:]

        # 计算新的中心
        for idx in clusters.keys():
            centers[idx] = cal_cluster_center(clusters[idx])
        
        if np.allclose(pre_centers, centers):
            print(f"early stop by iter:{iter_}")
            break
            
        iter_ += 1
    
    return clusters
            

if __name__ == "__main__":
    # a = np.array([1,2,3,4])
    # b = np.array([2,3,4,5])

    # data = np.random.randn(1000, 2)
    data = load_iris()["data"]

    clusters = kmeans(data, 3, 100)

    colors = {0:"red",1:"yellow",2:"blue",3:"green",4:"pink"}

    for k, v in clusters.items():
        v = np.array(v)
        plt.scatter(v[:,0], v[:,1], c=colors[k])

    plt.show()
    plt.savefig("scatter.png")
    


    # print(cal_distance(a,b))    
    pass

