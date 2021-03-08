# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#头插法：
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        cur=head
        while(cur):
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre
    
#递归法：1 2 3 4 5   1 2  5 4 3
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        newhead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newhead