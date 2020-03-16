import math

class lr:
    def __init__(self,alpha, lamda, epoch, dim):
        self.alpha = alpha
        self.lamda = lamda
        self.epoch = epoch
        self.dim = dim
        self.weights = [1 for _ in range(self.dim)]

    def get_pred(self,a,b):
        result = []
        for line in a:
            cur  = 0
            for i in range(len(line)):
                cur += line[i]*b[i]
            cur = 1/(1+math.exp(-cur))
            result.append(cur)
        print(result)
        return result

    def grad_descent(self, pred, train_y):
        bs = len(train_y)
        dim = len(self.weights)
        hx_y = [pred[i]-train_y[i] for i in range(bs)]
        for j in range(dim):
            cur = 0
            for i in range(bs):
                cur += (hx_y[i]*train_data[i][j])
            cur += lamda*self.weights[j]
            cur = cur*self.alpha/bs
            self.weights[j] -= cur
        # print(self.weights)
        return self.weights


    def train(self,train_data,train_y):
        for epc in range(self.epoch):
            pred = self.get_pred(train_data,self.weights)
            self.weights = self.grad_descent(pred, train_y)

    def test(self,test_data):
        pred_y = self.get_pred(test_data,self.weights)
        print(pred_y)
        test_y = []
        for pred in pred_y:
            if pred > 0.5:
                test_y.append(1)
            else:
                test_y.append(0)
        return test_y


# 学习率，正则约束，epoch，输入训练数据维度，训练数据，测试数据
alpha, lamda, epoch, dim, train_bs, test_bs = input().strip().split()
alpha = float(alpha)
lamda = float(lamda)
epoch = int(epoch)
dim = int(dim)
train_bs = int(train_bs)
test_bs = int(test_bs)
train_data = []
train_y = []
test_data = []

for i in range(train_bs):
    line = list(map(float,input().strip().split()))
    train_data.append(line[:dim])
    train_y.append(line[-1])
for i in range(test_bs):
    test_data.append(list(map(float, input().strip().split())))


my_lr = lr(alpha, lamda, epoch, dim)
my_lr.train(train_data,train_y)
test_y = my_lr.test(test_data)
for pred in test_y:
    print(pred)
