#pre,cur,next三个指针,在cur遍历k个节点中,每次cur.next指向pre,然后pre和cur后移
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) :
        sums=0 #用于记录链表中节点个数
        count=head
        while count:
            sums+=1
            count=count.next
        n,digit=divmod(sums,k) #n==sums//k表示倍数,digit表示余数

        def reverse(cur,k):
            pre=None
            tail1 = cur  # 记录每一个翻转完的尾节点
            for i in range(k):
                nexts=cur.next
                cur.next=pre
                pre=cur
                cur=nexts
            return tail1,pre,cur

        cur=head
        tail1,pre,cur=reverse(cur,k)
        total_head=pre
        for _ in range(1,n):
            tail2,pre,cur=reverse(cur,k)
            tail1.next=pre
            tail1=tail2
        if digit!=0:
            tail1.next=cur
        return total_head








