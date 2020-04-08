"""
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
输入: [1,2,3]

       1
      / \
     2   3

输出: 6

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

思路: 以123为例，最大路径要么为213，21，31，1，或者是1，21,31中某个和1父节点联合
我们需要用递归的方法求得到当前节点的最大路径并返回上层，在这过程中需要记录213,21,31,1中最大的那个。

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


ans = float("-inf")
def maxPath(root):

    if root is None:
        return 0

    left = max(0, maxPath(root.left))
    right = max(0, maxPath(root.right))

    # 这一步其实已经包含了1,12,13,123四种情况，试想如果2,3都小于0，结果就是1，
    # 如果2,3的都大于0，结果就是123，如果其中给一个大于一个小于，结果就是23
    ans = max(ans, left + right + root.val)

    return max(left, right) + root.val

print(ans)






