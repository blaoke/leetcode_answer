#同主站110题
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#方法一:层次递归遍历,缺点有很多元素进行了重复计算
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res=True
        def depth(root):
            if not root:
                return 0
            left=depth(root.left)
            right=depth(root.right)
            diff=left-right
            if abs(diff)>1:
                self.res=False
            return max(left,right)+1
        depth(root)
        return self.res
#方法二:后续遍历加剪枝
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
