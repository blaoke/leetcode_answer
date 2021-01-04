#方法一:常规方法,利用字典统计每个元素次数,最后如果次数最大的元素次数>一半,就返回
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
        if a[maxs]>n//2:
            return maxs

#方法二:摩尔投票法,假设第一个元素为众数,ans=1,如果下一个数等于众数,则ans+=1,如果下一个数不是众数,就ans-=1,当ans=0时设置下一个访问到的数为众数,
#以此类似进行,直到列表最后,ans>0时,返回那个众数
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            if ans == 0:
                res=nums[i]
            if nums[i]==res:
                ans+=1
            else:
                ans-=1
        if ans>0:
            return res
