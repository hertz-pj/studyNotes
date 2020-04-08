from torchvision import datasets, transforms
import numpy as np
from sklearn.metrics import accuracy_score
import torch
from tqdm import tqdm
import time

# matrix func
def KNN(train_x, train_y, test_x, test_y, k):

    since = time.time()

    m = test_x.size(0)
    n = train_x.size(0)

    # cal Eud distance mat
    print("cal dist matrix")
    xx = (test_x**2).sum(dim=1,keepdim=True).expand(m, n)
    yy = (train_x**2).sum(dim=1, keepdim=True).expand(n, m).transpose(0,1)

    dist_mat = xx + yy - 2*test_x.matmul(train_x.transpose(0,1))
    mink_idxs = dist_mat.argsort(dim=-1)

    res = []
    for idxs in mink_idxs:
        # voting
        res.append(np.bincount(np.array([train_y[idx] for idx in idxs[:k]])).argmax())
    
    assert len(res) == len(test_y)
    print("acc", accuracy_score(test_y, res))
    time_elapsed = time.time() - since
    print('KNN mat training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))

def cal_distance(x, y):
    return torch.sum((x-y)**2)**0.5
# iteration func
def KNN_by_iter(train_x, train_y, test_x, test_y, k):

    since = time.time()

    # cal distance
    res = []
    for x in tqdm(test_x):
        dists = []
        for y in train_x:
            dists.append(cal_distance(x,y).view(1))
        
        idxs = torch.cat(dists).argsort()[:k]
        res.append(np.bincount(np.array([train_y[idx] for idx in idxs])).argmax())

    # print(res[:10])
    print("acc",accuracy_score(test_y, res))

    time_elapsed = time.time() - since
    print('KNN iter training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
        


if __name__ == "__main__":

    train_dataset = datasets.MNIST(root="./data", transform=transforms.ToTensor(), train=True, download=True)
    test_dataset = datasets.MNIST(root="./data", transform=transforms.ToTensor(), train=False, download=True)

    # build train&test data
    train_x = []
    train_y = []
    for i in range(len(train_dataset)):
        img, target = train_dataset[i]
        train_x.append(img.view(-1))
        train_y.append(target)

        if i > 5000:
            break

    # print(set(train_y))

    test_x = [] 
    test_y = []
    for i in range(len(test_dataset)):
        img, target = test_dataset[i]
        test_x.append(img.view(-1))
        test_y.append(target)

        if i > 200:
            break

    print("classes:" , set(train_y))

    KNN(torch.stack(train_x), train_y, torch.stack(test_x), test_y, 7)
    KNN_by_iter(torch.stack(train_x), train_y, torch.stack(test_x), test_y, 7)
    
    