#状态转移方程为从[x,lens-1]
class Solution:
    def rob(self, nums: [int]) -> int:
        lens=len(nums)
        if lens==0:
            return 0
        memo=[-1 for _ in range(lens)]#存储每个位置可以偷取的最大值

        index=lens-1
        memo[index]=nums[index]
        while index>0:
            index-=1
            for j in range(index,lens):
                memo[index]=max(memo[index] , nums[j]+memo[j+2] if j+2<lens else nums[j])
        return memo[0]

#状态转移为从[0:x]
class Solution:
    def rob(self, nums: [int]) -> int:
        lens=len(nums)
        if lens==0:
            return 0
        memo=[-1 for _ in range(lens)]#存储每个位置可以偷取的最大值
        memo[0]=nums[0]
        for i in range(1,lens):
            j=i
            while j >=0:
                memo[i]=max(memo[i],nums[j]+memo[j-2] if j-2>=0 else nums[j])
                j-=1
        return memo[lens-1]


#状态转移方程f(x)=v(x)+f(x-2) (如果x-2>=0) 或者f(x)=f(x-1),最优方法
class Solution:
    def rob(self, nums: [int]) -> int:
        lens=len(nums)
        if lens==0:
            return 0
        f=[-1 for _ in range(lens)]
        f[0]=nums[0]
        for x in range(1,lens):
            f[x]=max(nums[x]+f[x-2] if x-2>=0 else nums[x],f[x-1])
        return f[lens-1]

#上一个方法减少空间复杂度的改进
class Solution:
    def rob(self, nums: [int]) -> int:
        lens=len(nums)
        if lens==0:
            return 0
        f=pre=0
        for x in range(lens):
            f,pre=max(nums[x]+pre, f),f
        return f
a=Solution()
print(a.rob(nums=[2,1,1,4]))