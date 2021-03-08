# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        print(nums)
a=Solution()
a.removeElement(nums=[1,2,3,0,5,6,2],val=2)