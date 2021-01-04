#方法一:使用二分查找方法,首先根据数组长度求出中间位置值,然后遍历数组求中间位置前面的元素个数,如果个数大于中间位置值,说明从
# 初始位置到中间位置有重复元素移动右指针到中间位置,否则移动左指针到中间位置+1
# class Solution:
#     def findDuplicate(self, nums: [int]) -> int:
#         n=len(nums)
#         left,right=1,n
#         while left<right:
#             mid=(left+right)//2
#             cnt=0
#             for num in nums:
#                 if num<=mid:
#                     cnt+=1
#             if cnt>mid: #如果从初始位置到中间位置的元素大于中间位置的值,说明区间内有重复元素,将右指针指向mid
#                 right=mid
#             else:
#                 left=mid+1
#         return left
# a=Solution()
# print(a.findDuplicate(nums=[3,1,3,4,2]))

#方法二:使用快慢指针(总是慢指针先移动),第一步,首先移动慢指针然后移动快指针,当两个指针指向的元素相同时表示相遇,说明中间有环
#第二步,将慢指针放到队首,快指针保持位置不变,当两者的值相同时,表示找到重复元素
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if nums[slow]==nums[fast]:
                break
        slow=0
        while nums[slow]!=nums[fast]:
            slow=nums[slow]
            fast=nums[fast]
        return nums[slow]
a=Solution()
print(a.findDuplicate(nums=[3,1,3,4,2]))
'''
这里简单解释为什么后面将 slow 放置起点后移动相遇的点就一定是答案了。假设环长为 L，从起点到环的入口的步数是 a，从环的入口继续走 b 步到达相遇位置，从相遇位置继续走 c 步回到环的入口，
则有 b+c=L，其中 L、a、b、c 都是正整数。根据上述定义，慢指针走了 a+b 步，快指针走了 2(a+b)步。从另一个角度考虑，在相遇位置，快指针比慢指针多走了若干圈
因此快指针走的步数还可以表示成 a+b+kL，其中 k 表示快指针在环上走的圈数。联立等式，可以得到2(a+b)=a+b+kL,解得 a=kL-b，整理可得a=(k-1)L+(L-b)=(k-1)L+c
从上述等式可知，如果慢指针从起点出发，快指针从相遇位置出发，每次两个指针都移动一步，则慢指针走了 aa 步之后到达环的入口，
快指针在环里走了k−1 圈之后又走了c 步，由于从相遇位置继续走 c 步即可回到环的入口，因此快指针也到达环的入口。两个指针在环的入口相遇，相遇点就是答案。
'''

