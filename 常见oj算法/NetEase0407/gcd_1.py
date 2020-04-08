# 第一行输入数字N，表示有N个元素的数组A
# 第二行输入N个数字的数组A
# 求一个最大正整数d，使得对于任意的i，有A[i]-A[i-1]被d整除。

# 思路，求等差数列后求最大公约数
def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        r = a%b
        a = b
        b = r
    
    return a


def solve(N, a):

    b = []
    for i in range(1, N):
        if a[i] - a[i-1] == 0:
            return -1
        else:
            b.append(a[i]-a[i-1])
    
    if len(b) < 2:
        return b[0]
    
    tmp = gcd(b[0], b[1])
    for i in range(2, len(b)):
        tmp = gcd(tmp, b[i])

    return tmp
    

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    print(solve(N, A))
    pass