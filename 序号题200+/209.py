#利用滑动窗口解决,r,l为两个指针
class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        ls=len(nums)+1
        l=0
        r=-1#初始状态[L,r]不包含任意元素
        sums=0
        while l<len(nums) :
            if sums<s and r+1<len(nums):
                r+=1
                sums+=nums[r]
            else:
                sums-=nums[l]
                l+=1
            if sums>=s:
                ls=min(ls,r-l+1)
        if ls==len(nums)+1:
            return 0
        else:
            print(ls)

a=Solution()
a.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3])
