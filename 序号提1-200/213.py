#将圆形问题分解成两个问题:1.求解从[0:n-1) 2.求解从[1:n) 求这两个问题的最大值
class Solution:
    def rob(self, nums: [int]) -> int:
        lens = len(nums)
        if lens == 0:
            return 0
        if lens == 1:
            return nums[0]

        def circle(nums):
            lens = len(nums)
            if lens == 0:
                return 0
            f = pre = 0
            for x in range(lens):
                f, pre = max(nums[x] + pre, f), f
            return f
        return max(circle(nums[:-1]),circle(nums[1:]))
