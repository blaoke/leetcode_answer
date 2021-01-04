#本题同剑指offor52题
#方法一:分别将两个链表压入栈中,然后不断从栈中弹出元素,如果弹出的元素相同就更新公共节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stack_a=[]
        stack_b=[]
        res=None #结果
        while headA:
            stack_a.append(headA)
            headA=headA.next
        while headB:
            stack_b.append(headB)
            headB=headB.next
        while stack_b and stack_a:
            top_a=stack_a.pop()
            top_b=stack_b.pop()
            if top_a==top_b:
                res=top_a
            else:
                break
        return res

#方法二:首先遍历一遍两个链表,分别求取各自长度,通过各自长度求得长度差,让长的链表先遍历长度差,然后一起遍历,如果两个链表遍历的节点相同,就是公共节点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a=0
        len_b=0
        res=None
        A=headA
        B=headB
        while A:
            len_a+=1
            A=A.next
        while B:
            len_b+=1
            B=B.next
        def first_run(head,diff_num):
            for i in range(diff_num):
                head=head.next
            return head
        diff_num=len_a-len_b
        if diff_num>0:
            first_run(headA,diff_num)
        elif diff_num<0:
            first_run(headB,-diff_num)
        while headA and headB:
            if headA==headB:
                res=headA
                break
            else:
                headA=headA.next
                headB=headB.next
        return res


