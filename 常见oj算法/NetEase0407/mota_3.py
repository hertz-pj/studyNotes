# 魔塔打怪，没打一个怪防御升级一级
# 当防御力小于怪物的破防能力时，受到伤害，问英雄受到的最小伤害
# 输入N, D, N表示共有N个怪，D表示初始防御力
# 输入N个数，表示N个怪物的破防
# 输入N个数，表示N个怪物的攻击

# 思路贪心

if __name__ == "__main__":
    N, D = tuple(map(int, input().split()))

    A = list(map(int, input().split())) 
    B = list(map(int, input().split()))

    
    pass