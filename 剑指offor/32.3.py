#方法一:使用队列,与32.2基本相同,在最后将res中奇数数组反转过来
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
        for i in range(len(res)):
            if i%2!=0:
                res[i].reverse()
        return res

#方法二:使用两个栈解决,如果当前层是偶数层(0,2,4),就访问queue1并依次读取左子树和右子树,如果当前层是奇数层,就访问queue2并先读取右子树再读取左子树
class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        res=[]
        if not root:
            return res
        queue1=[root] #栈1
        queue2=[] #栈2
        level=0 #表示节点的层级

        while queue1 or queue2:
            res.append([]) #不同层存放在不同的数组中
            if level%2==0: #如果当前是奇数层
                for i in range(len(queue1)):
                    node=queue1.pop()
                    res[level].append(node.val)
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)
            else:  #如果当前是偶数层
                for j in range(len(queue2)):
                    node=queue2.pop()
                    res[level].append(node.val)
                    if node.right:
                        queue1.append(node.right)
                    if node.left:
                        queue1.append(node.left)
            level+=1
        return res

#方法三:使用双端队列解决,与方法一不同点在于,不需要最后遍历数组并按行数翻转
#如果是奇数行,就先访问左子树再访问右子树,右边进右边出(相当于口朝右的栈),如果是偶数行,就向访问右子树再访问左子树,左边进左边出(相当于口朝左的栈)
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
            if level%2==0: #偶数层
                for i in range(len(queue)):
                    node=queue.popleft()
                    res[level].append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            else: #奇数层
                for j in range(len(queue)):
                    node=queue.pop()
                    res[level].append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            level+=1
        return res