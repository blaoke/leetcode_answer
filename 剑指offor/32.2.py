#同102题目
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