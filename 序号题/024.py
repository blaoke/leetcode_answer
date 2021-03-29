# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre=ListNode(0)#在head节点前面设立一个节点
        pre.next=head
        cur=pre
        while cur.next and cur.next.next: #如果cur后面节点数少于2个，则交换直接结束
            l1=cur.next #第一个节点l1
            l2=l1.next #第二个节点l2

            cur.next=l2
            l1.next=l2.next #第三个节点l2.next
            l2.next=l1
            cur=l1 
        return pre.next

#p-1-2-3 变成 p-2 1-3 2-1即p-2-1-3                 
#在头节点之前创立空节点pre，令cur表示当前到达的节点，初始时，cur=pre，每次交换cur后面的两个
