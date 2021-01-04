#双指针向后,注意算法的鲁棒性
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k==0:
            return
        cur=head
        for i in range(k-1):
            if cur.next:
                cur=cur.next
            else:
                return None
        pre=head
        while cur.next:
            pre=pre.next
            cur=cur.next
        return pre