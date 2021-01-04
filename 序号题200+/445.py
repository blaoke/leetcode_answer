# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = [0]
        stack2 = [0]
        ret = []
        while l1 or l2:
            if l1:
                stack1 = [i * 10 for i in stack1]
                stack1.append(l1.val)
                l1 = l1.next

            if l2:
                stack2 = [i * 10 for i in stack2]
                stack2.append(l2.val)
                l2 = l2.next
        sums = sum(stack2 + stack1)
        while sums!=0:
            a=sums%10
            sums//=10
            ret.append(a)
        ret.reverse()
        res=ListNode()
        back=res
        for i in ret:
            res.next=ListNode(i)
            res=res.next
        if not back.next:
            return back
        return back.next



while lists !=0:
    a=lists%10
    lists//=10
    ret.append(a)
ret.reverse()