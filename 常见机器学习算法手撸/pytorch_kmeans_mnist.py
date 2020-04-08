import torch
from torchvision import datasets, transforms
import random
import copy
import matplotlib.pyplot as plt
import numpy as np

def cal_distance(x, y):
    return torch.sum((x-y)**2)**0.5

def d(a):
    return a

def cal_cluster_center(cluster):
    return torch.mean(cluster, dim=0)

def Kmeans(data, k, max_iter):

    idxs = list(range(data.size(0)))

    # initial k cluster centers
    centers = [data[idx] for idx in random.sample(idxs, k)]
    
    iter_ = 0
    while iter_ < max_iter:
        clusters = {}
        for x in data:
            dist_list = []
            for i in range(k):
                dist = cal_distance(x, centers[i])
                dist_list.append((dist, i))
            
            min_dist, min_idx = min(dist_list, key=lambda x: x[0])
        
            # add the data x in clusters
            if min_idx not in clusters:
                clusters[min_idx] = []
            clusters[min_idx].append(x)

        print(clusters.keys())

        
        pre_centers = centers[:]
        # update center
        for i in range(k):
            centers[i] = cal_cluster_center(torch.stack(clusters[i]))
        
        # print(len(pre_centers), len(centers))
        
        # print(torch.stack(pre_centers).size())
        # print(torch.stack(centers).size())
        if torch.allclose(torch.stack(pre_centers), torch.stack(centers)):
            break
        # early stop
        iter_ += 1
    
    return clusters




if __name__ == "__main__":
    
    # test_data = datasets.MNIST("./data", train=False, transform=transforms.ToTensor())

    # train_x = []
    # for i in range(len(test_data)):
    #     train_x.append(test_data[i][0].view(-1))
    #     if i > 1000:
    #         break
    data = torch.randn((500, 2), dtype=float)

    # print(train_x[0].size())
    # print(len(train_x))
    colors = {0:"red",1:"yellow",2:"blue",3:"pink",4:"green"}
    clusters = Kmeans(data, 5, 100)

    for k,v in clusters.items():
        c = np.array([x.numpy() for x in v])
        plt.scatter(c[:,0], c[:,1], c=colors[k])
    # print(cal_cluster_center(torch.tensor([[1,2],[2,1]], dtype=float)))
    plt.show()
    plt.savefig("./tmp/scatter2.png")
    pass