# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre=ListNode(0)#在head节点前面设立一个节点
        pre.next=head
        cur=pre
        while cur.next and cur.next.next:
            next=cur.next#第一个节点next
            next_next=next.next#第二个节点next_next

            cur.next=next_next
            next.next=next_next.next#第三个节点next_next.next
            next_next.next=next
            cur=next
        return pre.next

#p-1-2-3 变成 p-2 1-3 2-1即p-2-1-3