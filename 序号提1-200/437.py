# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归方法
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        #在以node为根节点的二叉树中,寻找包含node,和为num的路径个数
        def findsum(node:TreeNode,num):
            if not node:
                return 0
            res=0
            if node.val==num:
                res+=1
            res+=findsum(node.right,num-node.val)
            res+=findsum(node.left,num-node.val)
            return res

        if not root:
            return 0

        res=findsum(root, sum)#当前节点其和为sum的值
        res+=self.pathSum(root.left,sum)#左子树中其和为sum的路径
        res+=self.pathSum(root.right,sum)#右子树中其和为sum的路径
        return res



