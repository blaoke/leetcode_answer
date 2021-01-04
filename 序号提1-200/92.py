# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#自己方法
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        if not head:
            return None
        pre1=None
        cur=head
        cur1=None
        curi=None
        i=1
        while i<m:
            pre1=cur
            cur1=pre1#cur1相当于官方解法中的con,表示m-1位
            cur=cur.next
            i+=1
        if i ==m:
            curi=cur  #curi相当于官方解法中的tail,表示m位
            pre=cur
            cur=cur.next
            i+=1
        while i>m and i<=n:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
            i+=1
        if cur1:
            cur1.next=pre#m-1位的next等于n
        else:#防止让反转的是最后一个链表的情况
            head=None
        curi.next=cur#m位的next等于n+1
        return head
a=Solution()
a.reverseBetween(head=[1,2,3,4,5],m=2,n=4)


#官方解法,优点:没有使用i用于链表递进,而是巧妙地使用m-1和n-1表示递进
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head





