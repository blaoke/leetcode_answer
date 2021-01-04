#一般方法是时间复杂度为O(n),空间复杂度为O(n),但是下面方法是空间复杂度为O(1)
# 从第0个位置开始,如果在这个位置的值与索引不相等,就交换这个值到与其对应的索引位置,如果索引位置等于这个值,说明有重复,返回这个值
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        n=len(nums)
        for i in range(n):
            a=nums[i]
            while a!=i:
                if nums[a]!=a:
                    nums[a],nums[i]=nums[i],nums[a]#交换位置
                else:
                    return a


