class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxs=0 #可以到达的最远距离
        for i in range(n): #遍历数组,如果所能到达的最远距离小于当前位置,则返回False
            if i>maxs:
                return False
            maxs=max(maxs,i+nums[i])
        return True

