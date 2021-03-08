#最长上升子序列 LIS(i)表示以第i个数字为结尾的最长上升子序列的长度
# lis(i)=max(1+lis(j) if nums[j]<nums[i]
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        n=len(nums)
        if n== 0:
            return 0
        memo=[1 for _ in range(n)]#memo[i]表示以nums[i]为结尾的最长上升子序列的长度
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    memo[i]=max(memo[i],memo[j]+1)
        return max(memo)