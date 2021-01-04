class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur=head
        pre=None
        while(cur):
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre