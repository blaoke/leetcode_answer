#同主站53题
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        sums=nums[0]
        maxs=nums[0]
        for i in range(1,len(nums)):
            sums=max(sums+nums[i],nums[i])
            maxs=max(sums,maxs)
        return maxs