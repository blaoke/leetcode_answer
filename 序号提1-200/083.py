# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) :
        if not head:
            return head
        cur=head
        while cur.next:
            next=cur.next
            if cur.val==next.val:
                cur.next=next.next
            else:
                cur=cur.next
        return head

