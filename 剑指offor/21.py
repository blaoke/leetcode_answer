class Solution:
    def exchange(self, nums: [int]) :
        n=len(nums)
        if n==0:
            return []
        if n==1:
            return nums
        left=0
        right=n-1
        while left<right:
            while left<right and not self.rule( nums[left] ):
                left+=1
            while left<right and self.rule(nums[right]):
                right-=1
            nums[left],nums[right]=nums[right],nums[left]
        return nums
    def rule(self,x):
        return x%2==0

a=Solution()
print(a.exchange(nums=[1,2,3,4]))


1
[1,2,3,4]