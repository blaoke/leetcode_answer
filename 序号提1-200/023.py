# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#遍历lists,将每一个链表的节点添加到堆中,之后不断从堆中取最小值,添加到新的链表中,最后返回这个列表
import heapq
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        k=len(lists)
        heap=[]
        pre=ListNode(0)
        cur=pre
        node=ListNode(0)
        for i in range(k):
            # for j in range(len(lists[i])):
                node.next=lists[i]
                while node.next:
                    node = node.next
                    heapq.heappush(heap,node.val)#存入堆的元素只能是数值,不能是链表的节点,所以是node.val
        while heap:
            b=heapq.heappop(heap)
            cur.next=ListNode(b)#将返回的int型变量转换为链表的结点型,然后不断先后
            cur=cur.next
        return pre.next





