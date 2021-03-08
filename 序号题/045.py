class Solution:
    def jump(self, nums: [int]) -> int:
        n=len(nums)
        if n==1: #如果只有一个列表中只有一个元素,直接返回
            return 0
        res=0 #用于结果的返回
        maxs=0 #可以访问的范围内可以达到的最远下标
        nexts=0 #确定下一个可以到的下标
        i=0
        while i<n-1: #如果还没有达到最后
            res += 1
            target=nums[i]+i #target表示
            if target>=n-1:
                return res
            for j in range(i+1,target+1):
                if nums[j]+j>maxs:
                    maxs=nums[j]+j
                    nexts = j
            i=nexts
a=Solution()
print(a.jump(nums=[3,3,0,1,4]))