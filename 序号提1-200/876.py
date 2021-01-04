#方法一:常规方法,将链表转换为数组表示
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a=head
        ret=[]
        while a:
            ret.append(a)
            a=a.next
        return ret[len(ret)//2]

#方法二:利用长短指针,长指针每次走两步,短指针每次走一下
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

