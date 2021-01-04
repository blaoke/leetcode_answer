class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque #引入队列这一数据结构
class Solution:
    def levelOrder(self, root: TreeNode):
        stack=deque([root])
        res=[]
        if not root:
            return res
        while stack:
            top=stack.popleft()
            res.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return res
