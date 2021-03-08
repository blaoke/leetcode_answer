# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 设立 双指针,第一个指针为cur,第二个指针next与cur相距n+1,然后不断先后遍历,
# 当next.next指针为空(即next指向链表最后一个节点),cur指针指向倒数第n+1个节点,然后让cur的next=next.next,这样就删除了倒数第n个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        next = head
        while n > 0:
            next = next.next
            n -= 1
        if next == None:  # 如果要删除倒数最后一个节点(第一个节点)，则直接返回head.next
            return head.next
        while next.next != None:
            cur = cur.next
            next = next.next
        cur.next = cur.next.next
        return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0, head)  # 在头节点前面定义一个新节点
        cur = pre  # 慢指针
        next = head  # 快指针
        for i in range(n):
            next = next.next
        if next == None:
            return head.next
        while next != None:
            cur = cur.next
            next = next.next
        cur.next = cur.next.next
        return head
