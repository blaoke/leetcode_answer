# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre=ListNode(0)#在头节点前面创建一个新的节点
        pre.next=head
        cur=pre
        while cur.next:
            if cur.next.val==val:
                next = cur.next
                cur.next=next.next
                cur=next
                next=None#使用完成后将next设为空,删除
            else:
                cur=cur.next
        return pre.next


