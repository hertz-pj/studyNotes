def bayes(train_x, y, test_x, N, dim):

    # 先验概率和条件概率
    Py = {}
    Py_x = {}
    for yy in set(y):
        Py[yy] = 0
        Py_x[yy] = {}
        for i in range(dim):
            Py_x[yy][i] = {}

    for i in range(N):
        Py[y[i]] += 1
        for j in range(dim):
            Py_x[y[i]][j][train_x[i][j]] = Py_x[y[i]][j].get(train_x[i][j], 0) + 1
    
    

    for k in Py_x.keys():
        for j in range(dim):
            for xj in Py_x[k][j].keys():
                Py_x[k][j][xj] = Py_x[k][j][xj]/Py[k]
    # print(Py_x)
    for k in Py.keys():
        Py[k] = Py[k]/N

    res = []
    Py_tst = {}
    for x in test_x:
        tmp = []
        for yy in set(y):
            Py_tst[yy] = Py[yy]
        for j in range(dim):
            for yy in set(y):
                # print(yy, j, x[j])
                Py_tst[yy] *= Py_x[yy][j].get(x[j],0)
        for yy in set(y):
            tmp.append((Py_tst[yy], yy))
        res.append(max(tmp, key=lambda x: x[0])[1])

    return res

if __name__ == "__main__":
    N = int(input())

    feature = []
    y_train = []
    for _ in range(N):
        inp = list(map(int, input().split()))
        feature.append(inp[:-1])
        y_train.append(inp[-1])

    TN = int(input())
    test_x = []
    for _ in range(TN):
        test_x.append(list(map(int, input().split())))

    print(" ".join(list(map(str,bayes(feature, y_train, test_x, N, len(feature[0]))))))
        


"""
14
1 1 1 0 1
1 1 1 1 1
2 1 1 0 0
3 2 1 0 0
3 3 0 0 0
3 3 0 1 1
2 3 0 1 0
1 2 1 0 1
1 3 0 0 0
3 2 0 0 0
1 2 0 0 0
2 2 1 1 0
2 1 0 0 0
3 2 1 1 1
5
1 1 0 0
1 1 1 0
1 2 1 0
2 1 0 1
2 2 1 1
"""

    
