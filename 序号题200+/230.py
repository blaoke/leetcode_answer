#参考94题,二叉树的中序遍历,因为这道题目是二叉搜索树,所以只需要中序遍历找第K个元素即可
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res=[]
        stack=[]
        i=0
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                top=stack.pop()
                res.append(top.val)
                i+=1
                if i==k:
                    return res[-1]
                root=top.right