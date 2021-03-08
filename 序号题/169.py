#利用哈希表进行计算
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        a={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                a[nums[i]]+=1

        for key,value in a.items():
            if value==max(a.values()):
                maxs=key
        if a[maxs]>n//2:#个数大于一半
            return maxs

a=Solution()
a.majorityElement(nums=[2,2,1,1,1,2,2])