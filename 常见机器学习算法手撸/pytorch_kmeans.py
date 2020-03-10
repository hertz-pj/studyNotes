import torch
import random
import copy
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

def cal_distance(a, b):
    return torch.sum((a-b)**2)**0.5

def cal_cluster_center(cluster):
    return torch.mean(cluster, dim=0)

def kmeans(data, k, max_iter):

    r_indexes = [i for i in range(len(data))]
    random.shuffle(r_indexes)

    centers = []
    for i in range(k):
        centers.append(data[r_indexes[i]])
    centers = torch.stack(centers)
    
    iter_ = 0
    while iter_ < max_iter:
        clusters = {}
        for x in data:
            dist_list = []
            for idx in range(k):
                dist = cal_distance(x, centers[idx])
                dist_list.append((idx, dist))
            
            min_idx, min_dist = min(dist_list, key=lambda x: x[1])
            
            if min_idx not in clusters:
                clusters[min_idx] = []
            
            clusters[min_idx].append(x)

        pre_centers = copy.deepcopy(centers)
        
        for idx in range(k):
            centers[idx] = cal_cluster_center(torch.stack(clusters[idx]))
        
        if torch.allclose(pre_centers, centers):
            print(f"early stop from iter:{iter_}")
            break
        
        # 设置早停
        iter_ += 1
    
    return clusters


if __name__ == "__main__":
    # a = torch.tensor([1.0,2,3,4], dtype=float)
    # b = torch.tensor([4.0,3,4,5], dtype=float)
    # print(cal_distance(a,b))
    # pass
    data = torch.randn((1000,2), dtype=float)
    clusters = kmeans(data, 4, 1000)

    colors = {0:"red",1:"yellow",2:"blue",3:"pink"}

    for k, v in clusters.items():
        # print(k, len(v))
        v = torch.stack(v).numpy()
        plt.scatter(v[:,0], v[:,1], c=colors[k])
    
    plt.show()
    plt.savefig("./tmp/scatter.png")

    
    # data = torch.stack((a,b))
    # print(cal_cluster_center(data))