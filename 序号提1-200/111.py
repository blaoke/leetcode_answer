# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归解决
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1

#利用队列迭代解决
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack=deque( [root])
        res=0
        while stack:
            for i in range(len(stack)):
                top=stack.popleft()
                if  not top.right and not top.left:
                    return res+1
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
            res+=1
        return res