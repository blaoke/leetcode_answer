#定义奇数和偶数开始节点和末尾节点，然后不断向后遍历，设置一个 is_odd参数判断当前访问节点是否为奇数节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: #如果为空链表，直接返回无
            return None
        if not head.next or not head.next.next: #如果链表节点数少于3，则直接返回原链表
            return head
        odd_start=head
        odd_end=head
        even_start=head.next
        even_end=head.next
        cur=head.next.next
        is_odd=True
        while cur:
            next=cur.next
            if is_odd: #如果下一个碰到的是奇节点，则将其添加到odd_end后面
                odd_end.next=cur
                cur.next=even_start
                even_end.next=next
                odd_end=cur
                is_odd=False
            else:
                even_end=cur
                is_odd=True
            cur=next
        return odd_start
