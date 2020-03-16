import numpy as np 
import torch
import math

# from sklearn.linear_model import LogisticRegression

"""0.1 10 100 5 10 10
0.105 0.956 0.876 0.133 0.249 0
0.195 0.672 0.193 0.016 0.009 0
0.059 0.282 0.709 0.139 0.478 1
0.303 0.39 0.95 0.912 0.522 1
0.59 0.57 0.141 0.959 0.036 1
0.231 0.355 0.305 0.508 0.625 1
0.896 0.415 0.771 0.197 0.826 0
0.051 0.537 0.442 0.46 0.628 0
0.737 0.583 0.09 0.337 0.774 1
0.062 0.217 0.553 0.868 0.87 0
0.13 0.972 0.845 0.737 0.492
0.016 0.009 0.432 0.41 0.092
0.257 0.327 0.451 0.18 0.62
0.774 0.143 0.879 0.123 0.222
0.885 0.114 0.352 0.484 0.367
0.439 0.227 0.675 0.654 0.323
0.778 0.191 0.633 0.628 0.929
0.958 0.231 0.07 0.739 0.34
0.015 0.115 0.154 0.75 0.649
0.283 0.853 0.752 0.915 0.937
"""

def sigmoid(x):
    return 1/(1+math.exp(-x))

def sigmoid_grad(x):
    return sigmoid(x)*(1-sigmoid(x))

# def torch_sigmoid(x):
#     return 1/torch.exp(-x)

class LR:
    def __init__(self, alpha, lamda, epoch, dim):
        self.alpha = alpha
        self.lamda = lamda
        self.epoch = epoch
        self.dim = dim
        
        # 初始化weights
        self.weights = [1.0]*dim
    
    def fit(self, train_x, y):
        
        for e in range(epoch):
            pred = self.get_pred(train_x)
            self.gradient_decent(pred, y, train_x)

    def gradient_decent(self, pred, y, train_x):
        grad_loss = [pred[i]-y[i] for i in range(len(pred))]

        for j in range(self.dim):
            grad = 0.0
            for i in range(len(pred)):
                grad += grad_loss[i]*train_x[i][j]
            
            # 正则约束
            grad += self.weights[j]*self.lamda
            self.weights[j] -= grad*self.alpha/len(pred)
        
        # print(self.weights)

    def get_pred(self, train_x):
        res = []
        
        for x in train_x:
            z = 0.0
            for i in range(self.dim):
                z += self.weights[i]*x[i]
            z = sigmoid(z)
            res.append(z)

        # print(res)
        return res



if __name__ == "__main__":

    alpha, lamda, epoch, dim, train_bs, test_bs = input().strip().split()
    alpha = float(alpha)
    lamda = float(lamda)
    epoch = int(epoch)
    dim = int(dim)
    train_bs = int(train_bs)
    test_bs = int(test_bs)

    train_x, train_y = [], []
    for i in range(train_bs):
        inp = input().strip().split(" ")
        train_x.append([float(x) for x in inp[:dim]])
        train_y.append(int(inp[-1]))
    
    test_x = []
    for i in range(test_bs):
        inp = input().strip().split(" ")
        test_x.append([float(x) for x in inp])

    lr = LR(alpha, lamda, epoch, dim)
    lr.fit(train_x, train_y)
    res = lr.get_pred(test_x)

    print(res )
    


    pass
    
    
