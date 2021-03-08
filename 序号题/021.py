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
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2