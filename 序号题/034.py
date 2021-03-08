#同剑指offor53.1题
#使用两次二分查找,分别查找target的start位置和end位置,然后返回[start,end]
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        def start_search(nums,target,left,right): #寻找start
            if left>right:
                return -1
            mid_index=(left+right)//2
            mid=nums[mid_index]
            if mid==target:
                if mid_index==0 or mid_index>0 and nums[mid_index-1]!=target: #如果是头元素或者不是头元素但前一个元素!=target,说明当前元素的start
                    return mid_index
                else:
                    right=mid_index-1
            elif mid>target:
                right=mid_index-1
            else:
                left=mid_index+1
            return start_search(nums,target,left,right)

        def end_search(nums,target,left,right): #寻找end
            if left>right:
                return -1
            mid_index=(left+right)//2
            mid=nums[mid_index]
            if mid==target:
                if mid_index==len(nums)-1 or mid_index<len(nums)-1 and nums[mid_index+1]!=target:
                    return mid_index
                else:
                    left=mid_index+1
            elif mid>target:
                right=mid_index-1
            else:
                left=mid_index+1
            return end_search(nums,target,left,right)

        res=[-1,-1]
        if len(nums)==0:
            return res
        start=start_search(nums,target,0,len(nums)-1)
        end=end_search(nums,target,0,len(nums)-1)
        if start>-1 and end>-1:
            res=[start,end]
        return res

a=Solution()
print(a.search(nums=[5,7,7,8,8,10],target=8))