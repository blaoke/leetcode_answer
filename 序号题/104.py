# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#利用递归解决方法
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        maxright=self.maxDepth(root.right)+1
        maxleft=self.maxDepth(root.left)+1
        return max(maxleft,maxright)

#利用队列迭代解决方法
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack=deque( [root])
        res=0
        while stack:
            for i in range(len(stack)):
                top=stack.popleft()
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
            res+=1
        return res

