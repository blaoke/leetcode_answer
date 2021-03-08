class Solution:
    def maxProduct(self, nums: [int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        res=float('-inf')
        maxs,mins=1,1 #定义到当前位置的最大和最小乘积
        for k in range(n):
            tmp1=maxs*nums[k] #tmp1和tmp2存储前一位置的最大值和最小值与当前位置的乘积,由于当前位置的正负不固定,所以这两个值大小不一定
            tmp2=mins*nums[k]
            maxs=max(tmp1,tmp2,nums[k])
            res=max(res,maxs)
            mins=min(tmp1,tmp2,nums[k])
        return res
a=Solution()
print(a.maxProduct(nums=[2,-5,-2,-4,3]))