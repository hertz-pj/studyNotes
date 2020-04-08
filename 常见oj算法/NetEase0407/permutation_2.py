# n个同学去看电影，1,2,...,7 做一排，但是有几对同学不愿意一起做，请按字典序输出所有可能的情况。
# 第一行n,k 表示共有n个同学,有k对不想坐一起的同学。
# 
# 思路：回溯 + 剪枝

def permutaiton(visit, cur, bad_case, n, res, final):

    if cur == n:
        final.append(res[:])
        return 

    for i in range(1, n+1):
        if not visit[i]:
            if cur >= 1 and (res[cur-1], i) in bad_case:
                continue
            visit[i] = True
            res[cur] = i
            permutaiton(visit, cur+1, bad_case, n, res, final)
            visit[i] = False
    

if __name__ == "__main__":
    
    n,k = tuple(map(int, input().split()))
    
    bad_case = set()
    for _ in range(k):
        a,b = tuple(map(int, input().split()))
        bad_case.add((a,b))
        bad_case.add((b,a))


    final = []
    res = [0] * n
    visit = [False]*(n+1)

    permutaiton(visit, 0, bad_case, n, res, final)

    for x in final:
        print(" ".join(map(str, x)))

    pass
        