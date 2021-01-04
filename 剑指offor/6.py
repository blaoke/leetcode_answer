#改变链表的结构,如果题目表示不能改变链表结构则可能不可取
class Solution:
    def reversePrint(self, head: ListNode) -> ListNode:
        cur=head
        pre=None
        res=[]
        while(cur):
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        while pre:
            res.append(pre.val)
            pre=pre.next
        return res

#利用栈是实现
class Solution:
    def reversePrint(self, head: ListNode) -> ListNode:
        ret=[]#栈
        # res=[]#返回结果的数组
        while(head):
            ret.append(head.val)
            head=head.next
        ret.reverse()
        return ret

#利用递归实现
class Solution:
    def reversePrint(self, head: ListNode) -> ListNode:
        res = []
        def di(head):
            if head:
                if head.next:
                    di(head.next)
                res.append(head.val)
        di(head)
        return res




