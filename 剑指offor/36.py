#方法一:通过非递归中序遍历将所有节点存入列表,然后遍历列表确定每个节点的left和right
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def mid_search(root): #标准中序遍历非递归写法
            stack = []
            res = []
            cur = root
            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    top = stack.pop()
                    res.append(top)
                    cur = top.right
            return res

        res=mid_search(root)
        pre=res[-1]
        for i in res:
            i.left=pre
            pre.right=i
            pre=i
        return res[0]

#方法二:在非递归中序遍历的过程中确定每个节点的left和right,最后确定头节点的left和尾节点的right
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.stack = []
        self.head = None
        self.pre = None
        if not root:
            return

        def mid_search(root):  # 标准中序遍历非递归写法
            cur = root
            while cur or self.stack:
                if cur:
                    self.stack.append(cur)
                    cur = cur.left
                else:
                    top = self.stack.pop()
                    if not self.head:
                        self.head = top
                        self.pre = top

                    else:
                        top.left = self.pre
                        self.pre.right = top
                        self.pre = top
                    cur = top.right

        mid_search(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head

#方法三:递归写法求解中序遍历,其余与方法二类似
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: #如果没有链表存在,直接返回
            return None

        self.head=None #链表的头节点
        self.pre=None #前一个节点

        def midorder(cur):
            if not cur:
                return
            midorder(cur.left) #先向左走到底
            if not self.head: #如果没有头节点(初始状态)
                self.head=cur
                self.pre=cur
            else:
                cur.left=self.pre #当前节点的左节点为中序遍历前一个节点
                self.pre.right=cur#前一个节点的右节点为当前节点
                self.pre=cur#前一个节点转为当前节点
            midorder(cur.right)

        midorder(root)
        #连接首尾节点
        self.head.left=self.pre
        self.pre.right=self.head
        return self.head







