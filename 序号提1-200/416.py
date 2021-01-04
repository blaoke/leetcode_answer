class Solution:
    def canPartition(self, nums: [int]) -> bool:
        sums=sum(nums)
        if sums%2:#如果数组的和不能除以二
            return False
        mid=int(sums/2) #定义一半的sums值
        memo=[False for _ in range(mid+1)] #存储从0到mid共mid+1个元素
        #memo初始化,只考虑第一个数
        for i in range(mid+1):#i表示数值
            memo[i]=(nums[0]==i)#首先考虑第一个数,如果memo中元素刚好等于nums[0]的值,就将这个元素的值设为True

        #考虑从第一个数向后的所有数
        for j in range(1,len(nums)):
            tmp=mid #从数值最大向前考虑
            while tmp>=nums[j]:
                memo[tmp]=memo[tmp] or memo[tmp-nums[j]]
                tmp-=1
        return memo[mid]

a=Solution()
print(a.canPartition(nums=[1, 5, 11, 5]))