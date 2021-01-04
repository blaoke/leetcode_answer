# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#二叉树的层次遍历,使用 deque 的 append()右边添加 和 popleft()左边删除 函数来快速实现队列的功能。
#deque模块是python标准库collections中的一项，它提供了两端都可以操作的序列,extendleft()左边添加,pop()右边删除
#BFS广度优先搜索
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        res=[]
        if not root:
            return res
        queue=deque([root]) #储存每一层节点的队列
        level=0 #表示节点的层级

        while queue:
            res.append([])
            for i in range(len(queue)):
                node=queue.popleft()
                res[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return res



