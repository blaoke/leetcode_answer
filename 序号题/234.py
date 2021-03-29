# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 使用快慢指针找到链表前面一半的尾节点，尾节点后面一个元素即为后面链表的头节点，然后将后面链表反转，然后判断两者是否相同
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast=head
        slow=head
        while fast.next and fast.next.next: #循环结束后，slow即为 前回文的尾节点 #这个地方先判断 fast.next是防止在fast.next为空的情况下，fast.next.next报错
            slow=slow.next
            fast=fast.next.next
        pre=None
        cur=slow.next
        while cur:  #接下来开始翻转后半部分，最后返回的pre即为尾节点
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        #现在开始判断部分
        res=True
        while res and pre and head:
            if pre.val==head.val:
                pre=pre.next
                head=head.next
            else:
                res=False
        return res



