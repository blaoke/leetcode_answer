class Solution:
    def missingNumber(self, nums: [int]) -> int:
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if mid==nums[mid]:
                l=mid+1
            elif mid<nums[mid]:
                if mid-1==nums[mid-1] or mid==0:
                    return mid
                else:
                    r=mid-1
        if l==n: #如果数组全是按照严格递增排列的,那么就应该返回数组长度,eg:[0,1,2,3] 或者[0]
            return n
print(a.missingNumber(nums=[0,1,3]))