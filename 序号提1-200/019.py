# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        next=head
        pre=ListNode(0)
        pre.next=head
        cur=pre
        while n>0:
            next=next.next
            n-=1
        while next!=None:
            cur=cur.next
            next=next.next
        if cur.next:
            NEX=cur.next
            cur.next=NEX.next
        return pre.next

#设立两个指针,第一个指针为cur,第二个指针next与cur相距n+1,然后不断先后遍历,
#当next指针为空时,cur指针指向倒数第n+1的位置,然后让cur的next=next.next,这样就删除了倒数第n个节点