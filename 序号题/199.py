from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        res = []
        ret=[]
        if not root:
            return res
        queue = deque([root])  # 储存每一层节点的队列
        level = 0  # 表示节点的层级

        while queue:
            res.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                res[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        for i in range(len(res)):
            ret.append(res[i][-1])
        return ret


from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        res = []
        ret=[]
        if not root:
            return res
        queue = deque([root])  # 储存每一层节点的队列
        level = 0  # 表示节点的层级

        while queue:
            res.append(queue[-1])
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return res