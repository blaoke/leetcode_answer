#使用双端队列(与队列的不同之处在于可以在o(1)时间复杂度内删除,查看队头和队尾元素),将前k个元素的最大值的下标存入双端队列,
# 然后从k到n-1开始遍历,每次将对头元素放入res,然后看如果队列头元素的下标与当前访问的下标差值>=k,就将对头元素出队,
#然后如果队列非空,队尾下标对应的元素如果小于当前访问元素,就将其队尾元素的索引出队,
#最后添加在队尾添加当前访问元素的索引
from collections import deque #引入双端队列
class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        deq=deque([]) #双端队列
        res=[] #返回结果
        n=len(nums)
        if n<k or k<1:#判断如果k小于n或者k为0,返回空
            return res
        for i in range(k):
            while  deq and nums[deq[-1]]<=nums[i]: #如果队列非空,并且队尾索引对应的元素小于当前值,就将其出队
                deq.pop()
            deq.append(i)
        for i in range(k,n):
            res.append(nums[deq[0]])
            if i-deq[0]>=k:#如果队首元素不在候选框内就移除
                deq.popleft()
            while  deq and nums[deq[-1]]<=nums[i]:#确保队列中
                deq.pop()
            deq.append(i)
        res.append(nums[deq[0]])
        return res
a=Solution()
print(a.maxSlidingWindow(nums=[2,3,4,2,6,2,5,1],k=3))
