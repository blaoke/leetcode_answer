# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        a=len(nums)
        b=False
        for i in range(a):
            if target<=nums[i]:
                print(i)
                b=True
                break
        if not b:
            print(a)
a=Solution()
a.searchInsert(nums=[1,3,5,6],target=0)

