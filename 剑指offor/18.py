# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        ret=pre=ListNode(0)
        pre.next=head
        cur=head
        while cur:
            if cur.val==val:
                pre.next=cur.next
            cur=cur.next
            pre=pre.next
        return ret.next