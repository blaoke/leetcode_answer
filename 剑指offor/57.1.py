class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        n=len(nums)
        a=0
        b=n-1
        res=[]
        summ=nums[a]+nums[b]
        while(summ!=target):
            if summ<target:
                a+=1
            if summ>target:
                b-=1
            summ=nums[a]+nums[b]
        res.append(nums[a])
        res.append(nums[b])
        return res
