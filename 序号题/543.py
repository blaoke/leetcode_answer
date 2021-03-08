class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0
        def dfs(root:TreeNode):# 记录每一个子树的深度
            if not root:
                return 0
            l= dfs(root.left)
            r= dfs(root.right)
            self.res=max(self.res,l+r+1)#存储当前节点与之前遍历节点的最长路径
            return max(l,r)+1 #返回当前子树的最长深度
        dfs(root)
        return self.res-1
