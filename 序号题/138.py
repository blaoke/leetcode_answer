class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
#分三步:第一步,在每个节点后面复制一个节点
#第二步,根据每个原始节点连接的radom_next,复制节点连接radom_next.next
#第三步,奇数链表连接一组,偶数链表连接一组

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def colone_node(head):#第一步,在每个节点后面复制一个节点
            cur=head
            while cur:
                nexts=Node(cur.val)
                nexts.random=None

                cur_next=cur.next
                nexts.next=cur_next
                cur.next=nexts
                cur=cur_next
        def connect_node(head):#根据每个原始节点连接的radom_next,复制节点连接radom_next.next
            cur=head
            while cur:
                nexts = cur.next
                if cur.random:
                    cur_random=cur.random
                    nexts.random=cur_random.next
                cur=nexts.next

        def reconnect_node(head):#拆分,将奇数链表连接一组,偶数链表连接一组
            cur=head
            random_cur=Node(0)
            random=random_cur
            while cur:
                nexts=cur.next
                random_cur.next=nexts
                random_cur=random_cur.next
                cur.next=nexts.next
                cur=cur.next
            return random.next

        colone_node(head)
        connect_node(head)
        return reconnect_node(head)