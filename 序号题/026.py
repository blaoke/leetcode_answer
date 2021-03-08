# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
# a=[1,1,1,5,5,2,3]
# i=0
# while i <len(a)-1:
#     if a[i]==a[i+1]:
#         a.pop(i)
#     else:
#         i+=1
# print(a)

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i=0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
a=Solution()
a.removeDuplicates(nums=[1,1,3,4,5])
