#方法一,自己的方法,有瑕疵不完整,不想改了
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return None
        if not head.next:
            return head
        if k==0:
            return head
        pre = ListNode(0)
        pre.next = head
        cur = pre
        next = head
        n = k
        while n > 0 and next != None:  # 当k的值比链表长度短时
            next = next.next
            n -= 1
        if next==None and n==0:
            return head

        ##处理k的值比链表长的情况
        if next==None and n!=0:
            lens=k-n
            to_num=lens-k%lens
            next=pre
            while to_num>0:
                next=next.next
                to_num-=1

        # cur = cur.next
        while next.next!=None:
            next_next=next.next
            cur=cur.next
            next=next_next
        cur=cur.next
        pre.next=cur.next
        cur.next=None
        next.next=head
        return pre.next


#方法二(官方推荐的方法)
#将链表形成一个循环链表的然后找到头和尾巴,并让尾巴的next=None即可
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return None
        if not head.next:
            return head
        pre=ListNode(0)
        pre.next=head
        cur=head
        lens=1
        while cur.next:
            cur=cur.next
            lens+=1
        cur.next=head
        tail=pre
        for i in range(lens-k%lens):
            tail=tail.next
        pre.next=tail.next
        tail.next=None
        return pre
