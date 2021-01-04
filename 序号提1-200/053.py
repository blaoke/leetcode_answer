# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
#方法一：分而治之法
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        sums=[0 for i in range(len(nums))]
        sums[0]=nums[0]
        for i in range(1,len(nums)):
            sums[i]=max(sums[i-1]+nums[i],nums[i])
        print(max(sums))
a=Solution()
a.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])
#方法一的变形版
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+max(nums[i-1],0)
        print(max(nums))
a=Solution()
a.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])

class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        sums=nums[0]
        maxs=nums[0]
        for i in range(1,len(nums)):
            sums=max(sums+nums[i],nums[i])
            maxs=max(sums,maxs)
        return maxs

