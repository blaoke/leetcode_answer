#方法一:自己方法,判断条件太过啰嗦
class Solution:
    def search(self, nums: [int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[l]>target and nums[mid]>target:
                if nums[l]<=nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[l]>=target and nums[mid]<target:
                if nums[l]==target:
                    return l
                l=mid+1
            elif nums[l]<=target and nums[mid]>target:
                if nums[l]==target:
                    return l
                r=mid-1
            elif nums[l]<target and nums[mid]<target:
                if nums[l]<=nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

a=Solution()
print(a.search(nums = [5,1,3], target = 5))
#方法二:官方方法,mid的左边和右边总有一方是有序的
class Solution:
    def search(self, nums: [int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid

            elif nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1



