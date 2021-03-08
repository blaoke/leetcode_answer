#在head前面设置空节点,然后不断先后,其中cur表示当前节点
# 若遇到next节点==next.next情况,就不断循环,直到遍历到重复元素的末尾,若无这种情况,直接cur=cur.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) :
        if not head:
            return head
        pre=ListNode(0)#创建一个新节点
        pre.next=head
        cur=pre#cur表示当前节点位置
        while cur.next:#cur.next非空
            next = cur.next
            if next.next!=None and next.val==next.next.val:#next.next非空时才能进行next.next.val操作
                while next.next!=None and next.val==next.next.val :
                    next_next=next.next
                    next=next_next
                    cur.next=next.next
            else:
                cur=cur.next
        return pre.next

