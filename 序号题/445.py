# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        ans=None
        res=0
        while stack1 or stack2 or res!=0: #如果两个栈有一个非空，res用于记录大于十的进位
        	a=0 if not stack1 else stack1.pop()
        	b=0 if not stack2 else stack2.pop()
        	cur=a+b+res
        	res=0
        	if cur>9:
	        	res=cur//10
	        	cur=cur%10
        	ret=ListNode(cur) #这里使用的头插法也是一个重点
        	ret.next=ans
        	ans=ret
        return ans




        #下面 直接求和的方法 就失去了本题考查的意义
        sums = sum(stack2 + stack1)
        while sums!=0: #7807通过求余输出的顺序为 从个位向上 7 0 8 7
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
