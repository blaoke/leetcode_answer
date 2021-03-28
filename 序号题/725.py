#nums=lens//k,每个链表最少放多少个节点，mod = lens % k ，如果有余数，就在前面几个链表前面多加一个
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        lens = 0
        cur = root
        while cur:
            cur = cur.next
            lens += 1
        res = [None for _ in range(k)]
        if lens == 0:  # 如果为空链表，直接返回
            return res
        nums = lens // k  # 表示每一个里面最少放几个
        mod = lens % k  # 表示前面有几个里面需要加一个

        pre = None
        start = root
        for i in range(k):
            res[i] = start
            for j in range(nums + 1 if mod != 0 else nums):
                if start:
                    pre = start #这个pre的作用是记录每一个短链表的最后一个节点
                    start = start.next
                else:
                    start = None
            if mod > 0:
                mod -= 1
            pre.next = None #将每个链表的最后截断
        return res
