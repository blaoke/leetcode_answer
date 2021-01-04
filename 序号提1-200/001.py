# !/usr/bin/env/ python
# -*- coding:utf-8 -*-
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#

# def tod():
#     nums=input('请输入:')
#     a = list(map(int, nums.split()))
#     target=int(input('目标值:'))
#     c = len(a)
#     for i in range(c):
#
#         for j in range(i+1,c):
#             d=a[i]+a[j]
#             if d==target:
#                 print([i,j])
#                 break
#             else:
#                 continue
#         break
# tod()


# class Solution:
#     def twoSum(self, nums: [int], target: int):
#        a=nums
#        c = len(a)
#        for i in range(c):
#
#            for j in range(i + 1, c):
#                d = a[i] + a[j]
#                if d == target:
#                    print([i, j])
#                    break
#                else:
#                    continue
#            continue
#
# so=Solution()
# so.twoSum(nums=[3,2,4],target=6)

class Solution:
    def twoSum(self, nums: [int], target: int):
        a={}
        b=[]
        for i in range(len(nums)):
            tar=target-nums[i]
            if tar in a:
                b.append(a[tar])
                b.append(i)
                break
            else:
                a[nums[i]] = i
        print(b)
so=Solution()
so.twoSum(nums=[3,2,4],target=6)


