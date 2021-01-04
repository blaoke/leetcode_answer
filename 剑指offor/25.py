#方法一:定义新链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) :
        pre=new=ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                new.next=l1
                l1=l1.next
            else:
                new.next=l2
                l2=l2.next
            new=new.next
        if l1:
            new.next=l1
        else:
            new.next=l2
        return pre.next
#方法二:使用递归
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) :
        if not l1 :
            return l2
        if not l2:
            return l1
        mergehead=ListNode(0)
        if l1.val<l2.val:
            mergehead=l1
            mergehead.next= self.mergeTwoLists(l1.next,l2)
        else:
            mergehead=l2
            mergehead.next= self.mergeTwoLists(l1,l2.next)
        return mergehead

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) :
        if not l1 :
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next= self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next= self.mergeTwoLists(l1,l2.next)
            return l2



