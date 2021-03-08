# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head:
            return head
        cur = head
        while cur.next:
            next = cur.next
            if cur.val == next.val:
                cur.next = next.next
            else:
                cur = cur.next
        return head

# 递归写法：

class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        else:
            return head
